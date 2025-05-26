from torch import float as fl
import torchvision.transforms as transforms

from PIL import Image
import io

def get_content_image_size(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    width, height = image.size
    return width, height

def image_loader(image_bytes, imsize, device):
    
    loader = transforms.Compose([
        transforms.Resize((imsize, imsize)),  
        transforms.ToTensor()])  
    
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    # fake batch dimension required to fit network's input dimensions
    image = loader(image).unsqueeze(0)

    return image.to(device, fl)

def save_image(tensor, content_w, content_h, path):

    unloader = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((content_h, content_w))])  
    
    image = tensor.cpu().clone().squeeze(0)
    image = unloader(image)
    image.save(path)
