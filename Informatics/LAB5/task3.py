import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

#рекомендую запускать тут https://colab.research.google.com/drive/1FsFB1vWhf8MyKEPjS-0jbNYXLCmTApca?usp=sharing
# Создаем DataFrame из таблицы, ранее составленной в exel
data = {
    'Date': ['2023-12-18', '2023-12-19', '2023-12-20', '2023-12-21'],
    'Open': [104910, 105080, 104750, 104840],
    'High': [106500, 106550, 106450, 106480],
    'Low': [104750, 104800, 104750, 104760],
    'Close': [105970, 105970, 105970, 105970]
}

# Преобразуем данные в формат DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])  # Преобразуем даты в формат datetime
df.set_index('Date', inplace=True)      # Устанавливаем столбец Date как индекс

# Построение биржевой диаграммы (свечей)
mpf.plot(df, type='candle', title="Биржевая диаграмма", style='yahoo', volume=False)