from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models, database

# Créer l'application FastAPI
app = FastAPI()

class User(BaseModel):
    name: str
    age: int


# Initialiser la base de données
models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return  "Welcome to the FastAPI app connected to PostgreSQL"

@app.post("/users/")
def create_user(user: User, db: Session = Depends(database.get_db)):
    new_user = models.Users(name=user.name, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/")
def read_users(db: Session = Depends(database.get_db)):
    users = db.query(models.Users).all()

    return users
