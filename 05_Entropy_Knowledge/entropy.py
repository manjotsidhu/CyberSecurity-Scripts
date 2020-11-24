"""
  This python script demonstrates Entropy.
  
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
import math

class bucket(object):

  def __init__(self):
    self.items = {}


  def insert_balls(self, ball, numbers = 1):
    if ball in self.items:
      self.items[ball] = self.items[ball] + numbers
    else:
      self.items[ball] = numbers


  def entropy(self):
    entropy = 0

    total_balls = 0
    for key in self.items.keys():
      total_balls = total_balls + self.items[key]

    for key in self.items.keys():
      for i in range(self.items[key]):
        p = self.items[key] / total_balls
        entropy = entropy - math.log2(p)

    return entropy / total_balls


b = bucket()
b.insert_balls("Black", 4)
b.insert_balls("Blue", 6)
b.insert_balls("Red", 1)
b.insert_balls("Green", 1)

print(f'Entropy: {round(b.entropy(), 4)}')