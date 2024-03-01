"""
Task 16 - Imran Bhatti
Program to calculate holiday cost by creating user defined functions
"""
############### Start Code ##########################
# global variables for cost calculation

# hotel rate per night
HOTEL_RATE = 45
# car rental daily rate
CAR_RENTAL_RATE = 32
# Paris flight cost
PARIS_COST = 200
# London flight cost
LONDON_COST = 150
# Istanbul flight cost
ISTANBUL_COST = 300
# Madrid flight cost
MADRID_COST = 250

def hotel_cost(num_of_nights):
    """ function to define total cost of hotel stay """
    hotel_stay_cost= num_of_nights * HOTEL_RATE
    return hotel_stay_cost

def car_rental(rent_days):
    """ function to define total cost of car rental"""
    car_rental_cost = rent_days * CAR_RENTAL_RATE
    return car_rental_cost

def plane_cost(flight):
    """ function to assign flight cost for city user entered """
    if flight == 'par':   # par for paris
        return PARIS_COST
    elif flight == 'lon': # lon for london
        return LONDON_COST
    elif flight == 'ist': # ist for istanbul
        return ISTANBUL_COST
    elif flight == 'mad': # mad for madrid
        return MADRID_COST
    else:
    # print error message
        raise ValueError()

# holiday_cost variables prefixed with 'f_' due to duplicate name
# of parameters in task otherwise gives pylint error
def holiday_cost (f_hotel_cost, f_car_rental, f_plane_cost):
    """function to calculate the total holiday cost"""
    total_holiday_cost = f_hotel_cost + f_car_rental + f_plane_cost
    return total_holiday_cost

def options():
    """ function for displaying the choice of holiday city"""
    print()
    print("City holiday options:")
    print("Enter Par if you would like to travel to Paris.")
    print("Enter Lon if you would like to travel to London.")
    print("Enter Mad if you would like to travel to Madrid.")
    print("Enter Ist if you would like to travel to Istanbul.")

def city (city_letter):
    """ function to output city name"""
    if city_letter == 'par':   # par for Paris
        return "Paris"
    elif city_letter == 'lon': # lon for London
        return "London"
    elif city_letter == 'ist': # ist for Istanbul
        return "Istanbul"
    elif city_letter == 'mad': # mad for Madrid
        return "Madrid"
    else:
    # print error message
        raise ValueError("Valid city not entered")
try:
    # output menu
    options()
    # obtain city from user and convert to lower case
    city_flight = input("Enter city name from above: ").lower()
    # calculate flight cost
    FLIGHT_COST = plane_cost(flight=city_flight)
    # assign city name
    CITY_NAME = city(city_flight)
    # input hotel nights
    num_nights = int(input("Enter number of nights you want a hotel for: "))
    # input car rental days
    car_rental_days = int(input("Enter number of days for car rental: "))
    while True:
        if num_nights < car_rental_days:
            # warning message if car_rental_days greater than holiday length
            print("WARNING: The car rental days is greater than the ", end="")
            print("holiday duration")
            car_rental_days = int(input("Enter number of days for car rental: "))
        else:
            break

    # calculate car cost
    CAR_COST = car_rental(car_rental_days)
    # calculate hotel cost
    HOTEL_TOTAL_COST = hotel_cost(num_of_nights=num_nights)
    # calculate total holiday cost
    TOTAL_HOLIDAY_COST = holiday_cost(HOTEL_TOTAL_COST,
                                      CAR_COST,
                                      FLIGHT_COST)
    # output blank line
    print()
    # print output message confirming total holiday cost and breakdown
    print(f"Total cost of your holiday is £{TOTAL_HOLIDAY_COST}.")
    print(f"If you visit {CITY_NAME} your flight cost is £{FLIGHT_COST}.")
    print(f"For a hotel for {num_nights} night(s), the hotel cost",end="")
    print(f" is £{HOTEL_TOTAL_COST}.\nIf you rent a car for ",end="")
    print(f"{car_rental_days} day(s), your car rental is £{CAR_COST}.")
except ValueError:
    print("ERROR: You have entered an invalid value.")
########################## End Code ########################################
