from fastapi import APIRouter

login_router = APIRouter()

@login_router.get("/login", tags=["auth"])
async def login(username: str, password: str):
    """
    Simulate a login process. In a real application, you would verify the username and password.
    """
    if username == "admin" and password == "password":
        return {"message": "Login successful", "username": username}
    else:
        return {"message": "Invalid credentials"}