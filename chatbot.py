"""
AI Chatbot - Rule Based
Author: Mehfooz
Year: 2025

How to run:
    python chatbot.py
"""

import random
from datetime import datetime

GREETINGS = ["Hello!", "Hi there!", "Hey!", "Hi! How can I help?"]
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
    "Why did the developer go broke? Because he used up all his cache!"
]

def get_time() -> str:
    """Return current time as HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")

def get_date() -> str:
    """Return today's date in readable format (e.g., 06 September 2025)."""
    return datetime.now().strftime("%d %B %Y")

def simple_calc(expr: str) -> str:
    """
    Very small safe-ish calculator:
    - Allows digits, + - * / . () and spaces.
    - Evaluates the expression using eval after a simple whitelist check.
    Note: This is for learning/demo only.
    """
    try:
        allowed = set("0123456789+-*/(). ")
        if not expr:
            return "No expression given."
        if any(ch not in allowed for ch in expr):
            return "Invalid characters in expression."
        # Evaluate expression (basic). In production, use a proper parser.
        result = eval(expr)
        return str(result)
    except Exception:
        return "Couldn't calculate that."

def respond(text: str) -> str:
    """
    Return a response string based on simple rule checks in the input text.
    Supports greetings, time, date, jokes, small calculations and help/exit commands.
    """
    text = text.lower().strip()

    # greetings
    if any(g in text for g in ["hi", "hello", "hey"]):
        return random.choice(GREETINGS)

    # time & date
    if "time" in text:
        return "Current time is " + get_time()
    if "date" in text:
        return "Today's date is " + get_date()

    # jokes
    if "joke" in text:
        return random.choice(JOKES)

    # calculator: "calc 2+3" or "calculate 2+3"
    if text.startswith("calc ") or text.startswith("calculate "):
        expr = text.split(" ", 1)[1]
        return "Result: " + simple_calc(expr)

    # help
    if "help" in text:
        return "Commands: time, date, joke, calc <expression>, bye"

    # exit
    if text in ["bye", "exit", "quit", "goodbye"]:
        return "Bye! Take care 👋"

    # fallback
    return "Sorry, I didn't understand. Type 'help' for commands."

def main() -> None:
    """Main loop: read user input and print bot responses until user exits."""
    print("🤖 AI Chatbot — type 'help' for commands, 'bye' to exit.")
    try:
        while True:
            user = input("You: ").strip()
            if not user:
                continue
            reply = respond(user)
            print("Bot:", reply)
            if user.lower() in ["bye", "exit", "quit", "goodbye"]:
                break
    except KeyboardInterrupt:
        print("\nBot: Bye! (keyboard interrupt)")

if _name_ == "_main_":
    main()
