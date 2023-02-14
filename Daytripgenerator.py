#  As a developer, I want to make at least three commits with descriptive messages
 
#   As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 

# As a user, I want a destination to be randomly selected for my day trip. 

# : As a user, I want a restaurant to be randomly selected for my day trip

#  As a user, I want a mode of transportation to be randomly selected for my day trip. 

#  As a user, I want a form of entertainment to be randomly selected for my day trip.

#  As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation,

#  and/or form of entertainment if I don’t like one or more of those thing


import random
print("welcome to trip generator here are some options we have today")

destination= ['california','texas','london','china']
restaurant= ['nobu','steakhouse','sketch','mott']
transportation= ['car','boat','plane','horseback']
entertainment = ['moviehouse','concert','skatingring','arcade']


 
def run_trip_generator(list_of_plans):
    selected_plans= random.choice(list_of_plans)
    return selected_plans
destinations=run_trip_generator(destination)
print("destionation:",destinations)
restaurants=run_trip_generator(restaurant)
print("restaurant:",restaurants)
transportations=run_trip_generator(transportation)
print('transportation:',transportations)
entertainments=run_trip_generator(entertainment)
print('entertainments:',entertainments)



def determine_satisfaction():
    run_trip_generator()
while True:    

    User_reponse= 'yes' 
    User_reponse2='no'  
    valid_trip_plans = input('Are you satistfied with this trip? yes or no ')
        
    
    if valid_trip_plans == User_reponse:
        print("Then have a great trip")
        break
    elif valid_trip_plans == User_reponse2:
        print('lets try another trip choice')
        destinations=run_trip_generator(destination)
        print("destionation:",destinations)
        restaurants=run_trip_generator(restaurant)
        print("restaurant:",restaurants)
        transportations=run_trip_generator(transportation)
        print('transportation:',transportations)
        entertainments=run_trip_generator(entertainment)
        print('entertainments:',entertainments)
    else:
        break
