import pickle
import os

HIGHSCORE_FILE = 'highscore.dat'

def load_highscore():
    """Loads the high score from a file, or returns 0 if the file doesn't exist."""
    if os.path.exists(HIGHSCORE_FILE):
        try:
            with open(HIGHSCORE_FILE, 'rb') as f:
                return pickle.load(f)
        except (IOError, pickle.UnpicklingError):
            # Handle potential errors with file reading/unpickling
            return 0
    return 0

def save_highscore(score):
    """Saves the high score to a file."""
    try:
        with open(HIGHSCORE_FILE, 'wb') as f:
            pickle.dump(score, f)
    except IOError:
        print("Error: Could not save high score.")
