"""same as v2 but this one makes the print look a whole lot cuter for printing
"""
def explode():
    # Function to end the program and print the monster dictionary
    print("Monster Dictionary:")
    for monster, details in monster_dict.items():
        details_str = "\n".join([f"{k}: {v}" for k, v in details.items()])
        print(f"- {monster}:")
        print(details_str)
    easygui.msgbox("Boom! The Monster Card collection exploded. Game over! Ur trash. 你没有朋友。")
    raise SystemExit
