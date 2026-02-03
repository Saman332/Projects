import openai

# Set your API key
openai.api_key = "YOUR_API_KEY"

SYSTEM_PROMPT = """
You are an intelligent educational chatbot.
You help students learn Python and LLMs.
Explain concepts clearly with examples.
"""

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def chatbot(user_input):
    conversation_history.append(
        {"role": "user", "content": user_input}
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        temperature=0.5
    )

    reply = response["choices"][0]["message"]["content"]

    conversation_history.append(
        {"role": "assistant", "content": reply}
    )

    return reply


print("🤖 Chatbot running (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    print("Chatbot:", chatbot(user_input))
