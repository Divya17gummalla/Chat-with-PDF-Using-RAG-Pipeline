from utils.pdf_processor import process_pdf
from utils.embedding_manager import generate_embeddings, embed_query
from utils.vector_database import initialize_database, store_embeddings, retrieve_chunks
from utils.query_handler import generate_response

# Constants
PDF_PATH = "example.pdf"
PINECONE_API_KEY = "your-pinecone-api-key"
OPENAI_API_KEY = "your-openai-api-key"

# Initialize
def main():
    print("Initializing Vector Database...")
    initialize_database(api_key=PINECONE_API_KEY)
    
    print("Processing PDF...")
    text_chunks = process_pdf(PDF_PATH)

    print("Generating Embeddings...")
    embeddings = generate_embeddings(text_chunks)

    print("Storing Embeddings...")
    store_embeddings(text_chunks, embeddings)

    print("Ready to handle queries!")
    while True:
        query = input("\nEnter your question (or 'exit' to quit): ")
        if query.lower() == "exit":
            break

        query_embedding = embed_query(query)
        relevant_chunks = retrieve_chunks(query_embedding)
        response = generate_response(relevant_chunks, query, OPENAI_API_KEY)
        print("\nResponse:\n", response)

if __name__ == "__main__":
    main()
