import re
import random

# Dictionary mapping patterns to possible responses
responses = {
    r"(hello|hi|hey)": ["Hi there! How can I assist you today?", "Hey! What's up?", "Hello! Need any help?"],
    r"how (are|r) you": ["I'm just a bot, but I'm doing great! How about you?", "I'm fine! Thanks for asking."],
    r"what('s| is) your name": ["I'm a chatbot!", "You can call me RishitsBot!"],
    r"(help|assist)": ["Sure, I'm here to help. What do you need assistance with?", "I'm happy to assist! What do you need?"],
    r"(bye|goodbye|see you)": ["Goodbye! Have a great day!", "See you later! Take care."],
    r"(thank you|thanks)": ["You're welcome! I'm happy to help.", "No problem! Always here for you."],
    r"(weather|forecast)": ["I can't check the weather yet, but you can look it up on Google!-https://search.brave.com/search?q=google+weather&source=desktop", 
        "Try asking Google for the latest weather updates.-https://search.brave.com/search?q=google+weather&source=desktop"],
    r"(time|clock)": ["I don't have a watch, but you can check the current time on your device.", "I wish I had a clock, but I don't! Check your phone or computer."],
    r"(joke|funny|laugh)": ["Why don't skeletons fight each other? Because they don't have the guts! 😂", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "default": ["I'm not sure I understand. Could you rephrase?", "Hmm, that’s tricky. Can you try rewording?", "I don't get it. Could you explain differently?"]
}

# Function to find the appropriate response
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    for pattern, response_list in responses.items():
        if re.search(pattern, user_input):
            return random.choice(response_list)  # Pick a random response
    
    return random.choice(responses["default"])

# Chatbot function that interacts with the user
def chatbot():
    print("Chatbot: Hello! I'm here to assist you. (Type 'bye' to exit)")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_input)
        
        # If chatbot doesn't understand, allow the user to teach it
        if response in responses["default"]:
            print("Chatbot: I don’t know how to respond. Can you teach me?")
            new_response = input("Type a response I should use next time: ")
            responses[user_input] = [new_response]  # Save new response
            print("Chatbot: Got it! I'll remember that.")
        
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
