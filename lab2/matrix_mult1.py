from matrix_mult import get_paths, create_matr, print_matrix

#свертка
def matrix_conv(m1: list, m2: list):
	a, b = len(m1), len(m1[0])  
	c, d = len(m2), len(m2[0])
	res = [[0]*(b-d+1) for i in range(a-c+1)]
	for i in range(a-c+1):
		for j in range(b-d+1):
			tmp2 = 0
			for u in range(c):
				tmp1 = 0
				for v in range(d):
					tmp1 += m1[i+u][j+v] * m2[u][v]
				tmp2 += tmp1
			res[i][j] = tmp2
	return res


if __name__ == "__main__":
	read, write = get_paths()
	mat1, mat2 = create_matr(read)
	result = matrix_conv(mat1, mat2)
	print_matrix(write, result)

# python matrix_mult1.py read1.txt write1.txt
