import random
from nltk.stem import PorterStemmer
from data import data  # Make sure this file exists and is structured properly

stemmer = PorterStemmer()

# Mapping intents to responses
INTENT_RESPONSE_MAP = {
    "greetings": "responses",
    "farewell": "farewell_responses",
    "questions": "question_responses",
    "small_talk": "small_talk_responses"
}

def preprocess(sentence):
    # Simpler tokenizer using split() instead of nltk.word_tokenize
    tokens = sentence.lower().split()
    return [stemmer.stem(token) for token in tokens if token.isalnum()]

def get_response(user_input):
    processed_input = preprocess(user_input)
    
    for intent_category, response_category in INTENT_RESPONSE_MAP.items():
        for pattern in data[intent_category]:
            processed_pattern = preprocess(pattern)
            if set(processed_pattern).issubset(set(processed_input)):
                return random.choice(data[response_category])
    
    return "I'm not sure how to respond to that. Could you rephrase it?"

def chat():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
