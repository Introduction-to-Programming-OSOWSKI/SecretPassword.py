#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 10
day = 8

def test_code():
    assert main.password("Knights19") == "ACCESS GRANTED", "password('Knights19') == ACCESS GRANTED failed"
    assert main.password("Ksdsdgssdb") == "ACCESS DENIED", "password('Ksdsdgssdb') == ACCESS DENIED failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
