from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def root():
    return "Trading Bot Home Route"


