from fastapi import APIRouter
# from ..middlewares.jwt_manager import create_jwt_token, decode_jwt_token

posts_router = APIRouter()

@posts_router.get("/all", tags=["posts"])
async def get_posts():
    return {"message": "List of posts"}

@posts_router.get("/{post_id}", tags=["posts"])
async def get_post(post_id: int):
    return {"message": f"Post with ID {post_id}"}

@posts_router.post("/", tags=["posts"])
async def create_post(title: str, content: str):
    return {"message": f"Post with title '{title}' created"}