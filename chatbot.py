def chatbot():
    print("Chatbot: Hi! I am your simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # .lower() cap small 

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi!")
        
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How about you?")
        
        elif user_input == "what is your name":
            print("Chatbot: I am a simple rule-based chatbot created in Python.")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break  # loop close
        
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Function ko call karo
chatbot()