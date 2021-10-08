import Scrabble_Methods
import pandas as pd

print("Welcome to Scrabble!")

players = {}
i = 1
bool = True

while(bool):
    print("(Type Exit to Exit.)")
    user_input = Scrabble_Methods.user_input(input("Spieler {}:".format(i)))
    if "Exit" in user_input:
        df = pd.DataFrame.from_dict(players)
        print("Folgende Spieler spielen mit: ")
        print(df)
        bool = False
    else:
        players[user_input] = [""]
        print("Der Spieler {} wurde hinzugefügt.".format(user_input))
    i += 1

df[input("PlayerName: ")].update(Scrabble_Methods.score_word("Help"))
Scrabble_Methods.total_points(players)


