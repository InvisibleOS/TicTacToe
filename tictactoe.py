import PySimpleGUI as sg
import random


sg.theme('DarkGrey12')


all_combos=["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]


# def tictactoe():
#     layout = [
#         [
#             sg.Text("X's turn", key="turn")
#         ],
#         [
#             sg.Button(" - ", key="a1"), sg.Button(" - ", key="a2"), sg.Button(" - ", key="a3", )
#         ],
#         [
#             sg.Button(" - ", key="b1"), sg.Button(" - ", key="b2"), sg.Button(" - ", key="b3")
#         ],
#         [
#             sg.Button(" - ", key="c1"), sg.Button(" - ", key="c2"), sg.Button(" - ", key="c3")
#         ],
#         [
#             sg.Button("New game")
#         ]
#     ]

#     O = []
#     X = []

#     window = sg.Window("TicTacToe", layout, element_justification="center")
#     click=0
#     while True:
#         event, values = window.read()
#         if event == sg.WINDOW_CLOSED:
#             break
#         elif event == "New game":
#             window.close()
#             tictactoe()
#         else:
#             click += 1
#             if click % 2 == 0:
#                 symbol = " O "
#                 turn = "X"
#                 O.append(event)
#                 # print(O)
#                 # print("")
#             else:
#                 symbol = " X "
#                 turn = "O"
#                 X.append(event)
#                 # print(X)
#                 # print("")

#             window.Element(event).update(symbol, disabled=True)
#             window.Element("turn").update(f"{turn}'s turn")
#             window.refresh()
#             check = win_check(X=X, O=O, window=window)
#             if click == 9:
#                 if check is False:
#                     sg.popup("Game tied")





def tictactoe_comp():
    chance = " X "
    layout = [
        [
            sg.Text("X's turn", key="turn")
        ],
        [
            sg.Button(" - ", key="a1"), sg.Button(" - ", key="a2"), sg.Button(" - ", key="a3", )
        ],
        [
            sg.Button(" - ", key="b1"), sg.Button(" - ", key="b2"), sg.Button(" - ", key="b3")
        ],
        [
            sg.Button(" - ", key="c1"), sg.Button(" - ", key="c2"), sg.Button(" - ", key="c3")
        ],
        [
            sg.Button("New game")
        ]
    ]

    O = set()
    X = set()

    window = sg.Window("TicTacToe", layout, element_justification="center")
    click=0
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        elif event == "New game":
            window.close()
            tictactoe_comp()

        else:
            window.Element(event).update(chance, disabled=True)
            X.add(event)
            window.refresh()
            if win_check(X, window):
                sg.popup("X won the game!")

            elif len(remaining := set(all_combos) - set(O) - set(X)) != 0:
                comp_choice = random.choice(list(remaining))
                window.Element(comp_choice).update(" O ", disabled=True)
                O.add(comp_choice)
                window.refresh()
                if win_check(O, window=window):
                    sg.popup("O won the game!")

            else:
                sg.popup("Game tied")


def win_check(tiles: set[str], window: sg.Window):
    print(f"{tiles}")
    combos=[
        {"a1", "a2", "a3"},
        {"b1", "b2", "b3"},
        {"c1", "c2", "c3"},
        {"a1", "b1", "c1"},
        {"a2", "b2", "c2"},
        {"a3", "b3", "c3"},
        {"a1", "b2", "c3"},
        {"a3", "b2", "c1"}
    ]

    for combo in combos:
        if tiles.issuperset(combo):
            for i in all_combos:
                window.Element(i).update(disabled=True)
            window.refresh()
            return True
    return False


tictactoe_comp()
