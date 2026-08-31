import re


# Common passwords
COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "welcome",
    "letmein",
    "iloveyou",
    "abc123",
    "india123",
    "hello@123" 
}


def analyze_password(password):

    score = 0
    suggestions = []

    # -----------------------------
    # LENGTH CHECK
    # -----------------------------

    if len(password) >= 8:
        score += 10
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 15
    else:
        suggestions.append("Use at least 12 characters for better security.")

    if len(password) >= 16:
        score += 15

    if len(password) >= 20:
        score += 10

    # -----------------------------
    # CHARACTER CHECKS
    # -----------------------------

    if re.search(r"[a-z]", password):
        score += 10
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 10
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 10
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        suggestions.append(
            "Add special characters such as @, #, $, !."
        )

    # -----------------------------
    # REPEATED CHARACTERS
    # -----------------------------

    if re.search(r"(.)\1\1", password):
        score -= 10
        suggestions.append(
            "Avoid repeating the same character multiple times."
        )

    # -----------------------------
    # COMMON PASSWORD CHECK
    # -----------------------------

    if password.lower() in COMMON_PASSWORDS:
        score -= 50
        suggestions.append(
            "This is a commonly used password."
        )

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    # -----------------------------
    # STRENGTH LEVEL
    # -----------------------------

    if score < 25:
        strength = "VERY WEAK"

    elif score < 45:
        strength = "WEAK"

    elif score < 65:
        strength = "MEDIUM"

    elif score < 85:
        strength = "STRONG"

    else:
        strength = "VERY STRONG"

    return score, strength, suggestions


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    print("\n" + "=" * 45)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    # Ask for password
    password = input("Enter your password: ")

    # Analyze password
    score, strength, suggestions = analyze_password(password)

    # -----------------------------
    # DISPLAY RESULT
    # -----------------------------

    print("\nPassword Analysis")
    print("-" * 30)

    print(f"Score    : {score}/100")
    print(f"Strength : {strength}")

    print("\nChecks:")

    print(
        f"Length >= 12       : "
        f"{'YES' if len(password) >= 12 else 'NO'}"
    )

    print(
        f"Lowercase          : "
        f"{'YES' if re.search(r'[a-z]', password) else 'NO'}"
    )

    print(
        f"Uppercase          : "
        f"{'YES' if re.search(r'[A-Z]', password) else 'NO'}"
    )

    print(
        f"Number             : "
        f"{'YES' if re.search(r'[0-9]', password) else 'NO'}"
    )

    print(
        f"Special character  : "
        f"{'YES' if re.search(r'[^A-Za-z0-9]', password) else 'NO'}"
    )

    # -----------------------------
    # SUGGESTIONS
    # -----------------------------

    if suggestions:

        print("\nSuggestions:")

        for suggestion in suggestions:
            print(f"- {suggestion}")

    else:

        print(
            "\n✅ Excellent! Your password "
            "satisfies the basic checks."
        )

    # -----------------------------
    # RUN AGAIN OPTION
    # -----------------------------

    print("\n" + "-" * 45)

    again = input(
        "Do you want to check another password? (y/n): "
    ).lower()

    if again != "y":

        print("\nThank you for using Password Strength Analyzer!")

        break