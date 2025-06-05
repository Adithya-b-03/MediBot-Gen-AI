# MediBot-Gen-AI

## How to Run

### Step 1: Clone the repository
```bash
git clone https://github.com/<your-repo>.git
cd MediBot-Gen-AI
Step 2: Create and activate conda environment
bash
Copy
Edit
conda create -n medibot python=3.10 -y
conda activate medibot
Step 3: Install requirements
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Setup environment variables
Create a .env file in the root directory and add your Pinecone & OpenAI credentials:

ini
Copy
Edit
PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Step 5: Store embeddings to Pinecone
bash
Copy
Edit
python store_index.py
Step 6: Run the application
bash
Copy
Edit
python app.py
Open your browser and navigate to:
http://localhost:5000

Tech Stack Used
Python

LangChain

Flask

GPT (OpenAI API)

Pinecone

AWS (CI/CD Deployment with GitHub Actions)

Docker

AWS Deployment Instructions
Login to AWS console.

Create IAM User with these access policies:

AmazonEC2ContainerRegistryFullAccess

AmazonEC2FullAccess

Create an ECR (Elastic Container Registry) repository to store your Docker image.
Example URI:
970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot

Create an EC2 machine (Ubuntu).

Install Docker on EC2:

bash
Copy
Edit
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
Build the Docker image from your source code and push it to ECR.

Pull your Docker image from ECR on EC2 and launch the Docker container.

(Optional) Configure EC2 as a GitHub self-hosted runner:
GitHub Settings > Actions > Runner > New self-hosted runner, choose OS, then run the provided commands on your EC2 instance.

Setup GitHub Secrets for CI/CD:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_DEFAULT_REGION

ECR_REPO

PINECONE_API_KEY

OPENAI_API_KEY

Repository Stats
Stars: 72

Forks: 62

Languages used
Jupyter Notebook 52.4%

Python 18.6%

CSS 14.9%

HTML 13.7%

Dockerfile 0.4%

License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

You can copy-paste this into your `README.md` in your repo root.  
Let me know if you want me to generate it as a file for you!
