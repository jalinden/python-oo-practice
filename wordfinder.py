"""Word Finder: finds random words from a dictionary."""
import random
class WordFinder:
    
    def __init__(self,path):
        words = open(path)
        self.word_list = self.read_file(words)
        print (f"{len(self.word_list)} words read")
        

    def read_file(self,words):
        return [word.strip() for word in words]

    def random(self):
        return random.choice(self.word_list)



class SpecialWordFinder(WordFinder):
    def read_file(self,words):
         return [word.strip() for word in words
                if word.strip() and not word.startswith("#")]
        
 


