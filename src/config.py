import sys
import os

WORDS_FILE_DIR = "data"
WORDS_FILE_NAME = "words.csv"
WORDS_REL_FILE_PATH = os.path.join(WORDS_FILE_DIR, WORDS_FILE_NAME)

BUNDLE_DIR = getattr(
    sys, "_MEIPASS",
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

WORDS_FILE = os.path.abspath(os.path.join(BUNDLE_DIR, WORDS_REL_FILE_PATH))
# print(WORDS_FILE)
