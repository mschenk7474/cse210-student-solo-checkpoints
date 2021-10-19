import random

# TODO: Define the Board class here
class Board():
   def __init__(self):
       self._piles = []
       self._prepare()

   def to_string(self):
      """
      Converts the board to a string that the console can print
      out.
      """
      board = "\n--------------------"
      for pile, stones in enumerate(self._piles):
         board += (f"\n{pile}: "+ "O " * stones)
      board += "\n--------------------"

      return board
   def apply(self, move):
      """
      Applies the move that the user chooses to the board
      """
      pile = move.get_pile()
      stones = move.get_stones()
      self._piles[pile] = max(0, self._piles[pile] - stones)

   def is_empty(self):
      """
      Returns a boolean that checks if the board is empty
      """
      empty = [0] * len(self._piles)
      return self._piles == empty
      
   def _prepare(self):
      piles = random.randint(2, 5)
      for n in range(piles):
         stones = random.randint(1, 9)
         self._piles.append(stones)
