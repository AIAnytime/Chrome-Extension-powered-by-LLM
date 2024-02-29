from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# CORS setup for Chrome Extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This is for example purposes, specify your extension's ID in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestData(BaseModel):
    request: str  # Dummy request data, not used in this example

@app.post("/random_fact/")
async def random_fact(data: RequestData):
    # Mock function to generate a random fact
    facts = [
        "The number 7 is considered lucky in many cultures.",
        "Zero is the only number that cannot be represented by Roman numerals.",
        "A 'googol' is the number 1 followed by 100 zeros.",
    ]
    random_fact = random.choice(facts)
    return {"fact": random_fact}
