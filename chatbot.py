import google.generativeai as genai
import streamlit as st
import random

# Configure Google Generative AI
GOOGLE_AI_KEY = "AIzaSyAfvKvGN-WqG1goRnfuDMd6blMA-k_lJO4"
genai.configure(api_key=GOOGLE_AI_KEY)

# Model Initiate
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get response from the model and add some emojis
def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    # Add random emojis to the bot's response
    emojis = ['🤖', '😊', '✨', '😎', '👍', '💡']
    bot_response = f"{random.choice(emojis)} {response.text} {random.choice(emojis)}"
    return bot_response

# Streamlit page title
st.set_page_config(page_title="Muskan's Chatbot", page_icon="🤖")

# Custom CSS for styling
st.markdown("""
    <style>
        .chat-bubble-user {
            background-color: #DCF8C6;
            border-radius: 15px;
            padding: 10px;
            margin-bottom: 10px;
            text-align: left;
            max-width: 70%;
            margin-right: auto;
            font-family: Arial, sans-serif;
        }
        .chat-bubble-bot {
            background-color: #F1F0F0;
            border-radius: 15px;
            padding: 10px;
            margin-bottom: 10px;
            text-align: left;
            max-width: 70%;
            margin-right: auto;
            font-family: Arial, sans-serif;
        }
        body {
            background-color: #f0f2f6;
        }
        .chat-input {
            font-family: Arial, sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Chatbot title with emoji
st.title("Muskan's Chatbot 🤖✨")
st.write("Powered By Google Generative AI 😎")

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Display chat history
if st.session_state["history"]:
    for user_text, bot_response in st.session_state["history"]:
        st.markdown(f'<div class="chat-bubble-user">👤 {user_text}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-bubble-bot">🤖 {bot_response}</div>', unsafe_allow_html=True)

# Form to take user input under the chat and with the button on the same line
st.write("### Enter your prompt below:")
with st.form(key="chat-form", clear_on_submit=True):
    cols = st.columns([4, 1])  # Create two columns with widths 4:1
    user_input = cols[0].text_input("", max_chars=2000, placeholder="Ask something... 💬", key="chat-input")
    submit_button = cols[1].form_submit_button("Send 🚀")

# Process new user input and get model response
if submit_button:
    if user_input:
        response = getResponseFromModel(user_input)
        st.session_state.history.append((user_input, response))
        # No need for rerun, Streamlit automatically updates the UI after appending history
    else:
        st.warning("Please enter a prompt! ⚠️")
