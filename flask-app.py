from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define pairs of patterns and responses for the chatbot
pairs = [
    # Greetings
    ["hi|hello", ["Hello!", "Hi there!", "Hey!"]],
    ["howdy", ["Howdy, partner!", "Howdy! How can I assist you today?"]],
    ["good morning", ["Good morning!", "Morning! How's it going?"]],
    ["good evening", ["Good evening! How can I help you tonight?"]],
    ["bye", ["Goodbye!", "See you later!", "Bye! Have a great day!"]],
    ["exit", ["Goodbye! Come back soon!", "Bye! Take care!"]],
    ["i am fine",["good, how i assit you today"]],
    ["good",["thank you, have you any other queries"]],

    # Asking About the Bot
    ["what is your name?", ["I'm a chatbot.", "I am an AI assistant."]],
    ["who are you?", ["I am your friendly chatbot.", "I am just a simple AI bot."]],
    ["what can you do?", ["I can chat with you!", "I can answer your questions and assist you with various tasks."]],
    
    # Asking About Well-being
    ["how are you?", ["I'm good, how about you?", "I'm just a bot, but I'm fine!"]],
    ["what's up?", ["Not much, just here to help you!", "Just hanging out, waiting to assist you."]],
    
    # Responding to Politeness
    ["thank you", ["You're welcome!", "Glad I could help!"]],
    ["thanks", ["You're welcome!", "Anytime!"]],
    ["please", ["Yes, of course!", "Sure, I got you!"]],
    
    # Miscellaneous Questions
    ["how old are you?", ["I don't have an age like humans, but I'm quite young!"]],
    ["where are you from?", ["I exist in the cloud, so I don't have a physical location."]],
    ["what is your favorite color?", ["I don't have preferences, but I think blue is nice!"]],
    ["what is the meaning of life?", ["The meaning of life is to live it to the fullest!"]],
    
    # Fun and Random Responses
    ["tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!", "Why don’t oysters donate to charity? Because they are shellfish!"]],
    ["make me laugh", ["Why did the computer go to the doctor? It had a virus!", "Why don’t eggs tell jokes? They might crack up!"]],
    
    # Questions Related to Time
    ["what time is it?", ["I'm not sure about the exact time, but you can check your device.", "Sorry, I don't have access to the time."]],
    ["what is the date today?", ["I can't check the date, but you can look at the bottom of your screen!"]],
    
    # Personal Queries
    ["what is your favorite movie?", ["I don't watch movies, but I hear 'Inception' is a great one!"]],
    ["do you like music?", ["I don't have ears, but I imagine music is wonderful!", "I can't listen to music, but I can help you find songs!"]],
    
    # Compliments
    ["you're awesome", ["Thank you! You're awesome too!", "I appreciate that!"]],
    ["you're cool", ["Thanks! You're pretty cool yourself!"]],
    
    # Simple General Queries
    ["what is AI?", ["AI stands for Artificial Intelligence. It's the simulation of human intelligence in machines."]],
    ["what is machine learning?", ["Machine learning is a subset of AI where computers learn from data to make predictions."]],
    ["what is Python?", ["Python is a high-level programming language used for web development, data science, and more."]],
    
    # Asking for Help
    ["can you help me?", ["Of course! What do you need help with?", "Yes! What can I do for you?"]],
    ["i need assistance", ["Sure! How can I assist you?", "I’m here to help! What do you need assistance with?"]],
    
    # Asking for the Weather (you can integrate with an API if needed)
    ["what's the weather like?", ["I'm not sure about the weather, but you can check it online or use a weather app."]],
    ["is it going to rain today?", ["I can't check, but you can use your phone or check a weather website."]]
]


# Create a Chat object
chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json["user_input"]
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)