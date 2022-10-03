from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Charlemagne', 'age': 29}}


@app.get('/about')
def about():
    return {'data': 'This is about page'}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")