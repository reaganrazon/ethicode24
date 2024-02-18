from llama_index import SimpleDirectoryReader, StorageContext, ServiceContext
from llama_index.indices.vector_store import VectorStoreIndex
from llama_iris import IRISVectorStore
from llama_index.agent import OpenAIAgent
import getpass
import os
from dotenv import load_dotenv
import textwrap

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
        documents = SimpleDirectoryReader("../FinalArticles").load_data()
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
