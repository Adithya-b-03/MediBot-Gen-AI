# MediBot-Gen-AI

How to run?
STEPS:
Clone the repository

Project repo: https://github.com/
STEP 01- Create a conda environment after opening the repository
conda create -n medibot python=3.10 -y
conda activate medibot
STEP 02- install the requirements
pip install -r requirements.txt
Create a .env file in the root directory and add your Pinecone & openai credentials as follows:
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# run the following command to store embeddings to pinecone
python store_index.py
# Finally run the following command
python app.py
Now,

open up localhost:
Techstack Used:
Python
LangChain
Flask
GPT
Pinecone
AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
OPENAI_API_KEY
About
No description, website, or topics provided.
Resources
 Readme
License
 MIT license
 Activity
Stars
 72 stars
Watchers
 1 watching
Forks
 62 forks
Report repository
Releases
No releases published
Packages
No packages published
Languages
Jupyter Notebook
52.4%
 
Python
18.6%
 
CSS
14.9%
 
HTML
13.7%
 
Dockerfile
0.4%
Footer
