import json
import xmltodict


def main():
    # Чтение JSON-файла
    with open('schedule.json', 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    # Преобразование JSON в XML
    xml_data = xmltodict.unparse({'root': json_data}, pretty=True)

    # Запись XML в файл
    with open('schedule_1.xml', 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_data)
