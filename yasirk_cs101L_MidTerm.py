def word_count(text):
    """Count the number of words of the text that was input."""
    words = text.split()
    return len(words)

def find_longest_word(text):
    """Find and return the longest word in the text that was input."""
    words = text.split()
    return max(words, key=len)

def count_substring(text, substring):
    "Count the occurrences of a substring in the text that was input."""
    return text.count(substring)

def extract_unique_words(text):
    """Extract and return a list of unique words from the text that was input."""
    words = set(text.split())
    return list(words)

def main():
    print("Welcome to Text Processing Test!")
    user_text = input("Please enter a text to process: ")

    print("\nOriginal Text:")

    print(user_text)
    
    while True:
        
        print("\nText Analysis Options:")
        print("1. Word Count")
        print("2. Longest Word")
        print("3. Count of Substring")
        print("4. Unique Words")
        print("5. Exit")

        choice = input("Enter the number of your choice (1-5): ")

        if choice == '1':
            print(f"Word Count: {word_count(user_text)}")
            
        elif choice == '2':
            print(f"Longest Word: {find_longest_word(user_text)}")
            
        elif choice == '3':
            substring = input("Enter the substring to count: ")
            print(f"Occurrences of '{substring}': {count_substring(user_text, substring)}")
            
        elif choice == '4':
            unique_words = extract_unique_words(user_text)
            print("Unique Words:", unique_words)
            
        elif choice == '5':
            print("Thank you for using the Text Processing Program!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    
