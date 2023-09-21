import os

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_BASE"] = "https://openai-ppcazure017.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "c3417acc5c654125b0b74cffeea8b491"
os.environ["OPENAI_API_VERSION"] = "2022-12-01"


import getpass

os.environ["33042089-5dfd-4477-a281-b43a0ea34ef9"] = getpass.getpass("Pinecone API Key:")

os.environ["gcp-starter"] = getpass.getpass("Pinecone Environment:")

os.environ["c3417acc5c654125b0b74cffeea8b491"] = getpass.getpass("OpenAI API Key:")

from langchain.embeddings import OpenAIEmbeddings


from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import UnstructuredExcelLoader

loader = UnstructuredExcelLoader("data.xlsx", mode="elements")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)
# res = []
# for i  in docs:
#     res.append(str(i))

# embeddings = OpenAIEmbeddings(deployment="text-embedding-ada-002")
# # doc_result = embeddings.embed_documents(docs)
# result = []
# for row in res:
#     result.append(embeddings.embed_query(row))

import pinecone

# initialize pinecone
pinecone.init(
    api_key=os.getenv("33042089-5dfd-4477-a281-b43a0ea34ef9"),  # find at app.pinecone.io
    environment=os.getenv("gcp-starter"),  # next to api key in console
)

index_name = "langchain-demo"


# The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

# if you already have an index, you can load it like this
# docsearch = Pinecone.from_existing_index(index_name, embeddings)

# query = "What did the president say about Ketanji Brown Jackson"
# docs = docsearch.similarity_search(query)


