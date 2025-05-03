from fastapi import FastAPI, Depends, Form
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para insertar datos mediante un formulario
@app.post("/users/")
async def create_user(name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(content={"message": "User created", "user": {"name": new_user.name, "email": new_user.email}})
