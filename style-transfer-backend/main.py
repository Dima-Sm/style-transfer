import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 
import uvicorn

def main():
    uvicorn.run("presentations.fastapi_app:app", host="localhost", port=8000)

if __name__ == "__main__":
    main()