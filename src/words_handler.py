from config import WORDS_FILE_PATH
# import json
import random
import pandas as pd


class LANGUAGES:
    RUS = "Russian"
    KOR = "Korean"


class WordsHandler:
    def __init__(self) -> None:
        self.words = self.__read_words()
        # print(self.words)
    
    def __save_words(self):
        self.words.to_csv(WORDS_FILE_PATH, sep=";", index=False)

    def __read_words(self) -> pd.DataFrame:
        return pd.read_csv(WORDS_FILE_PATH, sep=";")

    def add_new_word(self, new_word: dict):
        new_word = pd.DataFrame.from_dict(new_word)
        self.words = pd.concat([self.words, new_word], ignore_index=True)
        self.__save_words()

    def get_random_word(self) -> pd.DataFrame:
        return self.words.sample(n=1)

    def get_random_words(self, words_count: int) -> list[pd.DataFrame]:
        return [self.get_random_word() for i in range(words_count)]

    def get_languages(self) -> list[str]:
        # print(list(self.words.keys().values))
        return list(self.words.keys().values)
