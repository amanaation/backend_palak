import requests

payload = {
  "name": "string",
  "email": "string",
  "dob": "string",
  "password": "string"
}

res = requests.post("http://127.0.0.1:8000/register/", json=payload)


print(res, res.json())
