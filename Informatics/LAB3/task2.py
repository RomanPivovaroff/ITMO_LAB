from re import findall


def is_xaiky(arg):
    parts = arg.split('/')
    if len(parts) != 3:
        return 'Не хайку. Должно быть 3 строки.'
    slogs = 0
    iter = 0
    for i in parts:
        slogs += (len(findall(r'[ауоиэыяюеё]', i.lower())) * (10 ** iter))
        iter += 1
    return ['Не хайку.', 'хайку!'][slogs == 575]


# тест на не хайку (Не хайку.)
print(is_xaiky('тут проверим / простой / текст'))
# тест на хайку (хайку!)
print(is_xaiky('а тут типо ха / йку даааааа / вот вот а вы ду?'))
# тест на нечуствительность к регистру (хайку!)
print(is_xaiky('а тут типо ха / йку ДАААААа / вОт вот а вЫ ду?'))
# тест на ё (хайку!)
print(is_xaiky('а тут типо ха / йку даааааа / вОт вот а вы ё?'))
# тест на лишние разделители (Не хайку. Должно быть 3 строки.)
print(is_xaiky('а / тут / больше / строк/ ха/ ха/'))
