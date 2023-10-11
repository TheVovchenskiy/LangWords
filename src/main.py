from words_handler import WordsHandler
from io_handler import IOHandler


if __name__ == "__main__":
    words_handler = WordsHandler()
    io_handler = IOHandler(words_handler)

    # io_handler.show_words()
    # words_handler.get_languages()
    # io_handler.input_new_word()
    io_handler.run()
