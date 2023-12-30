#!/usr/bin/env bash
# Script that configures Nginx server with some folders and files

# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get -y install nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create or update symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/hbnb_static/!b;n;c\\talias /data/web_static/current/;' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
