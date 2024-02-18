"""Welcome to Reflex!."""

from ethicode import styles
from ethicode.pages import *
import reflex as rx
from fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy
from pathlib import Path

## INITIALIZE
from llama_index import SimpleDirectoryReader, StorageContext, ServiceContext
from llama_index.indices.vector_store import VectorStoreIndex
from llama_iris import IRISVectorStore
from llama_index.agent import OpenAIAgent
import getpass
import os
from dotenv import load_dotenv

load_dotenv("../.env")

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

username = os.environ.get("username")
password = os.environ.get("password")
hostname = os.environ.get("hostname")
port = os.environ.get("port")
namespace = os.environ.get("namespace")
CONNECTION_STRING = f"iris://{username}:{password}@{hostname}:{port}/{namespace}"


class VectorEngine:
    _instance = None
    query_engine = None
    retriever = None

    @staticmethod
    def get_instance():
        if VectorEngine._instance is None:
            VectorEngine()
        return VectorEngine._instance

    def __init__(self):
        if VectorEngine._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            VectorEngine._instance = self
            self.initialize_vector_engine()

    def initialize_vector_engine(self):
        print("initializing..")
        # final_articles_path = Path('ethicode/FinalArticles')
        documents = SimpleDirectoryReader("/Users/reaganrazon/Documents/treehacks2024/ethicode24/ethicode/ethicode/FinalArticles").load_data()
        vector_store = IRISVectorStore.from_params(
        connection_string=CONNECTION_STRING,
        table_name="scholarly_review",
        embed_dim=1536, 
    )
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        index = VectorStoreIndex.from_documents(
            documents, 
            storage_context=storage_context, 
            show_progress=True, 
        )
        VectorEngine.query_engine = index.as_query_engine()
        VectorEngine.retriever = index.as_retriever()


from transformers import pipeline
from llama_index.response_synthesizers import (
    get_response_synthesizer,
    BaseSynthesizer,
)
from llama_index.query_engine import CustomQueryEngine
from llama_index.retrievers import BaseRetriever

engine = VectorEngine.get_instance()
retriever = engine.retriever

class RAGQueryEngine(CustomQueryEngine):
    retriever: BaseRetriever
    response_synthesizer: BaseSynthesizer

    def custom_query(self, query_str: str):
        nodes = self.retriever.retrieve(query_str)
        response_obj = self.response_synthesizer.synthesize(query_str, nodes)
        return response_obj

synthesizer = get_response_synthesizer(response_mode="compact")
query_engine3 = RAGQueryEngine(
    retriever=retriever, response_synthesizer=synthesizer
)

def retrieval_query(user_query, engine):
    vector_engine = engine.get_instance()
    response = vector_engine.query_engine.query(user_query)
    return response

def retrieval_query3(user_query,engine):
    vector_engine = engine.get_instance()
    response = vector_engine.query_engine.custom_query(user_query)
    return str(response)

def rag_query(user_query, engine):
    vector_engine = engine.get_instance()
    retrieved_documents = vector_engine.query_engine.query(user_query)
    combined_input = f"{user_query} {retrieved_documents}"
    generator = pipeline('text-generation', model='gpt2')
    generated_response = generator(combined_input, num_return_sequences=1,eos_token_id=50256)[0]['generated_text']
    return generated_response

# REFLEX STARTING!!!

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""

class Query(BaseModel):
    question: str

# Testing database connection
with rx.session() as session:
    engine = VectorEngine.get_instance()
    # result = session.exec(sqlalchemy.text("SELECT text FROM data_scholarly_review"))
    result = session.exec(sqlalchemy.text("SELECT * FROM data_scholarly_review WHERE text LIKE '%ethics%' OR text LIKE '%justice%' OR text LIKE '%CS%'"))
    # text_entry = result.fetchone()
    # if text_entry:
    #     print(text_entry.text)

## CONNECTION FUNCTIONS
        

async def process_with_rag(question):
    response = await retrieval_query(question,engine)
    return response



async def rag_answer(item: Query):
    # Process query with RAG (pseudo-code)
    answer = await process_with_rag(item.question)
    if answer:
        return {"answer": answer}
    else:
        return {"answer": "error", "message": "Invalid credentials"}


app = rx.App(style=styles.base_style)

app.api.add_api_route("/rag-answer", rag_answer, methods=["POST"])
