# Coding Help Dashboard

## Overview

The **Coding Help Dashboard** is a user-friendly assistant designed to help with coding tasks in **Python**, **R**, and **SQL**. Built with Streamlit, this interactive app allows users to:

- Select a programming language.
- Define specific goals like explaining, evaluating, or optimizing code.
- Choose output formats, such as plain code or detailed explanations.

This tool is ideal for beginners seeking guidance or professionals streamlining routine tasks.

---

## Features

- **Language Support**: Python, R, and SQL.
- **Customizable Goals**: Explain, Evaluate, Optimize, or answer basic questions.
- **Interactive Output**: Select output formats like plain code or line-by-line explanation.
- **Powered by OpenAI**: Generate high-quality responses using OpenAI models like GPT-4 or GPT-3.5.

---

## Project Structure

```
coding_help_dashboard/
├── code_agents_venc/  # Virtual environment (excluded from the repository)
├── src/               # Source code for the app
│   ├── app.py         # Main Streamlit app script
│   └── utils.py       # Helper functions and utilities
├── tests/             # Unit tests for the project
├── requirements.txt   # List of dependencies
├── README.md          # Project overview and instructions
└── .gitignore         # Ignored files and directories
```

---

## Installation and Setup

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.8 or later installed on your system.
- An OpenAI API key (you can get it from [OpenAI](https://platform.openai.com/account/api-keys)).

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MRB-2020/coding_help_dashboard.git
   cd coding_help_dashboard
   ```

2. **Set Up the Virtual Environment**:
   ```bash
   python -m venv code_agents_venc
   source code_agents_venc/bin/activate  # For Linux/Mac
   code_agents_venc\\Scripts\\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up OpenAI API Key**:
   - Add your OpenAI API key in the app when prompted, or save it in a `.openai_key` file in the project directory:
     ```bash
     echo "your_openai_api_key" > .openai_key
     ```

5. **Run the Application**:
   ```bash
   streamlit run src/app.py
   ```

---

## Usage Instructions

1. Open the Streamlit app in your browser (usually at `http://localhost:8501`).
2. Enter your OpenAI API key in the sidebar.
3. Choose your programming language, goal, and output format.
4. Input your coding query in the text box and submit.
5. Review the generated output.

---

## Contributing

Contributions are welcome! Feel free to:
- Fork this repository.
- Create a new branch (`git checkout -b feature-name`).
- Make your changes and test them.
- Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Marcio Bernardo**  
- GitHub: [MRB-2020](https://github.com/MRB-2020)  
- Email: marciobernardo1@gmail.com  

---

## Acknowledgments

- Thanks to [Streamlit](https://streamlit.io/) for the interactive web app framework.
- Powered by [OpenAI](https://openai.com/) models.
"""