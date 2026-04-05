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
        self.__frequencies = {}

    def process_file(self):
        try:
            Path.exists(self.__filepath)
            Path.open(self.__filepath)
            doc = Path.read_text(self.__filepath)
            table = str.maketrans("", "", string.punctuation)
            text = doc.translate(table)
            lower_text = text.lower()
            split_text = lower_text.split()
            print("split text:", split_text[:10])
            #for word in split_text:
                
        except FileNotFoundError:
            print("We don't got that text.")

    def print_report(self):
        return self.process_file()

analysis = WordAnalyzer("/home/mya_applesauce/Documents/the_prophecy_of_deltarune.txt")
print(analysis.print_report())

#if __name__ == "__main__":
    #analyst_list = []
    #for fname in ["moby_dick.txt", "typee.txt", "omoo.txt", "billy_budd.txt"]:
        #analyst = WordAnalyzer(fname)
        #analyst_list.append(analyst)
