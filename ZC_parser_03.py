import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Получаем слово и его определение
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def translate_to_russian(text):
    try:
        translated = GoogleTranslator(source='en', target='ru').translate(text)
        print(f"Перевод: '{text}' -> '{translated}'")  # Отладочная печать
        return translated
    except Exception as e:
        print(f"Ошибка при переводе: {e}")
        return text


def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        if not word_dict:
            print("Не удалось получить слово. Попробуйте снова позже.")
            break

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и описание
        word_russian = translate_to_russian(word)
        word_definition_russian = translate_to_russian(word_definition)

        print(f"Описание слова: {word_definition_russian}")
        user = input("Какое это слово? (можно на русском или английском): ")

        # Проверяем ввод пользователя на русском и английском
        user_translated = translate_to_russian(user).lower()
        if user.lower() == word.lower() or user_translated == word_russian.lower():
            print("Верно!")
        else:
            print(f"Неверно. Загаданное слово было: {word} ({word_russian})")

        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


if __name__ == "__main__":
    word_game()