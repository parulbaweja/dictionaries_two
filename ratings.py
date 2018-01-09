def get_ratings(filename):
    """Restaurant rating lister."""


    restaurants = {}

    with open(filename) as all_restaurants:
        for line in all_restaurants:
            line = line.rstrip()
            name, rating = tuple(line.split(':'))
            restaurants[name] = restaurants.get(name, 0) + int(rating)

    ratings = sorted(restaurants.items())

    for restaurant in ratings:
        print "{} has a rating of {}.".format(restaurant[0],restaurant[1])

get_ratings('scores.txt')

