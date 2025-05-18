import json
from langchain_community.document_loaders import JSONLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document  # Use from langchain_core

def ingest_documents():
    # Load the JSON file
    with open('data/keploy_docs/keploy_resources.json', 'r') as f:
        data = json.load(f)

    documents = []

    # Iterate over each section in the JSON
    for category, links in data.items():
        print(f"Category: {category}")

        if isinstance(links, dict):
            for link_name, url in links.items():
                # Create document content
                document_content = f"Category: {category}\n{link_name}: {url}"

                # Add metadata for source tracking
                metadata = {
                    "source": url,
                    "category": category,
                    "title": link_name
                }

                # Create Document with metadata
                document = Document(page_content=document_content, metadata=metadata)
                documents.append(document)
                print(f"  {link_name}: {url}")
        else:
            print("Invalid format: Expected a dictionary of links.")
        print("\n")

    # Embeddings
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Store in vector database with metadata
    vectordb = FAISS.from_documents(documents, embedding)
    vectordb.save_local("keploy_vectordb")  # Save vectorstore locally

# Run ingestion
if __name__ == "__main__":
    ingest_documents()





