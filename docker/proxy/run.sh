#!/bin/bash

set -e

echo "Checking for dhparams.pem"

if [ ! -f "/vol/proxy/ssl-dhparams.pem" ]; then
    echo "dhparams.pem does not exist, generating a new one..."
    openssl dhparam -out /vol/proxy/ssl-dhparams.pem 2048
fi

#Avoid replacing these with envsubst
export host=\$host
export request_uri=\$request_uri

echo "Checking for fullchain.pem"
if [ ! -f "etc/letsencrypt/live/mm-mg.diamantovacky.cz/fullchain.pem" ]; then
    echo "No SSL cert, enabing HTTP only mode"
    envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
else
    echo "SSL cert found, enabling HTTPS mode"
    envsubst < /etc/nginx/default-ssl.conf.tpl > /etc/nginx/conf.d/default.conf
fi

nginx -g "daemon off;"
