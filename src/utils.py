import streamlit as st
import os
import openai


AVAILABLE_MODELS = [
    {"id": "gpt-4o-mini", "description": "Cost-effective GPT-4 variant"},
    {"id": "gpt-4", "description": "High-quality, general-purpose model"},
    {"id": "gpt-3.5-turbo", "description": "Fast, cost-effective coding assistant"}, 
]

def generate_openai_response(api_key: str, query: str, language: str, goal: str, output_format: str,model: str = "gpt-3.5-turbo") -> str:
    """Generate a response from OpenAI API based on user inputs."""
    openai.api_key = api_key

    prompt = (
        f"Language: {language}\n"
        f"Goal: {goal}\n"
        f"Query: {query}\n"
        f"Output Format: {output_format}\n"
        "Provide the output:"
    )

    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": (
                    "You are a coding assistant specialized in Python, R, and SQL. "
                    "Always follow the user's instructions carefully and consider the options they provide: "
                    "Language, Goal, Query, and Output Format. "
                    "Ensure the output aligns with these options and is tailored to the specified coding task. "
                    "Be concise, accurate, and explain clearly if the Output Format requires it."
                )},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except openai.OpenAIError as e:
        return f"Error communicating with OpenAI API: {str(e)}"

def configure_page() -> None:
    """Configure page settings like title, layout, and favicon."""
    st.set_page_config(
        page_title="Coding Assistant Dashboard",
        page_icon="🤖",
        layout="wide"  # Wide layout for better spacing
    )

def configure_overview() -> None:
    """Display the overview section of the app."""
    st.title("Coding Assistant Dashboard")
    st.write("Welcome! This dashboard helps you with Python, R, and SQL tasks.")
    st.write("Select your preferences and let the assistant guide you!")



def configure_openai_api_key() -> None:
    """Add a section for the user to input their OpenAI API key and select a model in the sidebar."""
    st.sidebar.subheader("API Configuration")
    st.sidebar.write("Please enter your OpenAI API key to enable AI-powered features.")

    # Input for the API key
    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

    if openai_api_key:
        st.session_state["openai_api_key"] = openai_api_key
        st.sidebar.success("API key set for this session.")
    else:
        st.sidebar.warning("Please enter your OpenAI API key.")
        


def configure_available_options() -> None:
    """Add interactive elements like language selection and goals to the sidebar."""
    st.sidebar.subheader("Configure Your Task")
    
    # Extract model IDs for the dropdown menu
    model_choices = [f"{model['id']} - {model['description']}" for model in AVAILABLE_MODELS]
    
    model = st.sidebar.selectbox("Choose an OpenAI model - default is gpt-3.5-turbo",model_choices)
    model_id = model.split(" - ")[0]
    language = st.sidebar.selectbox("Choose a language:", ["Python", "R", "SQL"])
    goal = st.sidebar.selectbox("What is your goal?", ["Explain", "Evaluate", "Optimize", "Basic Questions"])
    output_format = st.sidebar.radio("Output format:", ["Plain Code", "Brief Explanation", "Line-by-Line Explanation"])
    
    # Return the selected values
    return model_id, language, goal, output_format

def configure_query_input(model: str ,language: str, goal: str, output_format: str) -> None:
    """Display the query input box on the main page and generate a response."""
    st.subheader("Enter Your Task")
    query = st.text_area(
        "Describe your coding task or question:",
        placeholder="E.g., Write a Python function for calculating Fibonacci numbers.",
        height=300  # Adjust height for better usability
    )

    # Ensure API key is available before allowing submission
    if "openai_api_key" not in st.session_state or not st.session_state["openai_api_key"]:
        st.warning("Please configure your OpenAI API key before submitting a task.")
    elif st.button("Submit"):
        api_key = st.session_state["openai_api_key"]
        response = generate_openai_response(api_key= api_key, query=query, language=language, goal=goal, output_format=output_format,model=model)
        st.subheader("Generated Response")
        st.code(response, language.lower())