import openai

def generate_response(chunks, user_query, api_key):
    openai.api_key = api_key
    context = "\n\n".join(chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {user_query}\nAnswer:"
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response["choices"][0]["text"]
