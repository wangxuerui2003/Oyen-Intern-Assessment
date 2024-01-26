# Oyen-Intern-Assessment
A simple login system with FastAPI + SQLite as backend + database and Vanilla JS as frontend.

## Requirements
Python 3.10+
<br>
SQLite3


## Manual Setup

**Linux Bash / Windows Powershell**
```bash
# Install the python packages needed
$ pip install -r requirements.txt

# Bash
$ cp .env.example ./app/.env.local
# Powershell
$ Copy-Item -Path .\.env.example -Destination .\app\.env.local

$ cd app/

# Generate a secret key for JWT authentication
$ openssl rand -hex 32  # copy the output

# Use your favourite text editor to open the .env.local file
# Paste the secret key to the SECRET_KEY field
```


## Docker Setup (Recommended)
TODO


## Run it

**Manual**
```bash
$ cd app/

# Testing
$ uvicorn main:app --reload

# Production
$ uvicorn main:app --host 0.0.0.0 --port <desired-port>
```

**Docker**
```bash
$ docker build -t <your-image-name>:<tag> .
$ docker run -d -p <host-port>:8000 --name <your-container-name> <your-image-name>
```


## Usage
```
	1. Run the FastAPI server
	2. Open a Web Browser and navigate to localhost:8000
	3. Login if you already have an account, otherwise click register and register an account.
	4. Successfully login to the Home Page!
```

[Video Demo](https://youtu.be/cbQDFnTLHhM)


## Author
- [Wang Xue Rui (Ray)](https://github.com/wangxuerui2003)