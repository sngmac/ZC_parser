from bs4 import BeautifulSoup
import requests
from googletrans import Translator


# url = "https://aptekiplus.ru/samara/articles/vstrechaem-novyy-god-v-svoey-luchshey-forme/"
# response = requests.get(url)
# print(response.text)
#html = response.text

#soup = BeautifulSoup(html, "html.parser")

#links = soup.find_all("a")
#for link in links:
#    print(link.get('href'))

# ____
# url = "http://quotes.toscrape.com/"
# response = requests.get(url)
# html = response.text
#
# soup = BeautifulSoup(html, "html.parser")
#
# text = soup.find_all("span", class_="text")
# print(text)
# author = soup.find_all("small", class_="author")
# print(author)
#
# for i in range(len(text)):
#     print(f"Цитата номер - {i + 1}")
#     print(text[i].text)
#     print(f"Автор цитаты - {author[i].text}\n")


# ____

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово ? ")
        if user ==word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадо это слово - {word}")

        play_again = input("Хотите сыграть еще раз, y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()