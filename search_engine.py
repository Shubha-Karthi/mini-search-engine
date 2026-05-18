import string
from collections import Counter
import heapq

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        return ""

def process_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words

def build_frequency(words):
    return Counter(words)

def search_word(freq_dict, word):
    word = word.lower()
    if word in freq_dict:
        print(f"'{word}' found {freq_dict[word]} times")
    else:
        print(f"'{word}' not found")

def top_k_words(freq_dict, k=5):
    print(f"\nTop {k} frequent words:")
    top_words = heapq.nlargest(k, freq_dict.items(), key=lambda x: x[1])
    for word, count in top_words:
        print(word, "→", count)

def show_sorted(freq_dict):
    print("\nWords sorted by frequency:")
    sorted_words = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(word, "→", count)

def main():
    filename = input("Enter file name (e.g., data.txt): ")
    
    text = read_file(filename)
    if not text:
        return
    
    words = process_text(text)
    freq_dict = build_frequency(words)

    while True:
        print("\n--- Mini Search Engine ---")
        print("1. Search word")
        print("2. Top frequent words")
        print("3. Show all sorted words")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            word = input("Enter word to search: ")
            search_word(freq_dict, word)

        elif choice == "2":
            k = int(input("Enter value of k: "))
            top_k_words(freq_dict, k)

        elif choice == "3":
            show_sorted(freq_dict)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
