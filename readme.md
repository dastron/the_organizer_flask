Let's keep this as short as possible.


### APP UPDATES:
Given that this is a flask app we will need to leverage a runner or manager. In this case we are using gunicorn, because I was using flask-scripts this step took extra time to properly debug and get it running.

Logging, so that in production we can monitor the state of the application.


### VM:
Debian 8.0
1 CPU & 3.75GB of RAM

- Update Packages
	`sudo apt-get update`
	`sudo apt-get upgrade`
- Install App Related Packages
	`sudo apt-get install`:
		-build-essential
		-supervisor
		-python
		-python-dev
		-python-pip
		-libffi-dev
		-nginx
	    -npm

- Configure Nginx
	Remove default # `rm /etc/nginx/sites-enabled/default`
	Create new config # `nano /etc/nginx/sites-available/the-flask-org`
	Create Symbolic link to enabled config`ln -s /etc/nginx/sites-available/the-flask-org /etc/nginx/sites-enabled/`
	Check to see if config is valid`nginx -t`
	Reload Nginx (Debian) `/etc/init.d/nginx reload`

- Navigate to root folder & clone GIT Repo
	# `git clone https://github.com/googler4/the_organizer_flask.git`

- App / Execution 
	Create user to run app # `useradd -m -d /home/app app`
	Create Venv # `virtualenv venv`
	Install Dependencies # `pip install -r requirements.txt`
	Change Owner # `chown -R app:app /opt/app`
	Run Gunicorn:
	`gunicorn manage:app --bind 0.0.0.0:5000
		autostart=true
		autorestart=true
		user=pythonapp`

#### Startup script:
Every time the machine restarts, we install required programs, pull new code from repo, and re-install dependencies. 

Python: Install, setup and update Python & PIP.
Nginx: Install, create config and create symbolic link, and remove default config.
Create user: From which we will run our flask app and only our flask app.
Setup and Run via gunicorn run by supervisor.

#### Firewall:
Updated the roles, added the custom SSH port 9200


