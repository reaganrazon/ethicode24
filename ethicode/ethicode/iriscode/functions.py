from initialize import VectorEngine
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