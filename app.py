from flask import Flask, request, jsonify, render_template
import spacy
from knowledge_base import faq_knowledge_base, intent_keywords, intent_responses

# Initialize Flask app and SpaCy
app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

def detect_intent(user_input):
    """Detects the user's intent based on keywords."""
    doc = nlp(user_input.lower())
    for token in doc:
        for intent, keywords in intent_keywords.items():
            if token.lemma_ in keywords:
                return intent
    return "unknown"

def analyze_question(user_input):
    """Analyzes the user input for intents, keywords, and knowledge base matching."""
    # Detect intent
    intent = detect_intent(user_input)
    
    if intent in intent_responses:
        return intent_responses[intent]

    # Extract keywords from user input
    doc = nlp(user_input.lower())
    keywords = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

    # Search the knowledge base for matching keywords
    for keyword in keywords:
        if keyword in faq_knowledge_base:
            return faq_knowledge_base[keyword]

    # Default response if no match found
    return "I'm sorry, I couldn't find information on that topic. Please try asking differently."

@app.route("/")
def index():
    return render_template("index.html")  # Serve the HTML page

@app.route("/get_response", methods=["POST"])
def get_response():
    if request.content_type != "application/json":
        return jsonify({"error": "Unsupported Media Type. Use Content-Type: application/json"}), 415

    user_input = request.json.get("user_input")
    if not user_input:
        return jsonify({"error": "No user input provided"}), 400

    try:
        bot_response = analyze_question(user_input)
        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
