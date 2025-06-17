import google.generativeai as genai  # pip install google-generativeai
import tkinter as tk
from tkinter import scrolledtext

# API Key
api_data = "AIzaSyCKbkPOKz9hqy_N_s3-3T44-umq5lS9qE4"
genai.configure(api_key=api_data)

# Load Gemini model
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# Response generation function
def generate_response(query):
    try:
        response = gemini_model.generate_content(
            query,
            generation_config=genai.GenerationConfig(
                max_output_tokens=75,
                temperature=0.1,
            )
        )
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"

# On Send button click
def send_query():
    query = user_input.get()
    if not query.strip():
        return

    conversation_area.insert(tk.END, f"You: {query}\n", "user")
    user_input.delete(0, tk.END)

    response = generate_response(query)
    conversation_area.insert(tk.END, f"MAHI: {response}\n", "bot")
    conversation_area.see(tk.END)

# Set up main GUI window
root = tk.Tk()
root.title("💬 MAHI Chatbot")
root.configure(bg="#1e1e1e")
root.geometry("550x500")

# Chat area with scrollbar
conversation_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=70,
    height=20,
    font=("Consolas", 12),
    bg="#2e2e2e",
    fg="#f0f0f0",
    insertbackground="white"
)
conversation_area.pack(padx=10, pady=10)
conversation_area.tag_config("user", foreground="#00bfff", font=("Consolas", 12, "bold"))
conversation_area.tag_config("bot", foreground="#7CFC00", font=("Consolas", 12, "bold"))

# Input area
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(pady=10)

user_input = tk.Entry(
    input_frame,
    font=("Consolas", 12),
    width=40,
    bg="#3c3c3c",
    fg="white",
    insertbackground="white",
    borderwidth=2,
    relief=tk.FLAT
)
user_input.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Consolas", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    padx=10,
    pady=5,
    relief=tk.FLAT,
    command=send_query
)
send_button.pack(side=tk.LEFT)

root.mainloop()
