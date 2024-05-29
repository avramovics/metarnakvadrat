1. install python3 and all dependencies on EC2 use Ubuntu server. 
$ sudo apt-get update
$ sudo apt-get install -y python3 python3-pip python3-venv
2. setup server, edit server_name to match ip adress of EC2: 
$  sudo apt install nginx
$ sudo nano /etc/nginx/sites-enabled/fastapi_nginx
server {
    listen 80;
    server_name 16.171.31.42;

    location / {
        proxy_pass http://127.0.0.1:8000;
        # Additional proxy settings can be added here if needed
    }
}

$ sudo service nginx restart


3. Install the CodeDeploy agent for Ubuntu Server follow instructions: 
https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ubuntu.html

4. setup appspec.yml 

5. start the server using tmux, this will keep the server running in background:
$ tmux
https://stackoverflow.com/questions/21193988/keep-server-running-on-ec2-instance-after-ssh-is-terminated


6. update supervizor


Copy code
sudo apt-get update
sudo apt-get install supervisor

$ which uvicorn
$ sudo nano /etc/supervisor/conf.d/myapp.conf

[program:myapp]
command=/path/to/uvicorn your_app_module:app --host 0.0.0.0 --port 8000
directory=/path/to/your/app
autostart=true
autorestart=true
stderr_logfile=/var/log/myapp.err.log
stdout_logfile=/var/log/myapp.out.log

$ sudo supervisorctl reread
$ sudo supervisorctl update
$ sudo supervisorctl start myapp 
$ sudo supervisorctl start myapp


Install 
$ sudo apt-get update
$ sudo apt-get install python3-venv

cd ~/myapp
python3 -m venv venv

Activate the Virtual Environment

$ source venv/bin/activate
Install requierments
$ pip3 install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 8000 --reload


Check Disk Space:
Ensure that your system has enough disk space:

$ df -h


