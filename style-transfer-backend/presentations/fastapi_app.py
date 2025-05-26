from fastapi import FastAPI
from fastapi import UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from services.st_service import StyleTransferService
import json

app = FastAPI(title = "Visual style transfer")
style_transfer_service = StyleTransferService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transfer")
async def process_image(
        content: UploadFile = File(...),
        style: UploadFile = File(...),
        imsize: int = Form(512),
        steps: int = Form(300),
        style_weight: float = Form(1e5),
        content_weight: float = Form(1)):
    print(content)
    response = await style_transfer_service.transfer_style(content=content, style=style,imsize=imsize,steps=steps,style_weight=style_weight, content_weight=content_weight)
    response_data = response.body  # Получаем bytes
    response_dict = json.loads(response_data.decode('utf-8'))
    print(response_dict) 
    return response_dict