MINUTE = 1
HORSE = 60
DAY = HORSE * 24
WEEK = DAY * 7
MONTH = DAY * 30
YEAR = DAY * 365

PERIODIC_CHOICES = [
    (MINUTE, 'Минута'),
    (HORSE, 'Час'),
    (DAY, 'День'),
    (WEEK, 'Неделя'),
    (MONTH, 'Месяц'),
    (YEAR, 'Год'),
]

CREATED = 'CR'
LAUNCHED = 'LA'
COMPLETED = 'CP'
PAUSED = 'PA'

STATUS_CHOICES = [
    (CREATED, 'Создание'),
    (LAUNCHED, 'Запущена'),
    (COMPLETED, 'Завершина'),
    (PAUSED, 'Пауза'),
]

