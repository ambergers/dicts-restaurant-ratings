"""Restaurant rating lister."""


# put your code here
def get_ratings(file):
    with open(file) as ratings:

        restaurant_ratings = {}
        user_restaurant = input("Please enter a restaurant name: ")
        user_rating = input("Please enter your 1-5 rating for that restaurant: ")
        for line in ratings:
            line = line.rstrip()
            line = line.split(":")
            restaurant = line[0]
            rating = line[1]
            restaurant_ratings[restaurant] = rating ## adds keys, values to dictionary
        restaurant_ratings[user_restaurant.capitalize()] = user_rating

        for item in sorted(restaurant_ratings.items()):
            #item[0] is restaurant name item[1] is its rating
            print(f"{item[0]} is rated at {item[1]}.")

    
get_ratings('scores.txt')