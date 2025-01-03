# Product Suggestion Generator

This project is a web application that provides AI-powered product suggestions based on user queries. It utilizes a knowledge base stored in a MySQL database and the Groq API to deliver relevant product recommendations. The application is built with Python, Streamlit, and integrates external APIs for enhanced functionality.

## Features

- **AI-powered Suggestions**: Leverages the Groq API with the `llama3-8b-8192` model to generate personalized product recommendations.
- **Dynamic Knowledge Base**: Fetches product information from a MySQL database for contextual responses.
- **Interactive UI**: Built with Streamlit to offer a user-friendly interface for generating product suggestions.

## Prerequisites

- Python 3.8+
- MySQL Database
- `.env` file with the following variables:
  - `GROQ_API_KEY`: Your Groq API key. Sign up for an account at [Groq](https://groq.com/) to obtain an API key.
  - `DB_HOST`: MySQL database host.
  - `DB_USER`: MySQL username.
  - `DB_PASSWORD`: MySQL password.
  - `DB_NAME`: Name of the MySQL database.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/stwins60/ai-demo.git
   cd ai-demo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt --no-cache-dir
   ```

3. Set up the `.env` file with the required environment variables.

4. Ensure the MySQL database is running and accessible.

## Usage

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser (usually `http://localhost:8501`).

3. Input your query in the text box to get AI-powered product suggestions.

## File Structure

```
.
├── app.py                # Main Streamlit application file
├── fetch_knowledge.py    # Utility for fetching knowledge base from the database
├── .env                  # Environment variables file (not included in the repo, must be created)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## How It Works

1. **Fetch Knowledge Base**: The `fetch_knowledge_base()` function retrieves product data from the MySQL database.
2. **AI Integration**: The `ai()` function sends a query to the Groq API, incorporating the product data as context.
3. **Streamlit Interface**: Users interact with the application through a simple form, receiving AI-generated recommendations as text output.

## Environment Setup

Ensure the `.env` file is configured correctly. Below is an example:

```
GROQ_API_KEY=your_groq_api_key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=product_database
```

## Dependencies

- `requests`: For interacting with the Groq API.
- `python-dotenv`: For managing environment variables.
- `mysql-connector-python`: For connecting to the MySQL database.
- `streamlit`: For building the web interface.

Install dependencies with:
```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## Contact

For any inquiries or issues, please open an issue on the GitHub repository or contact the maintainer.
