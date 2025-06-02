from fastapi.responses import JSONResponse
from PIL import UnidentifiedImageError

from utils.image_preparation import get_content_image_size, image_loader, save_image
from utils.st_strategies import get_strategy
from utils.st_config import TransferConfigBuilder
from utils.st_facade import StyleTransferFacade


class StyleTransferService():
    def __init__(self):
        self.allowed_types = ["image/jpeg", "image/png"]

    async def transfer_style(self, content_file, style_file, imsize, steps, style_weight, content_weight, model_type):
        try:
            if content_file.content_type not in self.allowed_types:
                return JSONResponse(status_code=400, content={"error": "Content file must be an image (JPEG or PNG)."})
            if style_file.content_type not in self.allowed_types:
                return JSONResponse(status_code=400, content={"error": "Style file must be an image (JPEG or PNG)."})

            content_bytes = await content_file.read()
            style_bytes = await style_file.read()

            try:
                width, height = get_content_image_size(content_bytes)
            except UnidentifiedImageError:
                return JSONResponse(status_code=400, content={"error": "Uploaded files must be valid images."})
            
            strategy = get_strategy(model_type)
            config = (TransferConfigBuilder()
                      .with_steps(steps)
                      .with_imsize(imsize)
                      .with_style_weight(style_weight)
                      .with_content_weight(content_weight)
                      .with_strategy(strategy)
                      .build())
            
            try:
                content_img = image_loader(content_bytes, imsize, config.device)
                style_img = image_loader(style_bytes, imsize, config.device)
            except UnidentifiedImageError:
                return JSONResponse(status_code=400, content={"error": "Uploaded files must be valid images."})
            
            facade = StyleTransferFacade(config)
            output_img = facade.transfer_style(
                content_img=content_img,
                style_img=style_img
                )

            img_str = save_image(output_img, width, height)
            data_url = f"data:image/jpeg;base64,{img_str}"

            return {"output_image": data_url}

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": f"Unexpected error: {str(e)}"})