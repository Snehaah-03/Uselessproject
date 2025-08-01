import random

replies = [
    "Try saying: 'Your smile activated my neural net 😳'",
    "Confess during lab hours. She can't run away 😎",
    "If she replied to your story, that's basically marriage 💍",
    "Do you believe in love at first sight—or should I upload another photo?",
    "Is your name Google? Because you have everything I'm searching for (and still rejecting).",

]

def generate_reply(user_input):
    return random.choice(replies)
