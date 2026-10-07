import re
import math
import hashlib
import argparse
import getpass

import requests


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (aim for at least 12 characters).")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    else:
        feedback.append("Add special characters (e.g. !@#$%).")

    common_patterns = ["password", "123456", "qwerty", "letmein", "admin"]
    if password.lower() in common_patterns:
        score = 0
        feedback = ["This is a commonly used password — easily guessed."]

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score, feedback


def calculate_entropy(password):
    pool_size = 0

    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'[0-9]', password):
        pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        pool_size += 32

    if pool_size == 0:
        return 0

    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)


def entropy_rating(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Reasonable"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"


def check_pwned(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        return None

    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return int(count)

    return 0


def analyze_password(password, skip_breach_check=False):
    strength, score, feedback = check_password_strength(password)
    entropy = calculate_entropy(password)
    entropy_label = entropy_rating(entropy)

    print(f"\nRule-based strength: {strength} (score: {score}/6)")
    print(f"Entropy: {entropy} bits — {entropy_label}")

    if not skip_breach_check:
        print("\nChecking against known data breaches...")
        pwned_count = check_pwned(password)

        if pwned_count is None:
            print("Could not reach breach-check service — skipping this check.")
        elif pwned_count > 0:
            print(f"⚠️  This password has appeared in {pwned_count:,} known data breaches. Avoid using it.")
        else:
            print("✓ This password was not found in any known breach.")

    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print(f" - {tip}")
    else:
        print("\nGreat password!")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze password strength, entropy, and breach history."
    )
    parser.add_argument(
        "--no-breach-check",
        action="store_true",
        help="Skip the online HaveIBeenPwned breach check (useful if offline)."
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Show the password as you type it instead of hiding it."
    )

    args = parser.parse_args()

    if args.show:
        password = input("Enter a password to check: ")
    else:
        password = getpass.getpass("Enter a password to check (hidden): ")

    if not password:
        print("No password entered. Exiting.")
        return

    analyze_password(password, skip_breach_check=args.no_breach_check)


if __name__ == "__main__":
    main()