sudo apt-get update
sudo apt-get install -y nginx
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#cd /home/box/web/venev
#source bin/activate
#cd ../

sudo ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py

cd /home/box/web
virtualenv --python=python3 --always-copy venv
pip install gunicorn
#gunicorn hello:application
gunicorn -b 0.0.0.0:8080 hello:application
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart