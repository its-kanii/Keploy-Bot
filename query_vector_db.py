from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# Initialize HuggingFaceEmbeddings with a model name
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def load_vector_store():
    # Load the FAISS vector store from the specified path, allowing dangerous deserialization
    vectordb = FAISS.load_local(r"C:\Users\kanim\Desktop\keploy-rag-bot\keploy_vectordb", 
                               embedding_model, allow_dangerous_deserialization=True)
    return vectordb

# Now you can query the vector store
vectordb = load_vector_store()


def query_vector_db(query: str, vectordb):
    # Generate the embedding for the query
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    query_embedding = embedding.embed_query(query)

    # Perform similarity search in FAISS to get the top 3 most relevant documents
    results = vectordb.similarity_search(query, k=3)
    
    return results

if __name__ == "__main__":
    vectordb = load_vector_store()
    user_query = "What is Keploy?"  # Sample query
    
    results = query_vector_db(user_query, vectordb)
    
    # Print the results
    for result in results:
        print(result.page_content)
