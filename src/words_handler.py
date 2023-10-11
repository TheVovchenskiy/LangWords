from config import WORDS_FILE_PATH
# import json
import random
import pandas as pd


class WordTranslation:
    def __init__(self, korean: str, russian: str) -> None:
        self.korean = korean
        self.russian = russian

    def __str__(self) -> str:
        return f"korean: {self.korean}\nrussian: {self.russian}"


class WordsHandler:
    def __init__(self) -> None:
        self.words = self.__read_words()
        # print(self.words)

    def __read_words(self) -> pd.DataFrame:
        return pd.read_csv(WORDS_FILE_PATH, sep=";")

    def get_random_word(self) -> pd.DataFrame:
        return self.words.sample(n=1)

    def get_random_words(self, words_count: int) -> list[pd.DataFrame]:
        return [self.get_random_word() for i in range(words_count)]

    def show_words(self, words_count=5) -> None:
        # print(self.words.sample(n=words_count))
        words = self.get_random_words(words_count)

        print("Слова на русском:".upper())
        for word in words:
            print(*word['Russian'].values)
        
        print()
        print("Чтобы продолжить нажмите 'enter'...")
        input()

        print("Перевод:".upper())
        # print()
        for word in words:
            print(*word['Russian'].values, *word['Korean'].values, sep=" - ")
