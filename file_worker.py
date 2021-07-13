def write_data(cat_happiness):
    file = open("data/mood.txt", "w+")
    file.write(cat_happiness)
    file.seek(0)


def load_data():
    file = open("data/mood.txt", "r+")
    result = file.read()
    return result