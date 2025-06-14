from fastapi import FastAPI, Depends
from . import auth, models
from .database import engine
from .dependencies import get_current_user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)

@app.get("/users/me")
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return {"email": current_user.email}