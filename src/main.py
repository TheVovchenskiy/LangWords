import json
# from config import FILE_NAME
from words_handler import WordsHandler


if __name__ == "__main__":
    words_handler = WordsHandler()

    words_handler.show_words()

    # words = {}
    # with open(FILE_NAME, encoding="utf8") as file:
    #     for line in file:
    #         kor, rus = line.strip().split(";")
    #         print(kor, rus)
    #         words[kor] = rus

    # with open("korean_words.json", "w", encoding="utf8") as file:
    #     json.dump(words, file, ensure_ascii=False)
