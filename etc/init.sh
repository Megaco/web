#!/usr/bin/env bash
tmux attach -t base || tmux new -s base
sudo apt-get update
sudo apt-get install -y nginx
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#cd /home/box/web/venev
#source bin/activate
#cd ../

#sudo ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py

cd /home/box/web
virtualenv --python=python3 --always-copy venv
source venv/bin/activate

pip install gunicorn
pip install Django
#django-admin startproject ask
#gunicorn hello:application

#gunicorn -c /home/box/web/etc/gunicorn_settings.py /home/box/web/ask/ask/wsgi.py
#cd ask
gunicorn -w 1 -b 0.0.0.0:8000 ask.wsgi --pythonpath ask
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart