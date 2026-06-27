from fastapi import FastAPI, Request
from fastapi.templating import  Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory='templates')

with open('Diamond-Model-Complete.pkl', 'rb') as f:
    save_data = pickle.load(f)
    model = save_data['model']
    encoders = save_data['encoders']
    scaler = save_data['scaler']

class DiamondFeatures(BaseModel):
    carat : float
    cut : str
    color: str
    clarity : str
    depth : float
    table : float
    x : float
    y : float
    z : float

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.patch('/predict')
async def predict(features: DiamondFeatures):
    input_data = pd.DataFrame([features.model_dump()])
    print(input_data)

    for col in ['cut', 'color', 'clarity']:
        input_data[col] = encoders[col].transform(input_data[col])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    return {'prediction_price': prediction[0]}
