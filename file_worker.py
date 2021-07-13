def write_mood_data(cat_happiness):
    try:
        file = open("data/mood.txt", "w+")
        file.write(cat_happiness)
        file.seek(0)
    except IOError:
        print("file not found")


def load_mood_data():
    try:
        file = open("data/mood.txt", "r+")
        result = file.read()
        return result
    except IOError:
        print("file not found")


def write_food_data(hunger):
    try:
        file = open("data/food.txt", "w+")
        file.write(hunger)
        file.seek(0)
    except IOError:
        print("file not found")


def load_food_data():
    try:
        file = open("data/food.txt")
        result = file.read()
        return result
    except IOError:
        print("file not found")