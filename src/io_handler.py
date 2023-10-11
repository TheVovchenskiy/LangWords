import sys
from termcolor import cprint
import words_handler as wh


class Option:
    def __init__(self, index: int, description: str, callback) -> None:
        self.index = index
        self.description = description
        self.callback = callback

    def call(self, index: int, *args, **kwargs):
        if index == self.index:
            return (True, self.callback(*args, **kwargs))
        else:
            return (False, None)


def print_error(*messages):
    print()
    for message in messages:
        cprint(message, "red", end=" ")
    print()

def print_success(*messages):
    print()
    for message in messages:
        cprint(message, "green", end=" ")
    print()

class IOHandler:
    def __init__(self) -> None:
        try:
            self.words_handler = wh.WordsHandler()
        except FileNotFoundError:
            print("Пока слов нет :(")

            while True:
                line = input(
                    "Пожалуйста, введите языки, которые вы хотите использовать (разделенные пробелом): "
                )
                languages = line.split()
                print("Ваши языки, верно?")
                for language in languages:
                    print(f"\t- {language}")
                options = [
                    Option(1, "Да", lambda: True),
                    Option(2, "Нет", lambda: False),
                ]
                if self.choose_options(options):
                    break

            self.words_handler = wh.WordsHandler(languages)

    def choose_options(self, options: list[Option], *args, **kwargs) -> any:
        for option in options:
            print(f"{option.index}. {option.description}")

        print()

        try:
            chosen = int(input("Выберите желаемое действие: "))
            # print()
        except ValueError:
            print_error("Некорректное значение, введите число из списка:")
            return

        for option in options:
            called, callback_res = option.call(chosen, *args, **kwargs)
            if called:
                return callback_res
        else:
            print_error("Неверное значение, введите число из списка:")

    def run(self):
        options = [
            Option(1, "Вывести случайные слова", self.show_words),
            Option(2, "Добавить слово", self.input_new_word),
            Option(3, "Выйти", self.exit),
        ]

        while True:
            self.choose_options(options)

    def exit(self):
        sys.exit()

    def input_new_word(self):
        languages = self.words_handler.get_languages()
        new_word = {}

        print("Введите слово на следующих языках:")
        for language in languages:
            # print(f"{language}: ", end="")
            new_word[language] = (input(f"{language}: "), )

        self.words_handler.add_new_word(new_word)
        print_success("Новое слово успешно добавлено!")
        print()

    def __wait(self):
        print()
        input("Чтобы продолжить нажмите 'ENTER'...")
        print()

    def show_words(
        self,
        words_count=5,
        first_language=wh.LANGUAGES.RUS,
        second_language=wh.LANGUAGES.KOR,
    ) -> None:
        # print(self.words.sample(n=words_count))
        words = self.words_handler.get_random_words(words_count)
        if words is None:
            print_error("Пока слов нет")
            print()
            return

        print("Слова на русском:".upper())
        # print(*words[first_language], sep="\n")
        for word in words[first_language]:
            print("\t-", word)

        self.__wait()

        print("Перевод:".upper())
        for _, word in words.iterrows():
            print("\t-", word[second_language], " : ", word[first_language])
        # print()
        # for word in words:
        #     print(
        #         *word[first_language].values,
        #         *word[second_language].values,
        #         sep=" - "
        #     )

        self.__wait()
