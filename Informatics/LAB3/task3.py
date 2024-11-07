import re


def find_cost_BTC(arg):
    blocks = re.findall(r'<[^<]*>', arg)
    result = "НИЧЕГО НЕТ"
    for block in blocks:
        if re.search(r'bitcoin|btc', block, flags=re.IGNORECASE):
            result = re.findall(r'(?:(?:[1-9]+[.,0-9]+)\s(?:rub|₽))|(?:(?:rub|₽)(?:[1-9]+[.,0-9]+))', block, flags=re.IGNORECASE)
            if not result:
                continue
            else:
                break
    if not result:
        return 'Цена не найдена'
    return f'цена биткоина на данный момент: {result[0]}'


# тест на возможность находить нужный блок и парсить из него стоимость
print(find_cost_BTC('''<meta name="daily_price"
content=" Цена bitcoin в реальном времени сегодня составляет ₽5,797,806.88
RUB."/>'''))
# тест на возможность находить не только bitcoin но и btc и тест на регистрозависимость
print(find_cost_BTC('''<meta name="daily_price"
content=" Цена BtC в реальном времени сегодня составляет ₽5,797,806.88
RUB."/>'''))
# тест на распознования цены только в блоке с Bitcoin
print(find_cost_BTC('''<meta name="daily_volume" content="В суточным объемом торгов
₽2,835,029,974,960.63 RUB."/> <meta name="daily_price"
content=" Цена Bitcoin в реальном времени сегодня составляет ₽5,797,806.88
RUB."/><meta name="daily_price" content="Ethereum стоит на данный момент
₽229,590,78 RUB."/>
'''))
# тест на игнорирование блока содержащего BTC, но не содержащего цену.
print(find_cost_BTC('''<meta name="daily_price" content="Мы обновляем
нашу цену BTC к RUB в режиме реального времени."/> <meta name="daily_price"
content=" Цена Bitcoin в реальном времени сегодня составляет ₽5,797,806.88 RUB."/>
'''))
# тест на распознавания RUB вместо ₽ + возможность их распознования, если они расположены после числа
print(find_cost_BTC('''<meta name="daily_price"
content=" Цена bitcoin в реальном времени сегодня составляет 5,797,806.88 RUB"/>'''))
# тест из здания. проверяет на все вышеперечисленное
print(find_cost_BTC('''<meta name="daily_volume" content="В суточным объемом торгов
₽2,835,029,974,960.63 RUB."/> <meta name="daily_price" content="Мы обновляем
нашу цену BTC к RUB в режиме реального времени."/> <meta name="daily_price"
content=" Цена Bitcoin в реальном времени сегодня составляет ₽5,797,806.88 RUB."/>
<meta name="daily_price" content="Ethereum стоит на данный момент ₽229,590,78 RUB."/>
'''))


