#!/usr/bin/env bash
#commentttttttttttttttttttttttttttttt
sudo apt-get -y update;
sudo apt-get -y install nginx;
mkdir -p /data/;
mkdir -p /data/web_static/;
mkdir -p /data/web_static/releases/;
mkdir -p /data/web_static/shared/;
mkdir -p /data/web_static/releases/test/;
echo "<html><body><h1>hello world!</h1></body></html>" | sudo tee /data/web_static/releases/test/index.html;
ln -sf /data/web_static/releases/test/ /data/web_static/current;
sudo chown -R ubuntu:ubuntu /data/;
echo "server {
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}" | sudo tee -a /etc/nginx/sites-available/default /etc/nginx/config;
sudo service nginx restart;
