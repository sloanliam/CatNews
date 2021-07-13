import requests
from bs4 import BeautifulSoup

URL = "https://lite.cnn.com/en"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="mount")
more_results = soup.find("div", class_="afe4286c")

negative_words = ["killed", "died", "loss", "threat", "harmful", "worse"]
positive_words = ["won", "succeeded", "celebration",
                  "good", "fun", "happy", "solution",
                  "success", "better", "makeover", "vaccine"]

negative_word_count = 0
positive_word_count = 0
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


def get_data():
    return (positive_word_count - negative_word_count) * 10


print(word_dict)



