def json_to_wml(json_string):
    """Конвертирует JSON строку в WML."""
    parsed_json = parse_json(json_string)
    wml_result = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<wml>{parse_value(parsed_json, 'wml')}</wml>"
    return wml_result


def parse_value(value, format_type):
    """Обрабатывает значения при конвертации в WML."""
    if isinstance(value, dict):
        return parse_object(value, format_type)
    elif isinstance(value, list):
        return parse_array(value, format_type)
    elif isinstance(value, str):
        return escape_xml(value)  # Экранирование для WML тоже требуется.
    elif value is None:
        return ""
    else:
        return str(value)


def parse_object(obj, format_type):
    """Конвертирует dict в WML."""
    result = ""
    for key, value in obj.items():
        result += f"<card id=\"{key}\" title=\"{key}\">{parse_value(value, format_type)}</card>"
    return result


def parse_array(array, format_type):
    """Конвертирует list в WML."""
    result = ""
    for item in array:
        result += f"<p>{parse_value(item, format_type)}</p>"
    return result


def escape_xml(text):
    """Экранирует специальные символы XML и WML."""
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("\"", "&quot;")
                .replace("'", "&apos;"))


def parse_json(json_string):
    """Преобразует JSON строку в Python объект."""
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
    """Преобразует JSON строку в Python словарь."""
    obj = {}
    content = json_string[1:-1].strip()
    while content:
        key, content = parse_json_key_value(content)
        obj.update(key)
    return obj


def parse_json_key_value(content):
    """Преобразует пару ключ-значение в JSON объект в словарь и возвращает."""
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
    """Конвертирует JSON массив в список Python."""
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
        if char in "{[":  # открывающие скобки
            stack.append(char)
        elif char in "}]" and stack:  # закрывающие скобки
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
    # Чтение JSON из файла
    with open("schedule.json", "r", encoding="utf-8") as json_file:
        json_data = json_file.read()
    
    # Конвертация JSON в WML
    wml_data = json_to_wml(json_data)

    # Запись в файл WML
    with open("schedule.wml", "w", encoding="utf-8") as file:
        file.write(wml_data)
