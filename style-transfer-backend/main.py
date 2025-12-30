import os

import uvicorn

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

if __name__ == "__main__":
    uvicorn.run(
        "presentations.fastapi_app:app",
        host="0.0.0.0",   
        port=8000,
        log_level="info"
    )