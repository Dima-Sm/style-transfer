import io
import base64
import torch 
import torchvision.transforms as transforms
from PIL import Image

class ImageProcessor:
    def __init__(self, imsize: int, device: torch.device):
        self.imsize = imsize
        self.device = device
        self.loader = transforms.Compose([
            transforms.Resize((imsize, imsize)),  
            transforms.ToTensor()
        ])
        self.unloader = transforms.Compose([
            transforms.ToPILImage()
        ]) 

    def load(self, image_bytes: bytes) -> torch.Tensor:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = self.loader(image).unsqueeze(0)
        return (image.to(self.device, torch.float32))
    
    def unload(self, tensor: torch.Tensor, width: int, height: int) -> str:
        image = tensor.cpu().clone().squeeze(0)
        image = self.unloader(image)
        image = image.resize((width, height))
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")
        buffer.seek(0)
        img_str = base64.b64encode(buffer.read()).decode("utf-8")
        return img_str
    
    def get_size(self, image_bytes: bytes) -> tuple[int, int]:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        return image.size
