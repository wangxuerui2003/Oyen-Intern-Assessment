# Oyen-Intern-Assessment
A simple login system with FastAPI + SQLite as backend + database and Vanilla JS as frontend.

## Requirements
Python 3.10+
<br>
SQLite3


## Setup (Manual)

**Linux Bash**
```bash
# Install the python packages needed
$ pip install -r requirements.txt

$ cd app/

# Generate a secret key for JWT authentication
$ openssl rand -hex 32 | xargs -I {} echo "SECRET_KEY={}" >> .env
```

**Windows Powershell**
```bash
# Install the python packages needed
$ pip install -r requirements.txt

$ cd app/

# Generate a secret key for JWT authentication
$ openssl rand -hex 32 | ForEach-Object { "SECRET_KEY=$_" } | Out-File -Append -Encoding utf8 -FilePath .env
```


## Setup (Docker)
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