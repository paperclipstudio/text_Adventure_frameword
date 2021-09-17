# Class to hold an option for a state
class Option:
    def __init__(self, text, action, predicate):
          self.text = text
          self.action = action
          self.predicate = predicate

    # Takes in your current stats and returns if this is an option 
    def vaild(self, stats):
           return self.predicate(stats) 



    