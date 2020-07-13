"""
Create a program that prints out every line to the song "99 bottles of beer on the wall."
Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
lyrics at http://www.99-bottles-of-beer.net/lyrics.html
"""

bottle = 100  # number of bottles of beer
bottles = bottle - 1  # set a variable for when bottles equals zero
for i in range(bottle):
    bottle -= 1  # loops in decreasing order
    bottle_left = bottle - 1  # gives  the remaining number of beer bottles
    if bottle > 2:  # we set 2 so we can get the singular word for the remainder 1
        print(
            f"{bottle} bottles of beer on the wall, {bottle} bottles of beer. Take one down and pass it around,"
            f" {bottle_left} bottles of beer "
            "on the wall.")
    elif bottle == 2:
        print(
            f"{bottle} bottles of beer on the wall, {bottle} bottles of beer. Take one down and pass it around,"
            f" {bottle_left} bottle of beer "
            "on the wall.")
    elif bottle == 1:  # so we can set "no more" instead of 0  for remainder
        print(f"{bottle} bottle of beer on the wall, {bottle} bottle of beer. Take one down and pass it around,"
              f" no more bottles of "
              "beer on the wall.")
    else:
        print(f"No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, "
              f"{bottles} bottles of beer on the wall.")  # we set the remaining number of bottles back to 99
