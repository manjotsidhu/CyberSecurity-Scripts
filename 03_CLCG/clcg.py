#
#  This script finds Psedu-Random numbers using Combined Linear Congruential Method
#  http://www.new-npac.org/projects/cdroms/cewes-1999-06-vol1/cps615course/csematerials/applications/mc/montecarlo/node107.html
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
	print("Q1) X0 = 27 X1 = 30, a1 = 17, a2 = 17, c1=c2= 43, m1=m2 = 100")
	
	R = []

	m1 = 100
	a1 = 17
	m2 = 100
	a2 = 17
	c1 = 43
	c2 = 43

	X0 = 27
	X1 = 30

	for i in range(0, 6):

	    X0 = lcg(m1,a1,c1,X0)
	    X1 = lcg(m2,a2,c2,X1)

	    X = (X0 - X1) % (m1 - 1)

	    if (X > 0):
	       R.append(X / m1)
	    elif (X < 0):
	       R.append((X / m1) + 1)
	    elif (X == 0):
	       R.append((m1 - 1) / m1)

	print("Ans: ",R,'\n')


def q2():
	print("Q2) m1=m2 = 5, a1 = 1, a2=5, c1=c2 = 16, x0 = 1, x1 = 2")
	R = []

	m1 = 5
	a1 = 1
	m2 = 5
	a2 = 5
	c1 = 16
	c2 = 16

	X0 = 1
	X1 = 2

	for i in range(0, 6):

	    X0 = lcg(m1,a1,c1,X0)
	    X1 = lcg(m2,a2,c2,X1)

	    X = (X0 - X1) % (m1 - 1)

	    if (X > 0):
	       R.append(X / m1)
	    elif (X < 0):
	       R.append((X / m1) + 1)
	    elif (X == 0):
	       R.append((m1 - 1) / m1)

	print("Ans: ",R, '\n')


def q3():
	print("Q3) M1=M2 = 15, a1 = 0, a2=1, c1=c2 = 16, x0 = 1, x1=2")
	R = []

	m1 = 15
	a1 = 0
	m2 = 15
	a2 = 1
	c1 = 16
	c2 = 16

	X0 = 1
	X1 = 2

	for i in range(0, 6):

	    X0 = lcg(m1,a1,c1,X0)
	    X1 = lcg(m2,a2,c2,X1)

	    X = (X0 - X1) % (m1 - 1)

	    if (X > 0):
	       R.append(X / m1)
	    elif (X < 0):
	       R.append((X / m1) + 1)
	    elif (X == 0):
	       R.append((m1 - 1) / m1)

	print("Ans: ",R)


def main():
	q1()
	q2()
	q3()


main()