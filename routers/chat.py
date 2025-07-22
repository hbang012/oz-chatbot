from fastapi import APIRouter
from openai import OpenAI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv(".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

router = APIRouter()
client = OpenAI(api_key=OPENAI_API_KEY)


class ChatRequest(BaseModel):
    message: str


# 새로운 응답 생성이므로 post
@router.post("/chat")
def chat(chat: ChatRequest):
    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions="""친근한 반말로 답변하세요.""",
        input=[
            {
                "role": "developer",
                "content": "이전 대화를 기억하고 연속적인 답변을 제공하세요.",
            },
            {"role": "user", "content": chat.message},
        ],
    )
    return {"response": response.output_text}
