from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import Pinecone
from langchain_openai import ChatOpenAI
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *  # Make sure system_prompt is defined here
import os

app = Flask(__name__)

load_dotenv()

# Set API keys
# os.environ["PINECONE_API_KEY"] = "pcsk_4F6tjY_99kkDkaKWPVBoakaMRjp2pLcL7Yq6MVC7YSrzeUuSP6dncHpCuuaDb92xVp1ZY6"
# os.environ["OPENAI_API_KEY"] = "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"
# os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"


# Embedding
embeddings = download_hugging_face_embeddings()

# Pinecone vectorstore
index_name = "medicalbot"
docsearch = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# LLM from OpenRouter
llm = ChatOpenAI(
    temperature=0.4,
    max_tokens=500,
    model="gpt-3.5-turbo",
    openai_api_key=os.environ["OPENAI_API_KEY"],
    openai_api_base=os.environ["OPENAI_API_BASE"]
)

# Prompt template and chain
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('chat.html')

from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import Pinecone
from langchain_openai import ChatOpenAI
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *  # Make sure system_prompt is defined here
import os

app = Flask(__name__)

load_dotenv()

# Set API keys
# os.environ["PINECONE_API_KEY"] = "pcsk_4F6tjY_99kkDkaKWPVBoakaMRjp2pLcL7Yq6MVC7YSrzeUuSP6dncHpCuuaDb92xVp1ZY6"
# os.environ["OPENAI_API_KEY"] = "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"
# os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"


# Embedding
embeddings = download_hugging_face_embeddings()

# Pinecone vectorstore
index_name = "medicalbot"
docsearch = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# LLM from OpenRouter
llm = ChatOpenAI(
    temperature=0.4,
    max_tokens=500,
    model="gpt-3.5-turbo",
    openai_api_key=os.environ["OPENAI_API_KEY"],
    openai_api_base=os.environ["OPENAI_API_BASE"]
)

# Prompt template and chain
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = rag_chain.invoke({"input": msg})
    return str(response["answer"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
