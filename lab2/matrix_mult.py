import argparse

#умножение
def get_paths():
	parser = argparse.ArgumentParser(description='Pascal triangle')
	parser.add_argument('read_path', metavar='read', type=str)
	parser.add_argument('write_path', metavar='write', type=str)
	args = parser.parse_args()
	return args.read_path, args.write_path


def create_matr(read_file: str):
	m1, m2 = [], []
	with open(read_file, 'r') as file:
		for line in file:
			if line == '\n':
				break
			tmp = map(int, line.split())
			m1.append(list(tmp))
		for line in file:
			tmp = map(int, line.split())
			m2.append(list(tmp))
	return m1, m2


def mtrxmult(m1: list, m2: list):
	a, b = len(m1), len(m1[0])
	c, d = len(m2), len(m2[0])
	if c != b:  # проверка размерностей
		print("Нельзя перемножить матрицы")
		return
	res = [[0]*d for i in range(a)]
	for i in range(a):
		for j in range(d):
			for k in range(b):
				res[i][j] += m1[i][k] * m2[k][j]
	return res


def print_matrix(write: str, m: list):
	with open(write, 'w') as f:
		for line in m:
			tmp = list(map(str, line))
			f.write(' '.join(tmp))
			f.write('\n')


if __name__ == "__main__":
	read, write = get_paths()
	mat1, mat2 = create_matr(read)
	result = mtrxmult(mat1, mat2)
	print_matrix(write, result)

# python matrix_mult.py read.txt write.txt
