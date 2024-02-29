from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

client = OpenAI()

class URLCheckRequest(BaseModel):
    url: str

@app.post("/check_url")
async def check_url(request: URLCheckRequest):

    prompt = f"Check if the following URL is a phishing site. You have to answer in Yes or No. I am looking for binary response only. Phishing URL is : {request.url}"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a cybersecurity analyst whose expertise lies in analyzing websites URL and detect if that is a phishing site or not!"},
            {"role": "user", "content": prompt}
        ]
    )
    return {"result": completion.choices[0].message.content}
