print(sum([{'A Y':4, 'A Z':8, 'A X':3, 'B X':1, 'B Y':5, 'B Z':9,'C Z':7, 'C X':2, 'C Y':6}[i] for i in open("input", "rt").read().split('\n')[:-1]]))