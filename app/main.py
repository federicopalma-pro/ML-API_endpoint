import os
import hashlib
import pandas as pd
from joblib import load
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, root_validator

app = FastAPI()

# Token string defined into Dokerfile as ENV variable
TOKEN = os.environ.get("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN environment variable is missing")

model_name = "Diamonds"
version = "v1.0"

# Define the input data model


class DiamondInput(BaseModel):
    carat: float
    cut: str
    color: str
    clarity: str
    depth: float
    table: float
    x: float
    y: float
    z: float

    @root_validator(pre=True)
    def validate_input_data(cls, values):
        # Define the expected keys and types for the input data
        expected_keys = ['carat', 'cut', 'color',
                         'clarity', 'depth', 'table', 'x', 'y', 'z']
        expected_types = [float, str, str, str,
                          float, float, float, float, float]

        # Check that the input data has the expected keys and types
        for key, value, expected_type in zip(expected_keys, values.values(), expected_types):
            if key not in values:
                raise ValueError(f"{key} is missing")
            if not isinstance(value, expected_type):
                raise TypeError(
                    f"{key} must be of type {expected_type.__name__}")

        return values


# Load the trained model pipeline
pipeline = load('/code/app/models/model_diamonds_001.joblib')

# Define the API endpoint


@app.get('/')
async def model_info():
    # Return model information, version and status
    return {
        "name": model_name,
        "version": version,
        "status": "ok"
    }


@app.post('/predict_price')
async def predict_price(input_data: DiamondInput, token: str = Header(None)):

    # If the token is None, raise an HTTPException with a status code of 401
    if token is None:
        raise HTTPException(status_code=401, detail="Token is missing")

    # Compute the SHA-256 hash of the token
    token_sha256 = hashlib.sha256(token.encode()).hexdigest()

    # If the hash of the token does not match the predefined TOKEN, raise an HTTPException with a status code of 401
    if token_sha256 != TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Convert the input data to Pandas DataFrame
    input_array = pd.DataFrame(input_data.dict(exclude_unset=False), index=[0])

    # Use the pipeline to make a prediction
    prediction = pipeline.predict(input_array)

    # Create a response dict with the predicted price
    response = {'predicted_price': float(prediction)}

    return response
