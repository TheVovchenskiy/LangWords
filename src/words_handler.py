from config import FILE_NAME
import json
import random


class WordTranslation:
    def __init__(self, korean: str, russian: str) -> None:
        self.korean = korean
        self.russian = russian

    def __str__(self) -> str:
        return f"korean: {self.korean}\nrussian: {self.russian}"


class WordsHandler:
    def __init__(self) -> None:
        self.words = self.__read_words()

    def __read_words(self) -> list[WordTranslation]:
        with open(FILE_NAME, encoding="utf8") as file:
            korean_words = json.load(file)

        return [WordTranslation(kor, rus) for kor, rus in korean_words.items()]

    def get_random_word(self) -> WordTranslation:
        return random.choice(self.words)

    def get_random_words(self, words_count: int) -> list[WordTranslation]:
        return [self.get_random_word() for i in range(words_count)]

    def show_words(self, words_count=5) -> None:
        words = self.get_random_words(words_count)

        print("Слова на русском:".upper())
        for word in words:
            print(word.russian)
        
        print()
        print("Чтобы продолжить нажмите 'enter'...")
        input()

        print("Перевод:".upper())
        # print()
        for word in words:
            print(word)
            print()
