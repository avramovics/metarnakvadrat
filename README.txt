1. install python3 and all dependencies on EC2 use Ubuntu server. 

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




Check Disk Space:
Ensure that your system has enough disk space:

$ df -h


