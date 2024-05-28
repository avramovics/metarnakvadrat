
from .sinastry import synastry, synastry_houses,compatibility
from .position import prep_array_planets, prep_array_houses, display_houses, display_planets

#Check if user1 or user2 has did not specify exact time
def exact_time(user1, user2):
    if(user1['exact_time'] == False or user2['exact_time'] == False):
        return False
    return True


def extract_user_data(user):
    return (
        user["year"],
        user["month"],
        user["date"],
        user["local_time"],
        user["longi"],
        user["lati"],
        user["hours_difference"]
    )

async def get_compability(users):

    #Planets first_person_planets =
    first_person_planets = prep_array_planets(*extract_user_data(users[0]))
    second_person_planets = prep_array_planets(*extract_user_data(users[1]))
    first_person_houses = prep_array_houses(*extract_user_data(users[0]))
    second_person_houses = prep_array_houses(*extract_user_data(users[1]))
    return compatibility(synastry(first_person_planets, second_person_planets),
                   synastry_houses(first_person_planets, second_person_houses),
                   synastry_houses(second_person_planets, first_person_houses), 
                   exact_time(users[0], users[1])
           )
