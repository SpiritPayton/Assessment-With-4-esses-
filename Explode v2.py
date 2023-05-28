"""v2 of explode actually makes the explode button a function so that it can print the monster dictionary
 instead of simply just breaking the program"""
def explode():
    # Function to end the program and print the monster dictionary
    print(monster_dict)
    easygui.msgbox("Boom! The Monster Card collection exploded. Game over! Ur trash. 你没有朋友。")
    raise SystemExit

elif option == "Explode":
    explode()
