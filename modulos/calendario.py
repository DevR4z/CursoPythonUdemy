import calendar

# print(calendar.calendar(2026))
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2026, 4)
print(calendar.day_name[numero_primeiro_dia])
print(calendar.day_name[calendar.weekday(2026, 4, ultimo_dia)])
