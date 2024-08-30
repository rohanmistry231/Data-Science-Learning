# function to read five letter words from the list
# saving extracted words in a new file

def main():
    file_path = "data/words.txt"
    output_path= "data/wordle_words.txt"
    wordle_words = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            word = line.strip()
            if len(word)==5:
                wordle_words.append(word)

    

    with open(output_path, 'w') as f:
        for word in wordle_words:
            f.write(word +'\n')
    print(f"Found {len(wordle_words)} in the file")

if __name__ == "__main__":
    main()