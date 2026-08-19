from datetime import datetime, timedelta

data_str = "2026/06/04 12:51:33"
data_format = "%Y/%m/%d %H:%M:%S"
print(datetime.strptime(data_str, data_format))

data_inicio = datetime.strptime("1987/04/20 09:30:15", data_format)
data_fim = datetime.strptime("2022/12/12 08:20:25", data_format)
delta = data_fim - data_inicio
delta_mais10 = timedelta(days=10, hours=2)
print(data_fim > data_fim)
print(delta)
print(data_fim + delta_mais10)
print()
# --- formatando data ---
print(data_fim.strftime("%d-%m-%Y %H:%M"))
print(data_fim.strftime("%Y"), data_fim.year)
