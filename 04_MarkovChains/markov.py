"""
  This python script builds Markov Chain
  
  Copyright (C) 2020-2021, Manjot Sidhu <manjot.techie@gmail.com>

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.

  NOTE: This script is only meant for informational and educational purposes only.
"""
import numpy as np

class MarkovChain(object):
	def __init__(self, str):
		self.keys = list(set(str))
		self.keys.sort()
		l = len(self.keys)

		self.tpm = [ [0] * l for _ in range(l)]
		for i in range(0, len(str)-1):
			key_a = self.keys.index(str[i])
			key_b = self.keys.index(str[i+1])

			self.tpm[key_a][key_b] = self.tpm[key_a][key_b] + 1


		for i in range(0, len(self.keys)):
			s = sum(self.tpm[i])

			for j in range(0, len(self.keys)):
				self.tpm[i][j] = self.tpm[i][j] / s


	def next_state(self, current_state, show=False):
		next_state = np.random.choice(self.keys, p=self.tpm[self.keys.index(current_state)])

		if show:
			print(f'{current_state} -> {next_state}')

		return next_state


	def generate_states(self, current_state, no=5, show=True):
		states = []

		for i in range(0, no):
			current_state = self.next_state(current_state)
			states.append(current_state)

		if show:
			print(f'{current_state}', end='')
			for state in states:
				print(f' -> {state}', end='')
			print()

		return states


	def print_tpm(self):
		print('\nTransition Probability Matrix')
		
		print(f'   ', end='')
		for key in self.keys:
			print(f' {key} ', end='')

		print('\n  ', end='')
		print('-'*len(self.keys)*3)

		i_i = 0
		for i in self.tpm:

			print(f'{self.keys[i_i]} |', end='')
			i_i = i_i + 1

			for j in i:
				print(f' {j} ', end='')

			print('|', end='')

			print()

		print('  ', end='')
		print('-'*len(self.keys)*3)


mc = MarkovChain("abcabc")
mc.print_tpm()
mc.next_state("c", show=True)
mc.generate_states("a", show=True, no=10)