FROM debian:buster

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y --no-install-recommends \
	python3.10 \
	openssl \
	&& rm -rf /var/lib/apt/lists/*

COPY . /src

RUN python3.10 -m pip install -r requirements.txt

WORKDIR /src/app

EXPOSE 8000

COPY ./docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]


