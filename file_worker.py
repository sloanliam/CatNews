def write_mood_data(cat_happiness):
    file = open("data/mood.txt", "w+")
    file.write(cat_happiness)
    file.seek(0)


def load_mood_data():
    file = open("data/mood.txt", "r+")
    result = file.read()
    return result


def write_food_data(hunger):
    file = open("data/food.txt", "w+")
    file.write(hunger)
    file.seek(0)


def load_food_data():
    file = open("data/food.txt")
    result = file.read()
    return result