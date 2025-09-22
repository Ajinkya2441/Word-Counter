import re
from collections import Counter

def count_words(text):
    # Use regex to split by any whitespace
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def main():
    print("📄 Word Counter")

    print("\nEnter/paste your text below. When done, enter a blank line to finish input:\n")

    # Read multiline input until blank line
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    text = "\n".join(lines)

    if not text.strip():
        print("⚠️ No text entered.")
        return

    # Count lines
    line_count = len(lines)

    # Count characters (including spaces and newlines)
    char_count = len(text)

    # Count words
    words = count_words(text)
    word_count = len(words)

    print(f"\nLines: {line_count}")
    print(f"Characters (including spaces): {char_count}")
    print(f"Words: {word_count}")

    # Ask if user wants word frequency
    freq_choice = input("\nDo you want to see frequency of each word? (y/N): ").strip().lower()
    if freq_choice == 'y':
        word_freq = Counter(words)
        print("\nWord Frequencies:")
        for word, count in word_freq.most_common():
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()
