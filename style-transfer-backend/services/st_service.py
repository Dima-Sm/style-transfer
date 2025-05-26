from fastapi.responses import JSONResponse
from PIL import UnidentifiedImageError
import uuid
import os
from utils.style_transfer import get_device, get_vgg19, run_style_transfer
from utils.image_preparation import get_content_image_size, image_loader, save_image

class StyleTransferService():
    def __init__(self):
        ...
    async def transfer_style(self, content, style, imsize, steps, style_weight, content_weight):
        try:
            allowed_types = ["image/jpeg", "image/png"]
            if content.content_type not in allowed_types:
                return JSONResponse(status_code=400, content={"error": "Content file must be an image (JPEG or PNG)."})
            if style.content_type not in allowed_types:
                return JSONResponse(status_code=400, content={"error": "Style file must be an image (JPEG or PNG)."})

            content_bytes = await content.read()
            style_bytes = await style.read()

            device = get_device()

            try:
                width, height = get_content_image_size(content_bytes)
                content_img = image_loader(content_bytes, imsize, device)
                style_img = image_loader(style_bytes, imsize, device)
                input_img = content_img.clone()

            except UnidentifiedImageError:
                return JSONResponse(status_code=400, content={"error": "Uploaded files must be valid images."})

            cnn = get_vgg19()

            output = run_style_transfer(
                cnn, content_img, style_img, input_img,
                num_steps=steps,
                style_weight=style_weight,
                content_weight=content_weight
            )

            # output_filename = f"{uuid.uuid4().hex}.jpg"
            # output_path = os.path.join("static", output_filename)
            img_str = save_image(output, width, height)
            data_url = f"data:image/jpeg;base64,{img_str}"

            return {"output_image": data_url}

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": f"Unexpected error: {str(e)}"})