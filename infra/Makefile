setup:
	sudo apt update
	sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl


setup_db:
	sudo -u postgres psql
	CREATE DATABASE ${DATABASE_NAME};
	CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASSWORD}';
	ALTER ROLE ${DB_USER} SET client_encoding TO 'utf8';
	ALTER ROLE ${DB_USER} SET default_transaction_isolation TO 'read committed';
	ALTER ROLE ${DB_USER} SET timezone TO 'UTC';
	GRANT ALL PRIVILEGES ON DATABASE ${DATABASE_NAME} TO ${DB_USER};
	\q

setup_venv:
	mkdir ${PROJECT_DIR}
	cd ${PROJECT_DIR}
	git clone git@github.com:martim-lusofona/class-ping.git
	sudo apt install pipenv
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt update
	sudo apt install python3.12 python3.12-venv python3.12-dev
	pipenv shell
	pipenv install
	

create_pre:
	set -a && source .env && set +a && envsubst < ./Makefile > ./Makefile.new

setup_gunicord_socket:
	sudo nano /etc/systemd/system/gunicorn.socket

setup_gunicord_service:
	sudo nano /etc/systemd/system/gunicorn.service

start_gunicord:
	sudo systemctl start gunicorn.socket
	sudo systemctl enable gunicorn.socket

setup_nginx:
	sudo nano /etc/nginx/sites-available/${PROJECT_NAME}
	sudo ln -s /etc/nginx/sites-available/${PROJECT_NAME} /etc/nginx/sites-enabled
	sudo nginx -t
	sudo systemctl restart nginx
	sudo ufw allow 'Nginx Full'

setup_ssl:
	sudo snap install core; sudo snap refresh core
	sudo apt remove certbot
	sudo snap install --classic certbot
	sudo ln -s /snap/bin/certbot /usr/bin/certbot
	sudo ufw status
	sudo ufw allow 'Nginx Full'
    sudo ufw delete allow 'Nginx HTTP'
	sudo ufw status
	sudo certbot --nginx -d classping.org -d *.classping.org
	sudo systemctl status snap.certbot.renew.service

setup_staticpermissions:
	sudo chown -R www-data:www-data /root/class-ping/class-ping/staticfiles
	sudo chmod -R 755 /root/class-ping/class-ping/staticfiles
	sudo find /root/class-ping/class-ping/staticfiles -type f -exec chmod 644 {} \;
	sudo chmod +x /root
	sudo chmod +x /root/class-ping
	sudo chmod +x /root/class-ping/class-ping
	sudo systemctl restart nginx