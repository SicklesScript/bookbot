from stats import word_count, letter_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    count = word_count(text)
    print(f"Found {count} total words")
    
    chars = letter_count(text)
    swap_chars = {v: k for k, v in chars.items()}
    
    for char, count in swap_chars.items():
        print(f"{char}: {count}")

main()

