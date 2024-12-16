import pinecone

index = None

def initialize_database(api_key, environment="us-west1-gcp"):
    global index
    pinecone.init(api_key=api_key, environment=environment)
    index = pinecone.Index("pdf-index")

def store_embeddings(chunks, embeddings):
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        index.upsert([(str(i), embedding, {"text": chunk})])

def retrieve_chunks(query_embedding, top_k=5):
    results = index.query(query_embedding, top_k=top_k, include_metadata=True)
    return [result["metadata"]["text"] for result in results["matches"]]
