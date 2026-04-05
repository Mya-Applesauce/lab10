"""
WordAnalyzer
Ari Papke
word analyzer class
04/04/26
"""

from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = Path(filepath)

    def process_file(self):
        try:
            Path.exists(self.__filepath)
            doc = Path.open(self.__filepath)
            table = str.maketrans(string.punctuation)
            text = doc.translate(table)
            text.lower()
            text.split()
            for word in text:
                
        except FileNotFoundError:
            print("We don't got that text.")

    #def print_report(self):

#analysis = WordAnalyzer("the_prophecy_of_deltarune.txt")
#print(analysis.process_file)

#if __name__ == "__main__":
    #analyst_list = []
    #for fname in ["moby_dick.txt", "typee.txt", "omoo.txt", "billy_budd.txt"]:
        #analyst = WordAnalyzer(fname)
        #analyst_list.append(analyst)
