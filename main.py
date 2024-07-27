def convert_case(text):
    uppercase = text.upper()
    lowercase = text.lower()
    titlecase = text.title()
    
    return uppercase, lowercase, titlecase

# Get user input
user_input = input("Enter a character, word, or sentence: ")

# Convert case
uppercase, lowercase, titlecase = convert_case(user_input)

# Display results
print("\nConverted Cases:")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Title Case: {titlecase}")
