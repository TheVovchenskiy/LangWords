import words_handler as wh


class Option:
    def __init__(self, index: int, description: str, callback) -> None:
        self.index = index
        self.description = description
        self.callback = callback

    def call(self, index: int):
        if index == self.index:
            self.callback()
            return True
        else:
            return False


class IOHandler:
    def __init__(self, words_handler: wh.WordsHandler) -> None:
        self.words_handler = words_handler

    def choose_options(self, options: list[Option]):
        # print("Выберите желаемое действие:")
        for option in options:
            print(f"{option.index}. {option.description}")

        print()

        try:
            chosen = int(input("Выберите желаемое действие: "))
            print()
        except ValueError:
            print()
            print("Некорректное значение, введите число из списка:")
            return

        for option in options:
            res = option.call(chosen)
            if res:
                break
        else:
            print()
            print("Неверное значение, введите число из списка:")

    def run(self):
        options = [
            Option(1, "Вывести слова", self.show_words),
            Option(2, "Добавить слово", self.input_new_word),
            Option(3, "Выйти", self.exit),
        ]

        while True:
            self.choose_options(options)

    def exit(self):
        exit()

    def input_new_word(self):
        languages = self.words_handler.get_languages()
        new_word = {}

        print("Введите слово на следующих языках:")
        for language in languages:
            # print(f"{language}: ", end="")
            new_word[language] = (input(f"{language}: "), )

        self.words_handler.add_new_word(new_word)
        print("Новое слово успешно добавлено!")

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

        print("Слова на русском:".upper())
        for word in words:
            print(*word[first_language].values)

        self.__wait()

        print("Перевод:".upper())
        # print()
        for word in words:
            print(
                *word[first_language].values,
                *word[second_language].values,
                sep=" - "
            )

        self.__wait()
