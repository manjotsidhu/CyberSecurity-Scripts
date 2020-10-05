#
#  This script finds Psedu-Random numbers using Linear Congruential Method
#  https://www.eg.bucknell.edu/~xmeng/Course/CS6337/Note/master/node40.html
#  
#  Copyright (C) 2020-2021, Manjot Sidhu <manjot.techie@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  NOTE: This script is only meant for informational and educational purposes only.
# 

# a = multiplier
# x0 = seed
# c = increment
# m = modulus
def lcg(m, a, c, x):
	return ((a*x) + c) % m


def q1():
	print("Q1) X0 = 27, a = 17, c = 43, m = 100")
	x = 27
	a = 17
	c = 43
	m = 100

	q1_ans = []
	for i in range(1, 5):
		result = lcg(m, a, c, x)
		q1_ans.append(result)
		x = result

	print("Ans: ",q1_ans)


def q2():
	print("Q2) M = 5, a = 1, c = 16, x0 = 1")
	x = 1
	a = 1
	c = 16
	m = 5

	q2_ans = []
	for i in range(1, 5):
		result = lcg(m, a, c, x)
		q2_ans.append(result)
		x = result

	print("Ans: ",q2_ans)


def q3():
	print("Q3) M = 5, a = 0, c = 16, x0 = 1")
	x = 1
	a = 0
	c = 16
	m = 5

	q3_ans = []
	for i in range(1, 5):
		result = lcg(m, a, c, x)
		q3_ans.append(result)
		x = result

	print("Ans: ",q3_ans)


def main():
	q1()
	q2()
	q3()


main()