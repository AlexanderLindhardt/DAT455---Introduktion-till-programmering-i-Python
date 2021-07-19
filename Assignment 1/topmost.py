import wordfreq
import sys
import urllib.request


def main():
    is_url = False
    if 'http://' in sys.argv[2] or 'https://' in sys.argv[2]:
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
        is_url = True
    else:
        lines = open(sys.argv[2], encoding="utf-8")
    stop_words = open(sys.argv[1], encoding="utf-8")

    n = sys.argv[3]
    tokens = wordfreq.tokenize(lines)

    stop_words_stripped = []
    for word in stop_words:
        word_stripped = word.strip()
        stop_words_stripped.append(word_stripped)
    word_counts = wordfreq.countWords(tokens, stop_words_stripped)
    wordfreq.printTopMost(word_counts, n)
    stop_words.close()
    if not is_url:
        lines.close()


if __name__ == "__main__":
    main()
