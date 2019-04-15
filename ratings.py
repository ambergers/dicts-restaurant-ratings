"""Restaurant rating lister."""


# put your code here
def get_ratings(file):
    with open(file) as ratings:

        restaurant_ratings = {}

        ## give the user choices
        while True:
            user_choice = input("""
Enter 1 to see all ratings in alphabetical order, 
      2 to add a new restaurant, 
      3 to quit: """
                                )
            while user_choice not in ('1', '2', '3'):
                user_choice = input("""
Sorry, that wasn't one of the choices. Please enter 
1 to see all ratings, 
2 to add a new restaurant, 
3 to quit: """
                                    )
            if user_choice == "3":
                break

            elif user_choice in ("1","2"):
                ## validate new score

                if user_choice == "2":
                    user_restaurant = input("Please enter a restaurant name: ")
                    user_rating = input("Please enter your 1-5 rating for that restaurant: ")

                    while True:
                        try:
                            user_rating_int = int(user_rating)
                            if user_rating_int not in range(1, 6):
                                user_rating = input("Out of range - Please enter a valid integer from 1-5: ")
                                continue
                            break
                        except ValueError:
                            user_rating = input("Please enter a valid integer from 1-5: ")
                ## not within another if statement because we want this code to run for both 1 and 2 inputs
                for line in ratings:
                    line = line.rstrip()
                    line = line.split(":")
                    restaurant = line[0]
                    rating = line[1]
                    restaurant_ratings[restaurant] = rating ## adds keys, values to dictionary
                if user_choice == '2':
                    restaurant_ratings[user_restaurant.capitalize()] = user_rating

            for item in sorted(restaurant_ratings.items()):
                #item[0] is restaurant name item[1] is its rating
                print(f"{item[0]} is rated at {item[1]}.")

    
get_ratings('scores.txt')