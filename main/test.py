import requests

payload = {
  "name": "string",
  "email": "string",
  "dob": "string",
  "gender": "Male",
  "password": "string"
}

# res = requests.get("http://127.0.0.1:8000/")
res = requests.post("http://127.0.0.1:8000/validate_registeration/", json=payload)


print(res)
