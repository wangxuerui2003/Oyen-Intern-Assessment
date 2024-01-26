#!/bin/bash

if [ ! -f .env.local ] then
	cp ../.env.example .env.local
	secret_key=$(openssl rand -hex 32)
	sed -i "s/SECRET_KEY=.*/SECRET_KEY=$secret_key/"
fi


exec "$@"