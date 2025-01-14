
### Support Agent Chatbot
This repository contains a Flask-based application that integrates a pre-built transformer model for question answering. The bot assists with answering questions related to specific customer data platform (CDP) documentation, including Segment, mParticle, Lytics, and Zeotap.

### Requirements
Python 3.7+
Flask
transformers
requests
beautifulsoup4
Installation
Clone the repository:


Copy code
git clone <repository-url>
cd <repository-directory>
Install the required dependencies:


Copy code
pip install -r requirements.txt
You can create the requirements.txt by running:


Copy code
pip freeze > requirements.txt
Ensure you have a working Python environment and install the necessary libraries. You can install the required libraries with:

Copy code
pip install flask transformers requests beautifulsoup4
Usage
Starting the Application
Run the following command to start the Flask application:

Copy code
python app.py
This will start a local server at http://127.0.0.1:5000/.

### Interacting with the Chatbot
The chatbot works via the /ask endpoint, where you can send a POST request with a question related to any of the following platforms:

Segment
mParticle
Lytics
Zeotap
Here’s how you can interact with the API using a POST request with a JSON payload.

### Example Request
Copy code
curl -X POST http://127.0.0.1:5000/ask -H "Content-Type: application/json" -d '{"question": "How do I create a new user in Segment?"}'
Example Response
json
Copy code
{
    "response": "To create a new user in Segment, you would ..."
}
### Home Endpoint
The / route provides a basic message:
Copy code
"CDP Support Agent Chatbot is running. Use the /ask endpoint to interact."

### Functionality
Platform-Specific Assistance: The bot identifies the platform mentioned in the question (e.g., Segment, mParticle) and retrieves relevant documentation for that platform.
Question Answering: The chatbot uses a pre-trained question-answering model (pipeline("question-answering")) to extract answers from the platform’s documentation.
Error Handling: If no relevant documentation is available or if there’s an issue processing the question, appropriate error messages are returned.

### Available Platforms
The supported platforms are:
Segment
mParticle
Lytics
Zeotap

Documentation for these platforms is fetched and indexed from their official sites:
Segment Documentation
mParticle Documentation
Lytics Documentation
Zeotap Documentation
