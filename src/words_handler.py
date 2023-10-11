import os
from config import BUNDLE_DIR, WORDS_FILE, WORDS_FILE_DIR
import pandas as pd

from validator import is_list_of_str


class LANGUAGES:
    RUS = "russian"
    KOR = "korean"


class WordsHandler:
    def __init__(self, languages=None) -> None:
        if is_list_of_str(languages):
            self.words = pd.DataFrame(columns=languages)
            while True:
                try:
                    self.__save_words()
                    break
                except OSError:
                    os.mkdir(os.path.abspath(
                        os.path.join(BUNDLE_DIR, WORDS_FILE_DIR)))
        else:
            try:
                self.words = self.__read_words()
            except FileNotFoundError as err:
                raise err

    def __save_words(self):
        self.words.to_csv(WORDS_FILE, sep=";", index=False)

    def __read_words(self) -> pd.DataFrame:
        return pd.read_csv(WORDS_FILE, sep=";")

    def add_new_word(self, new_word: dict):
        new_word = pd.DataFrame.from_dict(new_word)
        self.words = pd.concat([self.words, new_word], ignore_index=True)
        self.__save_words()

    def get_random_word(self) -> pd.DataFrame:
        if len(self.words) == 0:
            return None
        return self.words.sample(n=1)

    def get_random_words(self, words_count: int) -> list[pd.DataFrame]:
        if len(self.words) == 0:
            return None
        if words_count > len(self.words):
            words_count = len(self.words)
        return self.words.sample(n=words_count)
        # return [self.words.sample(n=words_count).items() for i in range(words_count)]
        # res = []
        # while len(res) < words_count:
        #     word = self.get_random_word()
        #     if word not in res:
        #         res.append(word)
        # return res

    def get_languages(self) -> list[str]:
        # print(list(self.words.keys().values))
        return list(self.words.keys().values)
