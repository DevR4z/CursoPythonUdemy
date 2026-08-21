import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

print(calendar.calendar(2026))
print(locale.getlocale())
