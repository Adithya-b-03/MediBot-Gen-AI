# MediBot-Gen-AI

MediBot-Gen-AI is a conversational AI medical bot designed to provide information and assistance.

---

## How to Run

Follow these steps to set up and run the MediBot-Gen-AI application locally:

### Step 1: Clone the repository

git clone https://github.com/Adithya-b-03/MediBot-Gen-AI
cd MediBot-Gen-AI

### Step 2: Create and activate conda environment

conda create -n medibot python=3.10 -y
conda activate medibot


### Step 3: Install requirements

pip install -r requirements.txt


### step 4: Setup environment variables
Create a .env file in the root directory of your project and add your Pinecone and OpenAI credentials:

PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

### Step 5: Store embeddings to Pinecone

python store_index.py


### step 6: Run the application

python app.py

Open your browser and navigate to:
http://localhost:5000

##Tech Stack Used
Python
LangChain
Flask
GPT (OpenAI API)
Pinecone
AWS (CI/CD Deployment with GitHub Actions)

##Languages Used
Jupyter Notebook: 52.4%
Python: 18.6%
CSS: 14.9%
HTML: 13.7%


