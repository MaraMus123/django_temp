#!/bin/bash
cd ~/django_template || exit 1

echo "[+] Pulling latest code"
git pull origin main || exit 1

echo "[+] Rebuilding and restarting app"
docker compose -f docker-compose.deploy.yml down
docker compose -f docker-compose.deploy.yml up -d --build
