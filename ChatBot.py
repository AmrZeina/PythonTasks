# A simple chat Bot

data_base = {
    "hello": "Hi, how are you today?",
    "how are you": "I'm good, thanks",
    "bye": "Goodbye",
    "what is your name": "my name is robot"
}

name = None
print("Hello, what is your name?")
while True:
    user_input = input("user: ")

    if name is None:                               # Store name
        name = user_input
        print(f"Bot: Nice to meet you, {name}!")
        print("Write any two numebrs to add or subtract them if you want")
        continue

                                                                                                     
    if user_input == "bye":                         # Exit
        print(f"Bot: Bye {name}!")
        break


    if "+" in user_input:                           # Addition
        nums = [int(n) for n in user_input.split("+")]
        print("Bot:", sum(nums))
        continue

    if "-" in user_input:                           # Subtraction
        nums = [int(n) for n in user_input.split("-")]
        print("Bot:", nums[0] - nums[1])
        continue

    if user_input in data_base:                     # From data base
        print("Bot:", data_base[user_input])
    else:
        print("Bot: I don't know that.")
