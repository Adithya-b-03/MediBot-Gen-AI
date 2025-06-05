MediBot-Gen-AI
MediBot-Gen-AI is a conversational AI medical bot designed to provide information and assistance.

How to Run
Follow these steps to set up and run the MediBot-Gen-AI application locally:

Step 1: Clone the repository
Bash

git clone https://github.com/Adithya-b-03/MediBot-Gen-AI
cd MediBot-Gen-AI
Step 2: Create and activate conda environment
Bash

conda create -n medibot python=3.10 -y
conda activate medibot
Step 3: Install requirements
Bash

pip install -r requirements.txt
Step 4: Setup environment variables
Create a .env file in the root directory of your project and add your Pinecone and OpenAI credentials:

Ini, TOML

PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Step 5: Store embeddings to Pinecone
Bash

python store_index.py
Step 6: Run the application
Bash

python app.py
Open your browser and navigate to: http://localhost:5000

Tech Stack Used
Python
LangChain
Flask
GPT (OpenAI API)
Pinecone
AWS (CI/CD Deployment with GitHub Actions)
Docker
AWS Deployment Instructions
This section outlines the steps to deploy MediBot-Gen-AI on AWS using Docker and GitHub Actions for CI/CD.

1. Login to AWS console.
2. Create IAM User
Create an IAM User with the following access policies:

AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess
3. Create an ECR Repository
Create an ECR (Elastic Container Registry) repository to store your Docker image.
Example URI: 970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot

4. Create an EC2 machine (Ubuntu).
5. Install Docker on EC2
Bash

sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
6. Build and Push Docker Image
Build the Docker image from your source code and push it to your ECR repository.

7. Pull and Launch Docker Container
Pull your Docker image from ECR on EC2 and launch the Docker container.

8. (Optional) Configure EC2 as a GitHub self-hosted runner:
Go to GitHub Settings > Actions > Runner > New self-hosted runner, choose your OS, then run the provided commands on your EC2 instance.

9. Setup GitHub Secrets for CI/CD:
Add the following secrets to your GitHub repository:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
OPENAI_API_KEY
Repository Stats
Stars: 72
Forks: 62
Languages Used
Jupyter Notebook: 52.4%
Python: 18.6%
CSS: 14.9%
HTML: 13.7%










