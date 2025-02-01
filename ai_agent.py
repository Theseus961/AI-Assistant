from openai import OpenAI
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render!"

# Initialize OpenAI client
client = OpenAI(api_key="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")

# Product data (simplified for now)
products = [
    {"name": "Fit Power Bands Set", "price": "$29.99", "description": "A set of 5 resistance bands with different resistance levels."},
    # Add more products here
]

# Function to handle user queries
def ask_ai(question):
    try:
        response = client.chat_completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI support agent for a fitness product company."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in OpenAI API: {e}")
        return "There was an error processing your request."

# API endpoint for the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get user input from the JSON body
        user_input = request.json.get('message')
        
        # Check if the input is valid
        if not user_input:
            return jsonify({"error": "No message provided"}), 400
        
        # Call the AI function to get a response
        response = ask_ai(user_input)
        
        # Return the response as JSON
        return jsonify({"response": response})
    except Exception as e:
        print(f"Error in /chat endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
