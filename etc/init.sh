sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo apt update
sudo apt install -y gunicorn
sudo apt install -y pip3
sudo pip3 install -y -r /home/box/web/etc/requirements.txt
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo gunicorn -c /etc/gunicorn.d/hello.py /home/box/web/wsgi:app
