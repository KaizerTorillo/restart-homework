from fastapi import FastAPI

app = FastAPI()

# The @ is a decorator.
# uvicorn main:app --reload

@app.get("/")
async def root():
    return {"message": "Hello World"}