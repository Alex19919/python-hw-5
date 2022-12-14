# Створіть модуль vacations_checker який повинен містити глобально обʼявлену функцію def check(date_str) яка здатна виконати перевірку певної дати на те чи є вона державним святом чи ні.
# В модулі vacations_checker заборонено створювати якісь змінні які будуть містити інформацію про свята.
# Функція check повинна використовувати змінну calendar з модулю vacations_calendar.
# Функція приймає строчку наступного формату 'DD/MM/YYYY', наприклад '27/07/2022' - 27 липня 2022 року і повертає None (NoneType) або назву свята(str).
# Вважаємо що свята кожен рік в один і той самий день. Тобто, умовно, пасха не переноситься. Ви можете самі обрати статичний день для свят які зазвичай переносяться, або не включати їх зовсім. Головне показати логіку, а не коректність українських свят.
# Вважаємо що свята не змінюються від року в рік. Тобто ті свята які є в цьому році були і 3 роки назад.
# В модулі vacations_checker заборонено писати будь яку глобальну логіку. Якщо ви хочете протестувати ваш код, ви повинні це робити в іншому модулі, або прибрати логіку перед пушом в репозиторій.
# Приклади:

# check('27/07/2022') -> None
# check('28/07/2022') -> 'День Української Державності'
# check('28/07/2020') -> 'День Української Державності'
