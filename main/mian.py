
def chatbot():

    print("=" * 40)
    print("🤖 Welcome to the Basic Chatbot!")
    print("Type 'bye' to exit.")
    print("=" * 40)

    while True:

        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "hi":
            print("Bot: Hello!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")

        elif user == "who made you":
            print("Bot: I was created using Python.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")
chatbot()
