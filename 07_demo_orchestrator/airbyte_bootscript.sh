#!/usr/bin/env bash
yum update -y

# install ssm
yum install -y https://s3.${region}.amazonaws.com/amazon-ssm-${region}/latest/${linux_type}/amazon-ssm-agent.rpm
systemctl enable amazon-ssm-agent 
systemctl start amazon-ssm-agent

# install and start docker
amazon-linux-extras install docker -y
service docker start

# install docker compose
wget https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m) -O /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# add ec2-user to group that can access docker
sudo groupadd docker
sudo usermod -aG docker ec2-user

# install and start airbyte
cd /home/ec2-user
mkdir airbyte && cd airbyte
wget https://raw.githubusercontent.com/airbytehq/airbyte/master/{.env,docker-compose.yaml}
docker-compose up -d