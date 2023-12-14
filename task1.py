import logging
import argparse
from datetime import datetime
'''
Home Work 6.1. программа для проверки корректности даты, введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год". 
программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.

На входе:
date_to_prove = 15.4.2023
На выходе:
True

На входе:
date_to_prove = 31.6.2022
На выходе:
False
'''
try:
	logging.basicConfig(filename='./logs/task1.log', encoding='utf-8', level=logging.INFO)
except FileNotFoundError as fn:
	logging.basicConfig(filename='spare.log', encoding='utf-8', level=logging.INFO)
	logger = logging.getLogger('date_checker')
	logger.warning(fn)
else:
	logger = logging.getLogger('date_checker')


parser = argparse.ArgumentParser(description='input date to check')
parser.add_argument('-d', type=str, default=str(datetime.now().day))
parser.add_argument('-m', type=str, default=str(datetime.now().month))
parser.add_argument('-y', type=str, default=str(datetime.now().year))

args = parser.parse_args()
value = '.'.join([args.d, args.m, args.y])

def func(date: str) -> bool:
	try:
		day, month, year = map(int, date.split('.'))
	except ValueError as e:
		logger.error(e)
	else:
		if day in range(1,32) and month in range(1,13) and year in range(1, 10_000):  # проверка на корректность ввода
			logger.info('Проверка на валидность входных данных пройдена')
			if month in [1, 3, 5, 7, 8, 10, 12] and day in range(1,32):  # в эти месяцы должно быть от 1 до 31 дня
				logger.info('Проверка на соответствие месяца и количества дней пройдена. Дата корректна')
				return True
			if month in [4, 6, 9, 11] and day in range(1,31):  # в эти месяцы должно быть от 1 до 30 дней
				logger.info('Проверка на соответствие месяца и количества дней пройдена. Дата корректна')
				return True
			if month == 2:  # если февраль
				if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:  # если високосный год
					if day in range(1,30):  # если день в пределах 1..29
						logger.info('Проверка на високосность года пройдена. Дата корректна')
						return True
					logger.info('Проверка на корректность даты не пройдена')
					return False
				elif day in range(1,29):   # если год не високосный и день в пределах 1..28
					logger.info('Проверка на високосность года пройдена. Дата корректна')
					return True
		logger.info('Проверка на корректность даты не пройдена')
		return False

if __name__ == '__main__':
	print(func(value))