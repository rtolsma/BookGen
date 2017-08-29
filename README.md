# BookGen

This is a Python script used to help the process of accessing free educational books online.

Simply enter a title or ISBN number as an argument and the program will download the book to your local directory if available. Please only use this for legal purposes.

## Command Line Arguments

#### --title, -t
Pass in a string to use as the search keyword i.e python main.py --title "Of Mice and Men"

#### --isbn, -i
Dictates whether the program should search based on the book ISBN versus the title. ISBN is more accurate but may not always be available

#### --path, -p
Takes in a string path to download the file to. i.e python main.py --path "/home/user/Desktop/" -t "Intelligent Investor"

#### --auto, -a
Dicates whether the program auto chooses the first listing or instead asks users for choices.
