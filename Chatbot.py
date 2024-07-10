#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

# Define rules for the chatbot with regex
def get_response(user_input):
    # Convert the input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define regex patterns for different types of queries
    patterns = {
        'greeting': re.compile(r'\b(hello|hi|hey|greetings)\b'),
        'farewell': re.compile(r'\b(bye|goodbye|see you|later)\b'),
        'weather': re.compile(r'\b(weather|forecast|rain|sunny|cloudy)\b'),
        'time': re.compile(r'\b(time|clock|hour)\b'),
        'name': re.compile(r'\b(your name|who are you|what are you)\b'),
        'thanks': re.compile(r'\b(thank you|thanks|appreciate)\b')
    }

    # Check for patterns in user input and respond accordingly
    if patterns['greeting'].search(user_input):
        return "Hello! How can I assist you today?"
    elif patterns['farewell'].search(user_input):
        return "Goodbye! Have a great day!"
    elif patterns['weather'].search(user_input):
        return "The weather is sunny today with a high of 25°C."
    elif patterns['time'].search(user_input):
        return "I'm sorry, I can't provide the current time right now."
    elif patterns['name'].search(user_input):
        return "I'm a simple rule-based chatbot."
    elif patterns['thanks'].search(user_input):
        return "You're welcome!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

# Implement the chatbot logic
def chatbot():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()


# In[ ]:




