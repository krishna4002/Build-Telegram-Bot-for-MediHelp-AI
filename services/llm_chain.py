import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
vectorstore = PineconeVectorStore(
    index_name=PINECONE_INDEX_NAME,
    embedding=embedding_model,
    namespace="medibot",
    pinecone_api_key=PINECONE_API_KEY
)

custom_prompt_template = """
Use the pieces of information provided in the context to answer the user's question.
Provide a detailed and comprehensive response, explaining concepts thoroughly.
If you don't know the answer, just say that you don't know. Don't make up an answer.
Only provide information from the given context.

Context: {context}
Question: {question}

Start the answer directly and ensure it is well-explained and sufficiently detailed.
"""

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.3",
        temperature=0.5,
        top_p=0.5,
        repetition_penalty=1.0,
        model_kwargs={"token": HF_TOKEN, "max_length": "1024"},
        task="text-generation"
    ),
    retriever=vectorstore.as_retriever(search_kwargs={'k': 1}),
    return_source_documents=True,
    combine_docs_chain_kwargs={'prompt': PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])}
)

def get_qa_chain():
    return qa_chain
