from openai import OpenAI
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
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

# API endpoint for the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    response = ask_ai(user_input)
    return jsonify({"response": response})

# Root endpoint to check if the app is running
@app.route('/')
def home():
    return "AI Support Agent is running!"

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
