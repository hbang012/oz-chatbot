from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import index, items, chat

# fastapi 인스턴스
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index.router)
app.include_router(items.router)
app.include_router(chat.router)
