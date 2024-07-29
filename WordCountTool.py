import string

def count_words(text):
    
    translator = str.maketrans('', '', string.punctuation)
    text_no_punct = text.translate(translator)
    words = text_no_punct.lower().split()
    return len(words)

def main():
    print("Welcome to the Word Count Tool!")
    while True:
        print("\nSelect input method:")
        print("1. Enter text manually")
        print("2. Read from a file")
        print("3. Exit")
        
        choice = input("Enter choice ( 1 / 2 / 3 ): ")
        
        if choice == '1':
            text = input("Enter the text: ")
            if not text:
                print("Error: Empty text. Please try again.")
                continue
            word_count = count_words(text)
            print(f"Word count: {word_count}")
            
        elif choice == '2':
            filename = input("Enter the filename: ")
            try:
                with open(filename, 'r') as file:
                    text = file.read()
                    if not text:
                        print("Error: File is empty. Please try again.")
                        continue
                    word_count = count_words(text)
                    print(f"Word count: {word_count}")
            except FileNotFoundError:
                print("Error: File not found. Please try again.")
                
        elif choice == '3':
            print("Thanks for using the Word Count Tool.")
            break
            
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()