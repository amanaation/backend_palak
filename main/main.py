from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.responses import HTMLResponse
from pprint import pprint

from models import User
from actions import *
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

@app.get("/")
def serve_home(request: Request):
    with open("static/Index.html") as file:
        html_response = file.read()

    return HTMLResponse(content=html_response, status_code=200)


@app.get("/login")
def serve_home(request: Request):
    with open("static/Login.html") as file:
        html_response = file.read()

    return HTMLResponse(content=html_response, status_code=200)


@app.get("/register")
def serve_home(request: Request):
    with open("static/Registration.html") as file:
        html_response = file.read()

    return HTMLResponse(content=html_response, status_code=200)

@app.get("/asses")
def serve_home(request: Request):
    with open("static/assesment.html") as file:
        html_response = file.read()

    return HTMLResponse(content=html_response, status_code=200)


@app.post("/result")
def serve_home(request: Request):
    pprint(request.__dict__)
    return {"message": "Some message"}

    # with open("static/assesment.html") as file:
    #     html_response = file.read()

    # return HTMLResponse(content=html_response, status_code=200)

@app.post("/validate_registeration/")
def register(item:User):
    if registerUser(item):
        return {"Message": "User Registered successfully", "success": True}
    return {"Message": "Unable to register user", "success": False}

@app.post("/validate_login/")
def login(item:User):
    uname = item['uname']
    password = item['password']

    if validate(uname, password):
        return {"Message": "Login Succesfull", "success": True}
    return {"Message": "Invalid Login/Password", "success": False}


if __name__ == "__main__":
    uvicorn.run(app)