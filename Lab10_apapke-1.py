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
        if choice == "5":
            active = False

main()