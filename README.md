# CLI python Calculator

A cmd-line calculator built in Python. This Project demonstrates safe user input handling, error recovery, and automated testing using `pytest`.

## Features

- **Input Validation:** Automatically catches invalid inputs (like typing letters instead of numbers) and prompts the user to try again without crashing.
- **Safe Math:** Handles edge cases like division-by-zero gracefully.
- **Automated Testing:** Includes a full suite of mock-input tests to guarantee reliability.

## Project Structure

```text
my_calculator_project/
├── calculator/            # Main application code
│   ├── __init__.py
│   └── my_math.py         # Calculator logic and input handling
├── tests/                 # Automated test suite
│   └── test_my_math.py
├── setup.sh               # Bash script for easy environment setup
└── requirements.txt       # Project dependencies
```

## Installation & Setup

This project uses a Python virtual environment to manage dependencies. A Bash script is included to make setup instant.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fakelozic/py-calculator.git
   cd py-calculator
   ```
2. **Run the setup script:**
   This will automatically create `.venv` sandbox and install everything from `requirements.txt`.
   ```bash
   bash setup.sh
   ```
3. **Activate the environment:**
   ```bash
   source .venv/bin/activate
   ```
   _(Note for Windows users: run `.venv\Scripts\activate\ instead)_

## Usage

Make sure your virtual environment is activated, then run the main math script:

```bash
python calculator/my_math.py
```

## Running the Tests

This project uses `pytest` to automatically test the math logic and the simulated user inputs.
To run this suite, ensure your virtual environment is activate and run:

```bash
pytest
```
