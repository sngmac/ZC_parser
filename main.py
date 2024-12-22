import requests
import pprint

# response = requests.get('https://api.github.com/')
# # print(response.status_code)
# # if response.ok:
# #     print("Запрос успешно выполнен")
# # else:
# #     print("Произошла ошибка")
# print(response.text)
# response_json = response.json()
# pprint.pprint(response_json)


# params = {
#     'q' : 'python'
# }
#
# response = requests.get ('https://api.github.com/search/repositories', params=params)
#
# response_json = response.json()
#
# print(f"количество репозиториев python:{response_json['total_count']}")


# img = "https://aptekiplus.ru/media-data/articles/images/fitnes-dlya-novichkov-detail.png"
#
# response = requests.get(img)
#
# with open("test.jpg", "wb") as file:
#     file.write(response.content)

pip install googletrans==4.0.0-rc1



