server {
    listen 80;
    server_name localhost 127.0.0.1;

    # serve static the same way
    location /static/ {
        alias /vol/static/;
        access_log off;
        expires 7d;
    }

    # proxy directly to your app (no HTTPS redirect)
    location / {
        uwsgi_pass ${APP_HOST}:${APP_PORT};
        include /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }
}


