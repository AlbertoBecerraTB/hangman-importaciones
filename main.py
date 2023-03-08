import sys
import os
sys.path.append(os.getcwd())

from utils.config import HANGMAN, EMPTY_SOLUTION
from lib.err import show_errors
from lib.check_sol import check_letter

err = 4
show_errors(err, HANGMAN)

sol = "PARLA"
word = EMPTY_SOLUTION
letter = "L"

out = check_letter(letter, sol, word)
print(out)
