print("Hi! I am ChatBot . Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you today?")
    
    elif "your name" in user_input:
        print("Bot: I am ChatBot, your virtual assistant.")

    elif "how are you" in user_input:
        print("Bot: I’m doing great, thank you! How about you?")
    
    elif "weather" in user_input:
        print("Bot: I don’t know the weather right now, but you can check a weather app! ")

    elif "bye" in user_input:
        print("Bot: Goodbye! Have a nice day ")
        break
    
    else:
        print("Bot: Sorry, I don’t understand that. Can you rephrase?")