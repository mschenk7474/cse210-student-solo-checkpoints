import random

# TODO: Define the Hider class here
class Hider:
   def __init__(self):
       self.location = random.randint(1, 1000)
       self.distance = [0,0]

   def get_hint(self):
      """Gets a hint for the hunter.
         Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
      """
      hint = "I am going to sleep. zzzzzz"
      if self.distance[-1] == 0:
         hint = "(;.;) You found me!"
      elif self.distance[-1] < self.distance[-2]:
         hint = "(^.^) Getting colder!"
      elif self.distance[-1] > self.distance[-2]:
         hint = "(>.<) Getting warmer!"
      return hint

   def watch(self, location):
      """Watches the given location by keeping track of how far away it is.
        Args:
            self (Hider): An instance of Hider.
      """
      distance = abs(self.location - location)
      self.distance.append(distance)