"""Restaurant rating lister."""


# put your code here
def get_ratings(file):
    with open(file) as ratings:

        restaurant_ratings = {}

        for line in ratings:
            line = line.rstrip()
            line = line.split(":")
            restaurant = line[0]
            rating = line[1]
            restaurant_ratings[restaurant] = rating ## adds keys, values to dictionary

        for item in sorted(restaurant_ratings.items()):
            #item[0] is restaurant name item[1] is its rating
            print(f"{item[0]} is rated at {item[1]}.")

        # return sorted(restaurant_ratings)
get_ratings('scores.txt')