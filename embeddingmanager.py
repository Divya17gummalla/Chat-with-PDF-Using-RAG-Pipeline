from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    return model.encode(chunks)

def embed_query(query):
    return model.encode([query])[0]