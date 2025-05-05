from fastapi import FastAPI
import os
from fastapi.responses import FileResponse
from routes.auth.login import login_router
from routes.user_routes import user_router
from routes.posts_routes import posts_router

app = FastAPI(
    title="🌐Backend with FastAPI for Posts🖥",
    description="📂A simple FastAPI application with SQLAlchemy and SQLite⛃",
    version="1.0.0",
    # openapi_tags=[
    #     {
    #         "name": "users",
    #         "description": "Operations with users",
    #     },
    #     {
    #         "name": "posts",
    #         "description": "Operations with posts",

    #     },
    # ],
)

@app.get("/")
async def root():
    file_path = os.path.join(os.path.dirname(__file__), "welcome.html")
    return FileResponse(file_path)

app.include_router(login_router, prefix="/api/v1/auth")
app.include_router(user_router, prefix="/api/v1/users") 
app.include_router(posts_router, prefix="/api/v1/posts")