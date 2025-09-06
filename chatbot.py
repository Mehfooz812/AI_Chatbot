import datetime
import random

print("🤖 Chatbot: Hi! I am your AI chatbot. Type 'bye' to exit.")

# Some responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "All good here. What about you?"],
    "name": ["I'm your chatbot assistant.", "You can call me ChatBuddy!"],
    "time": [f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"],
    "date": [f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"]
}

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("🤖 Chatbot: Bye! Have a nice day 👋")
        break

    found = False
    for key in responses:
        if key in user_input:
            print("🤖 Chatbot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("🤖 Chatbot: Sorry, I didn't understand that.")
