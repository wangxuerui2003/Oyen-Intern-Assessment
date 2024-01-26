FROM python:3.10.13-slim-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends \
	openssl \
	&& rm -rf /var/lib/apt/lists/*

COPY . /src

RUN python3.10 -m pip install -r /src/requirements.txt

WORKDIR /src/app

RUN cp ../.env.example .env.local
RUN secret_key=$(openssl rand -hex 32) && sed -i "s/SECRET_KEY=.*/SECRET_KEY=$secret_key/" .env.local

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]s
