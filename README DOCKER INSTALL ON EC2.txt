
Firs of all dont use ngix! 
Disable Nginx to Prevent it from Starting on Boot
$ sudo systemctl stop nginx

Step 2: Verify Nginx is Stopped
$sudo systemctl disable nginx

You can check if Nginx has stopped by running:
$sudo systemctl status nginx




install Docker using apt if you are using an EC2 instance running a Debian-based distribution such as Ubuntu. Here are the steps to install Docker on an Ubuntu EC2 instance:

1. Update the package index
First, update your package index:

sh
Copy code
sudo apt-get update
2. Install required packages
Install the required packages to allow apt to use a repository over HTTPS:

sh
Copy code
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
3. Add Docker’s official GPG key
Add Docker’s official GPG key:

sh
Copy code
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
4. Set up the Docker repository
Add the Docker repository to apt sources:

sh
Copy code
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
5. Update the package index again
Update the package index again to include the Docker packages:

sh
Copy code
sudo apt-get update
6. Install Docker Engine
Install Docker Engine:

sh
Copy code
sudo apt-get install docker-ce docker-ce-cli containerd.io
7. Start the Docker service
Start the Docker service:

sh
Copy code
sudo systemctl start docker
8. Enable Docker to start on boot
Enable Docker to start automatically at boot time:

sh
Copy code
sudo systemctl enable docker
9. Add your user to the Docker group
To run Docker commands without sudo, add your user to the Docker group:

sh
Copy code
sudo usermod -aG docker $USER
Note: You'll need to log out and log back in for this change to take effect.

10. Verify Docker installation
Verify that Docker is installed correctly by running a test container:

sh
Copy code
docker run hello-world
11. Install Docker Compose (Optional)
If you need Docker Compose, you can install it as well:

sh
Copy code
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -Po '(?<="tag_name": ")[^"]*')/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
Make the Docker Compose binary executable:

sh
Copy code
sudo chmod +x /usr/local/bin/docker-compose
Verify the installation:

sh
Copy code
docker-compose --version
Summary of Commands
sh
Copy code
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
docker run hello-world
For Docker Compose (optional):

sh
Copy code
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -Po '(?<="tag_name": ")[^"]*')/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
After completing these steps, Docker and Docker Compose (if installed) should be ready to use on your EC2 instance running Ubuntu.