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