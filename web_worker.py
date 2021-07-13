import requests
from bs4 import BeautifulSoup

URL = "https://lite.cnn.com/en"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="mount")
more_results = soup.find("div", class_="afe4286c")

negative_words = ["killed", "died", "loss", "threat", "harmful", "worse", "dead"]
positive_words = ["won", "succeeded", "celebration",
                  "good", "fun", "happy", "solution",
                  "success", "better", "civil rights", "survivors"]
food_words = ["food", "hunger", "cook", "cooking", "rare", "superfood", "diet"]

negative_word_count = 0
positive_word_count = 0
food_word_count = 0
word_dict = more_results.text.split()

for word in word_dict:
    for n in range(len(negative_words)):
        if word == negative_words[n]:
            negative_word_count += 1
            break
    for p in range(len(positive_words)):
        if word == positive_words[p]:
            positive_word_count += 1
            break
    for f in range(len(food_words)):
        if word == food_words[f]:
            food_word_count += 1


def get_mental_health_data():
    return (positive_word_count - negative_word_count) * 5


def get_food_data():
    return food_word_count * 3





