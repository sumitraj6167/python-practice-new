#python program to calculate the number of words and characters present in a string.

def count_words_characters(text):
    # Count characters (excluding spaces if you want)
    characters = len(text)
    
    # Count words (split by spaces)
    words = len(text.split())
    
    return words, characters

# Example usage
user_input = input("Enter a string: ")
words, characters = count_words_characters(user_input)

print(f"Number of words: {words}")
print(f"Number of characters: {characters}")
