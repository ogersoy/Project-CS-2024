# // For reference, project name is UPPMAX 2024/2-18 
# // Run sbatch container.sh

!/bin/bash
#interactive should be run to create the node
#interactive -A uppmax2024-2-18 -t 1:00:00 -M snowy
module load python3
module load git
module load git-lfs
module load python_ML_packages/3.11.8-cpu

pip install --upgrade pip
pip install numpy
pip install pandas
pip install matplotlib
pip install markdown
pip install  torch
# pip install -r seaborn
# pip install -r scikit-learn
# pip install -r tensorflow
# pip install -r keras

#rm -r Project-CS-2024
#git clone https://github.com/ogersoy/Project-CS-2024
git fetch https://github.com/ogersoy/Project-CS-2024
cd Project-CS-2024

#Run the python script in the container
python /lib/markdown_cleaner.py
python app.py


#install github cli, no GH on rackham so cannot do this
# (type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
# 	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
# 	&& wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
# 	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
# 	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
# 	&& sudo apt update \
# 	&& sudo apt install gh -y
#install docker
# # Add Docker's official GPG key:
# sudo apt-get update
# sudo apt-get install ca-certificates curl
# sudo install -m 0755 -d /etc/apt/keyrings
# sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
# sudo chmod a+r /etc/apt/keyrings/docker.asc

# # Add the repository to Apt sources:
# echo \
#   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
#   $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
#   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# sudo apt-get update
# sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# #install other dependencies
# sudo apt install gh
# sudo apt-get update
# sudo apt-get install git-lfs
# sudo apt-get install python3-pip
# git init
# gh auth login
# gh repo clone Project-CS-2024

