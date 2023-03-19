import random


def create_matr(read_file: str):
	m1 = []
	with open(read_file, 'r') as file:
		for line in file:
			tmp = map(int, line.split())
			m1.append(list(tmp))
	return m1


class Pupa:
	def __init__(self, name="Pupa"):
		self.name = name
		self.work_done = False
		self.balance = 0

	def take_salary(self, amount: int):
		self.balance += amount

	def do_work(self, file1: str, file2: str):
		print("Результат работы Пупы")
		m1 = create_matr(file1)
		m2 = create_matr(file2)
		a, b = len(m1), len(m1[0])  # размеры матриц: строки столбцы
		for i in range(a):
			for j in range(b):
				m1[i][j] += m2[i][j]
		for line in m1:
			print(*line)
		self.work_done = True


class Lupa:
	def __init__(self, name="Lupa"):
		self.name = name
		self.work_done = False
		self.balance = 0

	def take_salary(self, amount: int):
		self.balance += amount

	def do_work(self, file1: str, file2: str):
		print("Результат работы Лупы")
		m1 = create_matr(file1)
		m2 = create_matr(file2)
		a, b = len(m1), len(m1[0])  # размеры матриц: строки столбцы
		for i in range(a):
			for j in range(b):
				m1[i][j] -= m2[i][j]
		for line in m1:
			print(*line)
		self.work_done = True


class Accountant:
	@staticmethod
	def give_salary(worker):
		if worker.work_done:
			print(f"Работа сделана, вот ваша зарплата, {worker.name}!")
			worker.take_salary(random.randint(1, 10000))
		else:
			print("Дедлайн просрочен!!! Штраф 100 деняк")
			worker.take_salary(-100)


if __name__ == "__main__":
	print("Лупа и Пупа устроились на работу.")
	Lupa = Lupa("Лупа")
	Pupa = Pupa("Пупа")
	boss = Accountant()
	print("Проработали целый месяц, трудились не покладая рук.")
	print('Введите пути файлов для работы Лупы!')
	sum1 = input()
	sum2 = input()
	work4lupa = (sum1, sum2)
	print('Введите пути файлов для работы Пупы!')
	sub1 = input()
	sub2 = input()
	work4pupa = (sub1, sub2)
	Lupa.do_work(*work4lupa)
	print('В конце месяца Лупа и Пупа пошли получать зарплату.')
	boss.give_salary(Lupa)
	boss.give_salary(Pupa)
	print(f'Баланс Лупы {Lupa.balance} деняк.')
	print(f'Баланс Пупы {Pupa.balance} деняк.')
	print(
		'Но в этой компании в бухгалтерии работает профессионал, и никто ничего не перепутал, поэтому каждый получил'
		' свою зарплату!\nКонец :)'
	)
