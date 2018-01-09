restaurants = {}


with open('scores.txt') as all_restaurants:
    for line in all_restaurants:
        line = line.rstrip()
        name, rating = tuple(line.split(':'))
        restaurants[name] = restaurants.get(name, 0) + int(rating)


def print_restaurants(restaurants):
    """ accepts a dictionary of restaurants along with ratings
        prints the restaurant name and ratings
    """

    #creates a sorted list of pairs (tuples) using items()

    ratings = sorted(restaurants.items())

    for name, rating in ratings:
        print "{} has a rating of {}.".format(name, rating)


def prompt_new_rating():
    """ Asks user for a new restaurant name and rating.
    """

    #stores both inputs in name and score
    name = raw_input("Please name the restaurant you would like to rate ?")
    score = raw_input("How would you rate the Restaurant?")
    return name, score


def is_valid(response, x, y):
    """Checks if response is between the input range of x and y.
    """

    if response.isdigit():
        response = int(response)
        return response < y and response > x


def update_rating():
    chosen_restaurant = raw_input("Which restaurant rating would you like to update ?")
    new_rating = raw_input("What is your new rating?")

    if is_valid(new_rating, 0, 6):
        restaurants[chosen_restaurant] = new_rating
        print_restaurants(restaurants)
    else:
        print "This is not a valid input. Please try again."
        update_rating()

def execute_response(response):
    if response == 1:
        name, score = prompt_new_rating()
        restaurants[name] = restaurants.get(name, 0) + int(score)
        print_restaurants(restaurants)
    if response == 2:
        print_restaurants(restaurants)
    if response == 3:
        print_restaurants(restaurants)
        update_rating()


while True:
    print "What would you like to do?"
    print "1. Rate a new restaurant"
    print "2. View current ratings"
    print "3. Update a current rating"
    print "4. Quit."

    response = raw_input('Your selection?')

    if is_valid(response, 0, 5):
        response = int(response)
        execute_response(response)

        if response == 4:
            print "Thanks for using RestaurantRater! See you next time"
            break
    else:
        print "That was not a valid response. Try again."
