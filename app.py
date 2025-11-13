from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted  # If available in your environment
import os


# Load environment variables from .env
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Model configuration
MODEL_NAME = "models/gemini-2.5-flash-lite"
model = genai.GenerativeModel(MODEL_NAME)

# Initialize Flask app
app = Flask(__name__)

def chat_with_friend(message):
    """Chat function using Gemini model with 429 handling."""
    try:
        response = model.generate_content(
            [
                {
                    "role": "user",
                    "parts": f"You are a fast, high-IQ AI friend named SingularityAI. {message}"
                }
            ]
        )
        return response.text.strip()
    except Exception as e:
        # Check for 429 error message in exception text if specific exception not available
        if "429" in str(e) or "Resource exhausted" in str(e):
            return "API rate limit exceeded. Please try again in a few minutes."
        return f"Error: {e}"


@app.route('/')
def home():
    """Render chat UI."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat message from frontend."""
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        reply = chat_with_friend(user_message)
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
