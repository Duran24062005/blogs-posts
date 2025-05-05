from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/all", tags=["users"])
async def get_users():
    return {"message": "List of users"}


@user_router.get("/{user_id}", tags=["users"])
async def get_user(user_id: int):
    return {"message": f"User with ID {user_id}"}

@user_router.post("/", tags=["users"])
async def create_user(name: str, email: str):
    return {"message": f"User {name} with email {email} created"}