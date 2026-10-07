import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (aim for at least 12 characters).")

    # Character variety checks
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

    # Common weak patterns
    common_patterns = ["password", "123456", "qwerty", "letmein", "admin"]
    if password.lower() in common_patterns:
        score = 0
        feedback = ["This is a commonly used password — easily guessed."]

    # Map score to a strength label
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score, feedback


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    strength, score, feedback = check_password_strength(pwd)

    print(f"\nStrength: {strength} (score: {score}/6)")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f" - {tip}")
    else:
        print("Great password!")
