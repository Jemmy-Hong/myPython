# promp = "If you tell us who you are, we can personalize the message you see."
# promp += "\nWhat is your first name? "
#
# name = input(promp)
# print("\nHello, " + name + "!")



#while循环
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
