from fastapi import FastAPI
from models import User
from actions import *
import uvicorn

app = FastAPI()


@app.post("/register/")
def register(item:User):
    if registerUser(item):
        return {"Message": "User Registered successfully", "success": True}
    return {"Message": "Unable to register user", "success": False}

@app.post("/register/")
def login(item:User):
    uname = item['uname']
    password = item['password']

    if validate(uname, password):
        return {"Message": "Login Succesfull", "success": True}
    return {"Message": "Invalid Login/Password", "success": False}


if __name__ == "__main__":
    uvicorn.run(app)