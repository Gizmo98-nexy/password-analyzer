# Password Analyzer

A Python-based password analysis tool that evaluates password strength through multiple lenses: rule-based complexity, mathematical entropy, and historical breach data.

This project is broken down into four progressive scripts, demonstrating how to build a robust password checker from scratch.

## Scripts Included

1. **`script1pass.anal.py`**: Basic rule-based password strength checking (length, character variety, common weak passwords).
2. **`script2entropy.py`**: Introduces mathematical entropy calculation to determine how many bits of randomness a password contains.
3. **`script3.py`**: Integrates the HaveIBeenPwned API to check if a password has appeared in known data breaches using k-Anonymity (SHA-1 hashing).
4. **`script4..CLI.py`**: The final, fully-featured Command Line Interface tool that combines all previous concepts with `argparse` for flags like `--no-breach-check` and `--show`.

## Installation

1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can run the final CLI tool directly:

```bash
python script4..CLI.py
```

### Options

- `--show`: Displays the password as you type it instead of hiding the input.
- `--no-breach-check`: Skips the online HaveIBeenPwned API check (useful if you are offline).

Example:
```bash
python script4..CLI.py --show --no-breach-check
```
