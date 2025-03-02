import re

def password_strength(password):
    # Initialize strength score
    score = 0
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'\d', password)
    special_char_criteria = re.search(r'[@$!%*?&]', password)
    # Evaluate criteria
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1
    # Determine strength level
    if score == 5:
        strength = 'Very Strong'
    elif score == 4:
        strength = 'Strong'
    elif score == 3:
        strength = 'Moderate'
    elif score == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'
    # Feedback message
    feedback = []
    if not length_criteria:
        feedback.append('Password should be at least 8 characters long.')
    if not uppercase_criteria:
        feedback.append('Password should include at least one uppercase letter.')
    if not lowercase_criteria:
        feedback.append('Password should include at least one lowercase letter.')
    if not digit_criteria:
        feedback.append('Password should include at least one digit.')
    if not special_char_criteria:
        feedback.append('Password should include at least one special character (@, $, !, %, *, ?, &).')
    # Return strength and feedback
    return strength, feedback

# Example usage
if __name__ == "__main__":
    pwd = input("Enter a password to check its strength: ")
    strength, feedback = password_strength(pwd)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for f in feedback:
            print(f"- {f}")
