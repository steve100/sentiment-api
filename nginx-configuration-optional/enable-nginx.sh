
sudo cp sentiment.nginx /etc/nginx/sites-available/sentiment
sudo ln -s /etc/nginx/sites-available/sentiment /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

