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
# Testing
$ uvicorn app.main:app --reload

# Production
$ 
```

**Docker**
```bash
$ docker build -t <your-image-name>:<tag> .
$ docker run -d -p <host-port>:8000 --name <your-container-name> <your-image-name>
```


## Usage
TODO: Describe the usage in text
TODO: Film a short video


## Author
- [Wang Xue Rui (Ray)](https://github.com/wangxuerui2003)