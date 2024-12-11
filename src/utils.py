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
    st.sidebar.subheader("Configure Your Preference")
    
    # Extract model IDs for the dropdown menu
    model_choices = [f"{model['id']} - {model['description']}" for model in AVAILABLE_MODELS]
    
    model = st.sidebar.selectbox("Choose an OpenAI model - default is gpt-3.5-turbo",model_choices)
    model_id = model.split(" - ")[0]
    language = st.sidebar.selectbox("Choose a language:", ["Python", "R", "SQL"])
    goal = st.sidebar.selectbox("What is your goal?", ["Explain", "Evaluate", "Optimize", "Basic Questions"])
    output_format = st.sidebar.radio("Output format:", ["Plain Code", "Brief Explanation", "Line-by-Line Explanation"])
    
    # Return the selected values
    return model_id, language, goal, output_format

def configure_clear_history():
    """Clear the chat history."""
    
    # Input for the Clear history key
    clear_history = st.sidebar.button("Clear Chat History")
    if clear_history:
        st.session_state["chat_history"] = []

        
def configure_chat(model: str, language: str, goal: str, output_format: str) -> None:
    """Interactive chat interface using st.chat_message."""
    st.subheader("Chat with Coding Assistant")

    # Check if chat history exists in the session state
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []  # Initialize chat history

    # Display existing chat messages
    for message in st.session_state["chat_history"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get user input from the chat input box
    if prompt := st.chat_input("Describe your coding task or question:"):
        # Add user message to chat history
        st.session_state["chat_history"].append({"role": "user", "content": prompt})

        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using OpenAI
        if "openai_api_key" in st.session_state and st.session_state["openai_api_key"]:
            api_key = st.session_state["openai_api_key"]
            response = generate_openai_response(
                api_key=api_key,
                query=prompt,
                language=language,
                goal=goal,
                output_format=output_format,
                model=model,
            )
            
            # Add assistant response to chat history
            st.session_state["chat_history"].append({"role": "assistant", "content": response})

            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(response)
        else:
            # Warn the user if API key is missing
            with st.chat_message("assistant"):
                st.markdown("Please configure your OpenAI API key in the sidebar.")
                
                
def add_custom_styles(sidebar_color="#4682B4", main_area_color="#D3D3D3"):
    """Add custom styles to Streamlit app with dynamic colors."""
    st.markdown(
        f"""
        <style>
        /* Sidebar */
        .css-1d391kg {{
            background-color: {sidebar_color};
        }}
        /* Main content area */
        .css-18e3th9 {{
            background-color: {main_area_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    