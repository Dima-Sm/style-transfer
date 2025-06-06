from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from services.st_service import StyleTransferService

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
        imsize: int = Form(...),
        steps: int = Form(...),
        style_weight: float = Form(...),
        content_weight: float = Form(...),
        model_type: str = Form(None)):

    response = await style_transfer_service.transfer_style(
        content_file=content, 
        style_file=style,
        imsize=imsize,
        steps=steps,
        style_weight=style_weight, 
        content_weight=content_weight,
        model_type=model_type
    )
    
    return JSONResponse(content=response, status_code=200)

