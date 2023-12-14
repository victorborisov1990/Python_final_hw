import logging
import argparse
import sys


try:
	logging.basicConfig(filename='./logs/task2.log', encoding='utf-8', level=logging.INFO)
except FileNotFoundError as fn:
	logging.basicConfig(filename='spare2.log', encoding='utf-8', level=logging.INFO)
	logger = logging.getLogger(__name__)
	logger.warning(fn)
else:
	logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser(description='input two group of numbers "1,2,3,4..."')
parser.add_argument('ticket_list', type=str, help='current list to compare. 10 numbers separated with ","')
parser.add_argument('winner_list', type=str, help='winning list compared with anothers. 10 numbers separated with ","')

args = parser.parse_args()


try:
	list1 = [int(x) for x in args.ticket_list.split(',')]
except ValueError as e:
	logger.error(f'Ошибка 1го аргумента')
	sys.exit(1)
else:
	try:
		list2 = [int(x) for x in args.winner_list.split(',')]
	except ValueError as e:	
		logger.error(f'Ошибка 2го аргумента')
		sys.exit(2)

print(list1)
print(list2)

class LotteryGame():
	'''
	На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
	Первый список ваш лотерейный билет.
	Второй список содержит список чисел, которые выпали в лотерею.
	Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
	'''
	size = 10

	def __init__(self, list1: list, list2: list):
		'''
		в качестве параметров принимает 2 списка
		:param list1: 
		:param list2: 
		'''
		self.list1 = list1.copy()
		self.list2 = list2.copy()

	def compare_lists(self):
		'''
		сравнивать числа из вашего билета из list1 со списком выпавших чисел list2
		Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
		:return str: 
		'''
		if len(self.list1) == len(self.list1) == self.size:
			logger.info('Проверка на длинну последовательностей чисел пройдена')
			result = []
			count = 0
			for number in list1:
				try:
					if type(number) != int or number < 0:
						raise ValueError(number)
				except ValueError as e:
					logger.error(f'Ошибка. Ожидается целое положительное число, а не {e}')
					sys.exit(3)
				else:
					if number in list2 and number not in result: 
						result.append(number)
						count += 1
			logger.info('Сравнение последовательностей чисел прошло успешно')
			return f'Совпадающие числа: {result}\nКоличество совпадающих чисел:{count}'
		else:
			logger.info('Проверка на длинну последовательностей чисел не пройдена')
			sys.exit(4)
				
if __name__ == '__main__':
	# list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
	# list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

	game = LotteryGame(list1, list2)
	matching_numbers = game.compare_lists()
	print(matching_numbers)
	

# Пример выходных данных:
# Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
# Количество совпадающих чисел:7
	
# task2.py 1,2,3,4,5,6,7,8,9,10 3,7,13,0,5,11,22,13,2,9