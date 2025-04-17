import os
import streamlit as st
import torch
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# --- Load environment variables ---
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

# --- Streamlit UI ---
st.set_page_config(page_title="Code Generator", page_icon="💻")
st.title("💻 Code Generator")
dream_text = st.text_input("🗣️ What do you want to code?  ")
if dream_text:
    # Prompt Template
    code_prompt = PromptTemplate(
        input_variables=["user_input"],
        template="""
                You are a coding assistant.
                Your task is to generate the code that meets the requirements.
                
                User requirements:
                {user_input}
                
                
                Make sure to include all necessary imports and dependencies.
                Use the latest version of the libraries and frameworks.
                Provide only the code, with helpful comments.
                """,
    )

    # LLM via OpenRouter (LLaMA-4)
    response = ChatOpenAI(
        openai_api_base="https://openrouter.ai/api/v1",
        model_name="google/gemma-3-27b-it:free",
    )
    chain = code_prompt | response
    # Generate output
    output_msg = chain.invoke({"user_input": dream_text})
    output = output_msg.content

    # Display Moodboard text
    st.markdown("### 🎨 Your Code")
    st.markdown(output)
