import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import(
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# Custom CSS Styling
st.markdown("""
<style>
            /* Existing Styles */
            .main {
                background-color: #1a1a1a;
                color: #ffffff;
            }
            .sidebar .sidebar-content{
                background-color: #2d2d2d;
            } 
            .stTextInput textarea{
                color: #ffffff !important;
            }

            /*Add new styles for the select box*/
            st.Selectbox div[data-baseweb="select"]{
                color: white !important;
                background-color: #3d3d3d !imporant;
            }
            st.Selectbox svg {
                fill: white !important;
            }
            st.Selectbox option {
                color: white !important;
                background-color: #2d2d2d !imporant;
            }
            /*drop down menu items*/
            div[role="listbox"] div {
                color: white !important;
                background-color: #2d2d2d !imporant;
            }
</style>
""", unsafe_allow_html=True)
st.title("Deepseek Code Pair Programmer")
st.caption("AI Pair Programmer with Debugging Support")

# Sidebar configuration
with st.sidebar:
    st.header("Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b"],
        index=0
    )

    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("""
    - Python Expert
    - Debugging Assistant
    - Code Documentation
    - Solution Design          
    """)

    st.divider()
    st.markdown("Built with Ollama and Langchain")

    # initiate chat engine

llm_engine=ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.2,
)

system_prompt = SystemMessagePromptTemplate.from_template(
    "Your are an expert AI coding assistant. Please provide concise and correct solutions."
    "with intermedia print statements for debugging."
)

if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm Deepseek. How can I help you code?"}]

chat_container=st.container() 

# display chat messages  
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_query = st.chat_input("Type your coding question here...")

def generate_ai_response(prompt_chain):
    processing_pipeline=prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})     

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))

    return ChatPromptTemplate.from_messages(prompt_sequence)


if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})

    with st.spinner("Processing..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)

    st.session_state.message_log.append({"role":"ai", "content": ai_response})

    st.rerun()