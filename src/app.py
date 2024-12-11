from utils import (
    configure_page,
    configure_overview,
    configure_openai_api_key,
    configure_available_options,
    configure_chat,
    configure_clear_history,
    add_custom_styles
)

def main() -> None:
    """Main function to run the Streamlit app."""
    configure_page()
    add_custom_styles()
    configure_overview()
    configure_openai_api_key()
    model, language, goal, output_format = configure_available_options()
    configure_clear_history()
    configure_chat(model,language, goal, output_format)

if __name__ == "__main__":
    main()