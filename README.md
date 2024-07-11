
# Simple Search Engine

A simple search engine project using Python and Flask.

## Project Structure

```
simple_search_engine/
│
├── app.py
├── indexing.py
├── tfidf.py
├── documents/
│   ├── doc1.txt
│   ├── doc2.txt
│   ├── doc3.txt
│   ├── doc4.txt
│   └── doc5.txt
└── templates/
    ├── index.html
    └── results.html
```

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd simple_search_engine
   ```

2. Install Flask:
   ```bash
   pip install flask
   ```

3. Add your documents in the `documents` directory.

## Running the Application

1. Navigate to the project directory:
   ```bash
   cd simple_search_engine
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000/`.

## Example Queries

- "fox" - Should show `doc1.txt` with a high score.
- "journey" - Should show `doc2.txt` with a high score.
- "galaxy" - Should show `doc3.txt` with a high score.
- "computer science" - Should show `doc4.txt` with a high score.
- "climate change" - Should show `doc5.txt` with a high score.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
