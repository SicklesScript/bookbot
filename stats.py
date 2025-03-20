def word_count(text):
    words = text.split()
    count = len(words)
    return count

def letter_count(text):
    letter_counts = {}
    
    for char in text.lower():
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
            
    reversed_dict = {v: k for k, v in letter_counts.items()}
    return dict(sorted(reversed_dict.items(), reverse=True))

