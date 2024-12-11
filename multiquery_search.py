from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.retrievers import TavilySearchAPIRetriever
from env_api import set_api

set_api() # init the API variables

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-8b"
)

retriever = TavilySearchAPIRetriever(k = 5)

def multi_query_search(query: str) -> str:
    return ""