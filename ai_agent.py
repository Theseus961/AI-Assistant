from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="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")

# Product data (simplified for now)
products = [
    {"name": "Fit Power Bands Set", "price": "$29.99", "description": "A set of 5 resistance bands with different resistance levels."},
    # Add more products here
]

# Function to handle user queries
def ask_ai(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI support agent for a fitness product company."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# Test the AI
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = ask_ai(user_input)
    print("AI: ", response)