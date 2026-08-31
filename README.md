# 🔐 Password Strength Analyzer

A Python-based cybersecurity project that analyzes password strength and provides security recommendations.

## 📌 Features

* Checks password length
* Detects lowercase letters
* Detects uppercase letters
* Detects numbers
* Detects special characters
* Detects repeated characters
* Checks against a list of common passwords
* Generates a password score from 0–100
* Classifies passwords as:

  * Very Weak
  * Weak
  * Medium
  * Strong
  * Very Strong
* Provides suggestions for improving weak passwords
* Allows the user to analyze multiple passwords in one execution

## 🛠️ Technologies Used

* Python
* Regular Expressions (`re`)
* Conditional statements
* Functions
* Loops
* Lists and Sets
* User input handling

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/password-strength-analyzer.git
```

Go into the project directory:

```bash
cd password-strength-analyzer
```

Run the program:

```bash
python password_analyzer.py
```

## 💻 Example

```text
=============================================
       PASSWORD STRENGTH ANALYZER
=============================================

Enter your password: Hello@123

Password Analysis
------------------------------
Score    : 45/100
Strength : MEDIUM

Checks:
Length >= 12       : NO
Lowercase          : YES
Uppercase          : YES
Number             : YES
Special character  : YES
```

## 🔍 Security Checks

The analyzer evaluates passwords based on:

| Check               | Purpose                                                |
| ------------------- | ------------------------------------------------------ |
| Length              | Longer passwords are generally harder to guess         |
| Lowercase           | Checks for lowercase characters                        |
| Uppercase           | Checks for uppercase characters                        |
| Numbers             | Checks for numeric characters                          |
| Special Characters  | Checks for symbols                                     |
| Repeated Characters | Detects simple repeated patterns                       |
| Common Passwords    | Identifies passwords from a small common-password list |

## ⚠️ Disclaimer

This project is intended for educational and portfolio purposes.

It is not a replacement for professional password-security libraries or enterprise password-strength systems.

Do not enter real passwords that you currently use on important accounts.

## 🚀 Future Improvements

* Entropy calculation
* Larger dictionary/common-password database
* Keyboard-pattern detection
* Password breach checking using a privacy-preserving API
* Graphical user interface using Tkinter
* Password generation
* Detailed security scoring
* Exporting analysis results

## 👨‍💻 Author

YOUR NAME

GitHub: https://github.com/CypherHarsh0
LinkedIn: https://www.linkedin.com/in/harsh-nomul/
