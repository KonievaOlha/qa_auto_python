import requests
import datetime


def test_api_hw():
    URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.request(method="GET", url=URL)
    content_json = response.json()
    write_text = ""
    current_date = datetime.datetime.now()
    create_date = f"===============Дата створення запиту===============\n"
    query_date = f"==============={str(current_date)}===============\n\n"
    with open("api_hw.txt", "w", encoding="utf-8") as file:
        for i in range(len(content_json)):
            write_text += f" {content_json[i]['txt']} to UAH: {content_json[i]['rate']}\n"
        file.write(create_date)
        file.write(query_date)
        file.write(write_text)
