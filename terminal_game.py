"""Grasshopper - Terminal Game Turn Function.

Best practices Baaart & others 

def do_turn():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()
"""


def do_turn():
    print("Your adventure game begins here, roll your dice to see where you're going!")
    roll_dice()
    print("Let us get on the move!")
    move()
    print("Now it is time for some combat!")
    combat()
    print("You need money for that!")
    get_coins()
    print("You need more health for that!")
    buy_health()
    print("Let us see where your adventure took you.")
    print_status()
    print("Good job! You went on an awesome adventure!")