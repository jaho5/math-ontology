# Streamlit SQLite Viewer

A simple Streamlit application that allows you to explore and join SQLite database tables through an intuitive web interface.

## Features

1. **View Database Tables**
   - List all tables in a SQLite database
   - Examine table schemas
   - View table contents

2. **Join Tables**
   - Select tables to join
   - Choose join columns
   - Select join type (INNER, LEFT, RIGHT, FULL OUTER)
   - View results with clear column naming

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd streamlit_sqlite_app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Create a sample database (optional):
   ```
   python sample_data.py
   ```
   This creates a sample database with `customers` and `orders` tables in the `data/` directory.

2. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

3. Open your web browser and navigate to http://localhost:8501

4. Use the sidebar to:
   - Enter the path to your SQLite database
   - Choose between viewing tables or joining tables

## Project Structure

```
streamlit_sqlite_app/
├── app.py                 # Main Streamlit application
├── database.py            # Database connection and query functions
├── sample_data.py         # Script to create sample data
├── requirements.txt       # Dependencies
└── data/                  # Directory for SQLite database files
    └── sample.db          # Sample SQLite database (created by sample_data.py)
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or bug fixes.

## License

[MIT License](LICENSE)
