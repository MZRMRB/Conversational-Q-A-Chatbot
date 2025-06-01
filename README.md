# Gemini Chatbot

A simple chatbot application using Google's Gemini API and Streamlit.

## Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. **Create a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
- Create a `.env` file in the root directory
- Add your Gemini API key:
```
GEMINI_API_KEY=your-api-key-here
```

## Running the Application

1. **Activate the virtual environment** (if not already activated)
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

2. **Run the Streamlit app**
```bash
streamlit run app.py
```

## Features

- Real-time chat interface
- Persistent chat history
- Powered by Google's Gemini AI
- Clean and modern UI

## Project Structure

```
├── app.py              # Main Streamlit application
├── backend.py          # Gemini API integration
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (ignored by git)
├── .gitignore         # Git ignore rules
└── README.md          # Documentation
```

## Notes

- Make sure to keep your API key secure and never commit it to version control
- The `.env` file should be added to `.gitignore 