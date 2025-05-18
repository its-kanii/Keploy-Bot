import os
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage


os.environ["GROQ_API_KEY"] = "your groq api"
# Step 1: Load Embedding Model (same one used during ingestion)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: Load FAISS Vector Store
vector_store_path = r"C:\Users\kanim\Desktop\keploy-rag-bot\keploy_vectordb"
vectordb = FAISS.load_local(vector_store_path, embedding_model, allow_dangerous_deserialization=True)

# Step 3: Initialize Groq Chat Model with LLaMA3
llm = ChatGroq(
    model="llama3-8b-8192",  # Use "llama3-70b-8192" if needed
    temperature=0.1
)

# Step 4: Setup Retrieval QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

# Step 5: Query loop
def main():
    print("Welcome to Keploy RAG Bot (Powered by LLaMA3 on Groq)")
    while True:
        query = input("\nAsk a question (or type 'exit' to quit): ")
        if query.lower() in ['exit', 'quit']:
            break

        result = qa_chain.invoke(query)
        print("\nAnswer:\n", result["result"])

        print("\nSources:")
        for doc in result["source_documents"]:
            print(f"- {doc.metadata.get('source', 'Unknown')}")


if __name__ == "__main__":
    main()
