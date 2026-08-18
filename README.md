# Wapsa - Integrated WhatsApp Personal Assistant

Wapsa is an intelligent WhatsApp assistant that automates routine tasks etc (updating soon :D)

## Getting Started

### Prerequisites
- Python 3.9 or higher
- `uv` package manager
- WhatsApp account

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd wapsa
   ```

2. Install dependencies:
   ```bash
   uv add python-dotenv requests
   ```

3. Configure environment variables:
   Create a `.env` file in the root directory with the following content:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

### Usage
Run the application using `uv`:
```bash
uv run python main.py
```

## Running Tests
To run the built-in tests:
```bash
uv run pytest
```

## Project Structure
```
wapsa/
├── .gitignore       # Git ignore rules
├── .env             # Environment variables (not version controlled)
├── .python-version  # Python version specification
├── README.md        # Project documentation
├── main.py          # Main application entry point
├── pyproject.toml   # Project configuration and dependencies
├── src/
│   └── wapsa/
│       └── __init__.py  # Package initialization
└── uv.lock          # Lock file for dependency versions
```

## License
This project is licensed under the terms of the MIT license.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Contact
For questions or support, please open an issue or contact the maintainers.
