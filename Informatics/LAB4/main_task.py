def json_to_xml(json_string):
    """стартовая функция для парсера"""
    parsed_json = parse_json(json_string)
    xml_result = f"<root>{parse_value(parsed_json)}</root>"
    return xml_result


def parse_value(value):
    """Обрабатывает значения при конвертации в XML."""
    if isinstance(value, dict):
        return parse_object(value)
    elif isinstance(value, list):
        return parse_array(value)
    elif isinstance(value, str):
        return escape_xml(value)
    elif value is None:
        return ""
    else:
        return str(value)


def parse_object(obj):
    """конвертирует dict в xml."""
    result = ""
    for key, value in obj.items():
        result += f"<{key}>{parse_value(value)}</{key}>"
    return result


def parse_array(array):
    """конвертирует list в xml."""
    result = ""
    for item in array:
        result += f"<item>{parse_value(item)}</item>"
    return result


def escape_xml(text):
    """Экранирует специальные символы XML."""
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("\"", "&quot;")
                .replace("'", "&apos;"))


def parse_json(json_string):
    """отправная функция преобразующая JSON строку в Python-объект."""
    json_string = json_string.strip()
    if json_string.startswith("{") and json_string.endswith("}"):
        return parse_json_object(json_string)
    elif json_string.startswith("[") and json_string.endswith("]"):
        return parse_json_array(json_string)
    elif json_string.startswith("\"") and json_string.endswith("\""):
        return json_string[1:-1]
    elif json_string in ("true", "false"):
        return json_string == "true"
    elif json_string == "null":
        return None
    else:
        try:
            if "." in json_string:
                return float(json_string)
            else:
                return int(json_string)
        except ValueError:
            raise ValueError(f"Invalid JSON value: {json_string}")


def parse_json_object(json_string):
    """отправная функция для конвертации JSON в dict."""
    obj = {}
    content = json_string[1:-1].strip()
    while content:
        key, content = parse_json_key_value(content)
        obj.update(key)
    return obj


def parse_json_key_value(content):
    """преобразует пару ключ-значение в JSON-объекте в dict(в том числе рекусрсивно) и возвращает."""
    colon_index = content.index(":")
    key = content[:colon_index].strip()
    if key.startswith("\"") and key.endswith("\""):
        key = key[1:-1]
    else:
        raise ValueError(f"Invalid JSON key: {key}")
    content = content[colon_index + 1:].strip()
    if content.startswith("{") or content.startswith("["):
        value, remaining = parse_brackets(content)
    else:
        value_end = find_next_comma_or_end(content)
        value = content[:value_end].strip()
        remaining = content[value_end:].strip()
    if remaining.startswith(","):
        remaining = remaining[1:].strip()
    return {key: parse_json(value)}, remaining


def parse_json_array(json_string):
    """конвертация JSON-массива в list"""
    array = []
    content = json_string[1:-1].strip()
    while content:
        if content.startswith("{") or content.startswith("["):
            value, content = parse_brackets(content)
        else:
            value_end = find_next_comma_or_end(content)
            value = content[:value_end].strip()
            content = content[value_end:].strip()
        array.append(parse_json(value))
        if content.startswith(","):
            content = content[1:].strip()
    return array


def parse_brackets(content):
    """Находит закрывающую скобку и возвращает содержимое."""
    stack = []
    for i, char in enumerate(content):
        if char in "{[":
            stack.append(char)
        elif char in "}]":
            stack.pop()
            if not stack:
                return content[:i + 1], content[i + 1:].strip()
    raise ValueError("Unmatched brackets in JSON")


def find_next_comma_or_end(content):
    """Находит позицию следующей запятой или конца строки."""
    for i, char in enumerate(content):
        if char == ",":
            return i
    return len(content)


def main():
    # чтение файла JSON
    json_data = open("schedule.json", "r", encoding="utf-8")
    # использование функции для конвертации нашегой файлв
    xml_data = json_to_xml(json_data.read())
    xml_data = "<?xml version=\"1.0\" encoding=\"utf-8\"?>" + xml_data
    # запись файла xml
    with open("schedule.xml", "w", encoding="utf-8") as file:
        file.write(xml_data)
