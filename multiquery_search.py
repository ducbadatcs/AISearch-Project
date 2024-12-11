from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.retrievers import TavilySearchAPIRetriever
from dotenv import load_dotenv

from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(".env")
import os 

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-8b"
)

retriever = TavilySearchAPIRetriever(k = 3)

# def ai_summary(docs: list[Document]) -> str:
#     content = ""
#     for doc in docs:
#         content += doc.page_content
    
#     answer = llm.invoke(prompt.invoke({"question": }))
    

def multi_query_search(query: str) -> tuple[list[Document], str]:
    """_summary_

    Args:
        query (str): user query

    Returns:
        tuple[list[Document], str]: Tuple of relevant docs and AI summary.
    """
    retriever_from_llm = MultiQueryRetriever.from_llm(
        retriever=retriever, llm=llm
    )
    
    unique_docs = retriever_from_llm.invoke(query)
    
    content = ""
    for doc in unique_docs:
        content += doc.page_content
        
    prompt =  ChatPromptTemplate.from_messages([
        ("system", """
            You are a helpful assistant. 
            Your task is to help the user summarize information about {question} with the relevant content they provide.
            Your answer will be used with other HTML tags, so please don't include scripts,
            and use headings from H3 to lower.
            
         """),
        ("user", "{content}")
    ]).invoke({"question": query, "content": content}).to_string()
    
    ai_answer = llm.invoke(prompt).content
    for doc in unique_docs:
        print(doc.metadata)

    return (unique_docs, ai_answer)