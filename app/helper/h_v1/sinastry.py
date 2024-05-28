
from ...model.aspect_schema import sexuality, toxic, marriage, friendship

orb_degrese = 8


def between(distance, orb):

    if abs(orb - distance) < orb_degrese:
       print(distance - orb)
       return  distance - orb
    return 100

def check_for_aspect(a, b, orbs):
    result = {}
    for orb in orbs:
        if between(abs(a - b), orb['degre']) <= orb_degrese:
            result  = {'aspect_name': orb['aspect_name'], 'orb': between(abs(a - b), orb['degre']) }
    return result if result else {}


def get_house(house, planets):
    planets_in_synastry_house = []
    for planet in planets:
        i = 0
        while i < 12:
            prev_house = i  # house to check
            next_house = i + 1 if i < 11 else 0  # if prev house is on the 12th house then use 1 as next_house
            if (house[prev_house]['position'] < house[next_house]['position'] and
                    (planet['degre'] > house[prev_house]['position'] and
                         planet['degre'] < house[next_house]['position'])):
                planets_in_synastry_house.append({'house': i+1, 'planet': planet['planet']})
            elif (house[prev_house]['position'] > house[next_house]['position'] and ( planet['degre'] > house[prev_house]['position'] or planet['degre'] < house[next_house]['position'])):
                 planets_in_synastry_house.append({'house': i+1, 'planet': planet['planet']})
            i += 1
    return planets_in_synastry_house

def synastry(planets_first, planets_second):
   
    orbs = [
                {"aspect_name": 'Conjunction', 'degre': 0},
                {"aspect_name": 'Sextile', 'degre': 60},
                {"aspect_name": 'Sextile', 'degre':300},
                {"aspect_name": 'Square', 'degre':90},
                {"aspect_name": 'Square', 'degre':270},
                {"aspect_name": 'Trine', 'degre':120},
                {"aspect_name": 'Trine', 'degre':240},
                {"aspect_name": 'Opposition', 'degre':180},
            ]


    result = []

    for first in planets_first:
        for second in planets_second:
            aspect_array = check_for_aspect(first['degre'], second['degre'], orbs)

            if aspect_array:

                result.append({
                    'first_person': first['planet'],
                    'aspect': aspect_array['aspect_name'],
                    'second_person': second['planet'],
                    'orbs': abs(aspect_array['orb'])
                })
    return result


def synastry_houses(first_person_planets, second_person_houses):
    return get_house( second_person_houses , first_person_planets)



def compatibility_planets_in_houses(synastry_houses, schema_to_check):
    descArray= []
    aspectArray= []

    value = 0
    for planet in synastry_houses:
        for pair in schema_to_check:
            #if this is an planet house aspect
            if (pair["algo"] == "position") : 
                #if planet maches first position and house maches second position increment
                if (planet["planet"] == pair["Planets/cusps"][0]
                     and planet["house"] == pair["Planets/cusps"][1]):
                    descArray.append(pair["Description"])
                    aspectArray.append(pair["Planets/cusps"])
                    value += 1 
    return {"value":value, "desc": descArray, "aspects": aspectArray}



def calculate_compatibility(synastry, synastry_houses_fp, synastry_houses_sp, exact_time, schema_to_check):

    arrayOfAspects = []
    arrayOfDescription = []
    value = 0
    for aspect in synastry:
        for pair in schema_to_check:
            if(pair['algo'] == 'aspect' and  aspect["aspect"] in pair["Aspects"] ): 
                if (aspect['first_person'] == pair["Planets/cusps"][0] 
                    and aspect['second_person'] == pair["Planets/cusps"][1]
                    ) or (aspect['first_person'] == pair["Planets/cusps"][1] 
                    and aspect['second_person'] == pair["Planets/cusps"][0]):
                    if pair["exact_time"] == False or (pair["exact_time"] == True and exact_time == True):   
                        value +=1
                        arrayOfAspects.append(aspect)
                        arrayOfDescription.append(pair["Description"])

    if pair["exact_time"] == False or (pair["exact_time"] == True and exact_time == True):             
        v1 = compatibility_planets_in_houses(synastry_houses_fp, schema_to_check)
        arrayOfDescription.append(v1["desc"])
        value += v1["value"]
        arrayOfAspects += v1["aspects"]
        v2 = compatibility_planets_in_houses(synastry_houses_sp, schema_to_check)
        value += v2["value"]
        arrayOfDescription.append(v2["desc"])
        arrayOfAspects += v2["aspects"]

    return {"aspects":arrayOfAspects, "count":value, "desc": arrayOfDescription}



def compatibility(synastry,synastry_houses_fp, synastry_houses_sp, exact_time):
    result = {"sexualcompability":calculate_compatibility(synastry, synastry_houses_fp, synastry_houses_sp, exact_time, sexuality),
              "toxicity":calculate_compatibility(synastry, synastry_houses_fp, synastry_houses_sp, exact_time, toxic),
              "marriage":calculate_compatibility(synastry, synastry_houses_fp, synastry_houses_sp, exact_time, marriage),
              "friendship":calculate_compatibility(synastry, synastry_houses_fp, synastry_houses_sp, exact_time, friendship)

     }
    return result 









