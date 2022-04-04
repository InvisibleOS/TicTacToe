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

    O = []
    X = []

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
            # click += 1
            # if click % 2 == 0:
            #     symbol = " O "
            #     turn = "X"
            #     O.append(event)
            #     # print(O)
            #     # print("")
            # else:
            #     symbol = " X "
            #     turn = "O"
            #     X.append(event)
            #     # print(X)
            #     # print("")

            window.Element(event).update(chance, disabled=True)
            X.append(event)
            window.refresh()
            check = win_check(X=set(X), O=set(O), window=window)
            if check is False:

            # print(list(set(all_combos) - set(O) - set(X)))

                if len(list(set(all_combos) - set(O) - set(X))) != 0:
                    comp_choice = random.choice(list(set(all_combos) - set(O) - set(X)))
                    window.Element(comp_choice).update(" O ", disabled=True)
                    O.append(comp_choice)
                    window.refresh()
                    check = win_check(X=set(X), O=set(O), window=window)
                    # check = win_check(X=["a1", "b2", "c3"], O=["a2", "a3", "b3"], window=window)
                    # print(X)
                    # print(O)
                    # print("")

                else:
                    print("error")
                    check = win_check(X=set(X), O=set(O), window=window)
                    # check = win_check(X=["a1", "b2", "c3"], O=["a2", "a3", "b3"], window=window)
                    if check is False:
                        sg.popup("Game tied")
                    else:
                        sg.popup("O won the game!")






# def win_check(X, O, window):
#     print(f"{X}\n{O}")
#     combos=[
#         ["a1", "a2", "a3"],
#         ["b1", "b2", "b3"],
#         ["c1", "c2", "c3"],
#         ["a1", "b1", "c1"],
#         ["a2", "b2", "c2"],
#         ["a3", "b3", "c3"],
#         ["a1", "b2", "c3"],
#         ["a3", "b2", "c1"]
#     ]

    # for combo in combos:
    #     print("check 1")
    #     if all(item in X for item in combo):
    #         print("check 2a")
    #         for i in all_combos:
    #             window.Element(i).update(disabled=True)
    #         window.refresh()
    #         sg.popup("X won the game!")
    #         return True
    #     elif all(item in O for item in combo): # here      
    #         print("check 2b")      
    #         for i in all_combos:
    #             window.Element(i).update(disabled=True)
    #         window.refresh()
    #         sg.popup("O won the game!")
    #         return True
    # print("check c")
    # return False



def win_check(X: set[str], O: set[str], window: sg.Window):
    print(f"{X}\n{O}")
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
        print("check 1")
        if X.issuperset(combo):
            print("check 2a")
            for i in all_combos:
                window.Element(i).update(disabled=True)
            window.refresh()
            sg.popup("X won the game!")
            return True
        elif O.issuperset(combo): # here      
            print("check 2b")      
            for i in all_combos:
                window.Element(i).update(disabled=True)
            window.refresh()
            sg.popup("O won the game!")
            return True
        else:
            print("check c")

    return False


tictactoe_comp()
