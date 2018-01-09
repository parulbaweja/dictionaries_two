import sys

def new_rating():
    """ Asks user for a new restaurant name and rating.
    """

    #stores both inputs in name and score
    name = raw_input("Please name the restaurant you would like to rate ?")
    score = raw_input("how would you rate the Restaurant?")
    return name, score


def organize_restaurants(restaurants):
    """ accepts a dictionary of restaurants along with ratings
        prints the restaurant name and ratings
    """

    #creates a sorted list of pairs (tuples) using items()
    ratings = sorted(restaurants.items())

    for restaurant in ratings:
        print "{} has a rating of {}.".format(restaurant[0],restaurant[1])



def get_ratings(filename):
    """Creates a dictionary from a file of restaurants and ratings.
        Prints the restaurants and ratings alphabetically.
        Asks user for input using new_rating() function.
    """

    restaurants = {}

    with open(filename) as all_restaurants:
        for line in all_restaurants:
            line = line.rstrip()
            name, rating = tuple(line.split(':'))
            restaurants[name] = restaurants.get(name, 0) + int(rating)

    organize_restaurants(restaurants)
    
    response = raw_input("Would you like to rate a new restaurant? Y/N")

    if response == 'Y':
        name, score = new_rating()
        restaurants[name] = restaurants.get(name, 0) + int(score)

        organize_restaurants(restaurants)

get_ratings(sys.argv[1])

