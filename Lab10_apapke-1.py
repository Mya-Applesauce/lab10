"""
Lab 10
Ari Papke
word count project
04/05/26
"""

from wordanalyzer import WordAnalyzer

def main():
    active = True
    while active:
        print(f"~~~ Word Counter ~~~")
        print(f"1. Dracula\n2. Antigone (R. C. Jebb translation)\n3. I Have No Mouth and I Must Scream\n4. The Prophecy\n5. Quit")
        choice = input(f"Select a text to analyze! (1-5) ")
        if choice == "1":
            analysis = WordAnalyzer("/home/mya_applesauce/Documents/dracula.txt")
            analysis.process_file()
            analysis.print_report()
            print("")
        elif choice == "2":
            analysis = WordAnalyzer("/home/mya_applesauce/Documents/antigone.txt")
            analysis.process_file()
            analysis.print_report()
            print("")
        elif choice == "3":
            analysis = WordAnalyzer("/home/mya_applesauce/Documents/ihnmaims.txt")
            analysis.process_file()
            analysis.print_report()
            print("")
        elif choice == "4":
            analysis = WordAnalyzer("/home/mya_applesauce/Documents/the_prophecy_of_deltarune.txt")
            analysis.process_file()
            analysis.print_report()
            print("")
        elif choice == "5":
            print("bye!")
            active = False
        else:
            print("we don't got that one.\n")

main()