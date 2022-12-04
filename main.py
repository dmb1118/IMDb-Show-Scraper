import random
from bs4 import BeautifulSoup
import requests


def rng(num):
    return random.randint(1, num)


def start_program(num_shows):
    # Initializing
    url = 'https://www.imdb.com/chart/toptv/'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")

    shows = bs.select('td.titleColumn')
    title_list = []
    # Adds each show to a list
    for index in range(0, len(shows)):
        movie_str = shows[index].get_text()
        movie = (' '.join(movie_str.split()).replace('.', ''))
        movie_title = movie[len(str(index)) + 1:-7]
        title_list.append(movie_title)

    # Prints out the number of shows requested and removes them from the list to prevent repeats
    for i in range(0, num_shows):
        ran_num = rng(len(title_list)) - 1
        rec_show = title_list[ran_num]
        print(f'{i + 1}. {rec_show}')
        title_list.pop(ran_num)


if __name__ == '__main__':
    loop = True
    choice = 0
    while loop:  # Prevents invalid entries
        try:
            choice = int(input("How many recommendations would you like, 1 - 250? "))
        except ValueError as err:
            pass
        except TypeError as err:
            pass
        if 1 <= choice <= 250:
            loop = False
        else:
            print("Please enter a number between 1 and 250.")
    start_program(choice)
