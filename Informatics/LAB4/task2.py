import re


def start_json_to_xml(json_str):
    """стартовая функция парсера."""
    # Шаблон для поиска ключей и значений в JSON
    pattern = r'"([^"]+)":\s*(".*?"|\d+|true|false|null|\{.*?\}|\[.*?\])'
    # Основной процесс извлечения данных и создания XML
    xml_result = ''.join([json_to_xml(match) for match in re.finditer(pattern, json_str, re.DOTALL)])
    return f"<root>{xml_result}</root>"


def json_to_xml(match):
    """основная функция парсера."""
    key = match.group(1)
    value = match.group(2)
    # Если значение это строка
    if value.startswith('"'):
        value = value[1:-1]
        return f"<{key}>{value}</{key}>"
    # Если значение это объект
    elif value.startswith('{'):
        return f"<{key}>{json_to_xml_for_object(value)}</{key}>"
    # Если значение это массив
    elif value.startswith('['):
        return f"<{key}>{json_to_xml_for_array(value)}</{key}>"
    # Если это число, true, false или null
    else:
        return f"<{key}>{value}</{key}>"


def json_to_xml_for_object(value):
    """Функция для обработки словаря"""
    value = value[1:-1]
    pattern = r'"([^"]+)":\s*(".*?"|\d+|true|false|null|\{.*?\}|\[.*?\])'
    return ''.join([json_to_xml(match) for match in re.finditer(pattern, value, re.DOTALL)])


def json_to_xml_for_array(value):
    """Функция для обработки массива"""
    value = value[1:-1]
    elements = re.findall(r'(".*?"|\d+|true|false|null|\{.*?\}|\[.*?\])', value, re.DOTALL)
    return ''.join([json_to_xml_for_value(el) for el in elements])


def json_to_xml_for_value(value):
    """Функция для обработки значений массива"""
    if value.startswith('"'):
        value = value[1:-1]
        return f"<item>{value}</item>"
    elif value.startswith('{'):
        return f"<item>{json_to_xml_for_object(value)}</item>"
    elif value.startswith('['):
        return f"<item>{json_to_xml_for_array(value)}</item>"
    else:
        return f"<item>{value}</item>"


def main():
    # Чтение JSON-файла
    with open('schedule.json', 'r', encoding='utf-8') as json_file:
        json_content = json_file.read()
    # Преобразование JSON в XML
    xml_data = start_json_to_xml(json_content)
    xml_data = "<?xml version=\"1.0\" encoding=\"utf-8\"?>" + xml_data
    # Запись XML в файл
    with open('schedule_2.xml', 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_data)
