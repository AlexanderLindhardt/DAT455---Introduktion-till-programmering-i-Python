# Tokenization, separates words in a text and returns the words as a list
def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):

            if line[start].isspace():  # If there is a space, we just let the index increment by 1
                pass

            elif line[start].isdigit():  # When we see a digit, we count how many digits are following
                end = start
                while line[end].isdigit():
                    end += 1
                    if end >= len(line):  # If we reach the end of the line, we need to break
                        break

                words.append(line[start:end])  # Append the "word" to the final list
                start = end - 1

            elif line[start].isalpha():  # When we see a letter, we count how many letters are following
                end = start
                while line[end].isalpha():
                    end += 1
                    if end >= len(line):  # If we reach the end of the line, we need to break
                        break

                words.append(line[start:end].lower())  # Append the word to the final list
                start = end - 1

            else:  # If it's neither a letter or digit, we have a symbol. We just add this symbol to the word list
                words.append(line[start])

            start = start + 1  # Move to the next index
    return words


def countWords(words, stopWords):  # Count the occurrences of words in a word list, ignoring some stop words
    counts = {}
    for word in words:
        if word in stopWords:  # If word is a stop word we ignore it
            continue
        else:
            if word in counts:  # If it's a word already encountered we just increase the frequency by 1
                counts[word] += 1
            else:
                counts[word] = 1  # If it's a new word we add it to the dict and set the value to 1
    return counts


def printTopMost(frequencies, n):  # Prints the top n words based on frequencies
    n = int(n)
    if n > len(frequencies):  # If n is larger than the list of words, we set it to its max value
        n = len(frequencies)
    sorted_freq = sorted(frequencies.items(), key=lambda x: -x[1])  # Sort words based on frequencies
    for i in range(n):  # Print the first n words and their counts
        print(sorted_freq[i][0].ljust(20) + str(sorted_freq[i][1]).rjust(5))

