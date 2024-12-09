from utils import (
    configure_page,
    configure_overview,
    configure_openai_api_key,
    configure_available_options,
    configure_query_input
)

def main() -> None:
    """Main function to run the Streamlit app."""
    configure_page()
    configure_overview()
    configure_openai_api_key()
    model, language, goal, output_format = configure_available_options()
    configure_query_input(model,language, goal, output_format)

if __name__ == "__main__":
    main()