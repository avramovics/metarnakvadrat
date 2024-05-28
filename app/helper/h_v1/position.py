import swisseph as swe
from datetime import datetime, timedelta
import json
from decimal import Decimal

planet_names = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
# Initialize the Swiss Ephemeris library
swe.set_ephe_path('/sweph/ephe')  # Path to ephemeris files



def planetary_position(julian_day_ET):

    # Define the flag for calculation options
    flag = swe.FLG_NONUT   # You can set specific calculation flags if needed
    # Format the output
    # Calculate the planetary positions
    planets = [swe.SUN, swe.MOON, swe.MERCURY, swe.VENUS, swe.MARS, swe.JUPITER, swe.SATURN, swe.URANUS, swe.NEPTUNE, swe.PLUTO]
    planets_output = []
   
    for planet, name in zip(planets, planet_names):
        # Call the swe_calc function to calculate the position of the celestial body
        #planets_output.append(f"{name} { swe.calc_ut(julian_day_ET, planet, flag)}")
        output = swe.calc_ut(julian_day_ET, planet, flag)

        planets_output +=   output

    return planets_output





def local_to_standard_time(year, month, date, local_time, hours_difference):
   

    # Convert the decimal number to integers for hours and minutes
    hours = int(local_time)
    minutes = int((local_time - hours) * 100)  # Extract the decimal part as minutes

    local_time = datetime(year, month, date, hours, minutes +1)

   
    # Define the time difference between local time (+1) and standard time (0)
    time_difference = timedelta(hours=hours_difference)

    # Convert the local time to standard time by subtracting the time difference
    standard_time = local_time - time_difference
    print(f"local_time123 {standard_time}")
     # Convert the decimal number to integers for hours and minutes
    hour = int(standard_time.strftime(" %H "))
    minute = int(standard_time.strftime(" %M "))  # Extract the decimal part as minutes
    Decimal(f"{hour}.{minute}")
  
    return (hour + minute / 60 + 0 / 3600)
 





def chart(year, month, date, local_time, longi, lati, hours_difference):

    #Use standard time to get correct julday 
    standard_time = local_to_standard_time(year, month, date, local_time, hours_difference)
    print(f"standard time {standard_time}")
    calendar = swe.GREG_CAL
    jd = swe.julday(year,month,date,standard_time, calendar)
    print(f"jd {jd}")

    hsys = bytes('P', encoding='ascii')

    cusps, ascmc = swe.houses_ex( jd, lati, longi, hsys, swe.FLG_NONUT )
    #ascmc[0] = Ascendant
    #ascmc[1] = MC
    #ascmc[2] = ARMC
    #ascmc[3] = Vertex
    #ascmc[4] = "equatorial ascendant"
    #ascmc[5] = "co-ascendant" (Walter Koch)
    #ascmc[6] = "co-ascendant" (Michael Munkasey)
    #ascmc[7] = "polar ascendant" (M. Munkasey)
    # Calculate UTC time using swisseph.utc()
    
    D = {'Houses': cusps , 
         'Planets': planetary_position(jd), 
         'ascmc':ascmc
         } 
    return json.dumps(D)





def prep_array_houses(year, month, date, local_time, longi, lati, hours_difference):
    positionData = chart(year, 
                  month, 
                  date, 
                  local_time,
                  longi, 
                  lati, 
                  hours_difference
                  )
    housesArrays = []
    array = []
    data = json.loads(positionData)
    houses = data["Houses"]
    if isinstance(houses, list): 
        i=1
        for  hposition in houses:
            housesArrays.append(hposition)
                
        for  house in housesArrays:
            array.append({'house':i, 'position': house }) #+= f"<div>{i}->{house}</div>"
            i+=1


    return array



def calculate_Descendant(asc):
    if(asc + 180) > 360:
        return (asc + 180) - 360
    else:
        return asc + 180



def prep_array_planets(year, month, date, local_time, longi, lati, hours_difference):
    
    positionData = chart(year, 
                  month, 
                  date, 
                  local_time,
                  longi, 
                  lati, 
                  hours_difference
                  )
    planetsArrays = []

    array = []
    
    # Parse the JSON string
    data = json.loads(positionData)

    # Extract the first element from the "Planets" list
    planets = data["Planets"]

    # Print the result

  
    if isinstance(planets, list): 

        for  position in planets:
            if isinstance(position, list):
                planetsArrays.append(position[0])
        for  planet, name in zip(planetsArrays, planet_names):
                array.append({"planet":name, "degre": planet})


    array.append({"planet":"Ascendant", "degre": data['ascmc'][0]})
    array.append({"planet":"Descendant", "degre": calculate_Descendant(data['ascmc'][0])})
    array.append({"planet":"MC", "degre": data['ascmc'][1]})
    array.append({"planet":"Vertex", "degre": data['ascmc'][3]})
    
    #ascmc[0] = Ascendant
    #ascmc[1] = MC
    #ascmc[2] = ARMC
    #ascmc[3] = Vertex
    #ascmc[4] = "equatorial ascendant"
    #ascmc[5] = "co-ascendant" (Walter Koch)
    #ascmc[6] = "co-ascendant" (Michael Munkasey)
    #ascmc[7] = "polar ascendant" (M. Munkasey)

    return  array




def display_planets(year, month, date, local_time, longi, lati, hours_difference):
    
    positionData = chart(year, 
                  month, 
                  date, 
                  local_time,
                  longi, 
                  lati, 
                  hours_difference
                  )
    planetsArrays = []
    planetsString = ""
    # Parse the JSON string
    data = json.loads(positionData)

    # Extract the first element from the "Planets" list
    planets = data["Planets"]

    # Print the result

  
    if isinstance(planets, list): 
        
        for  position in planets:
            if isinstance(position, list):
                planetsArrays.append(position[0])
                
        for  planet, name in zip(planetsArrays, planet_names):
                planetsString += f"<div>{name}->{planet}</div>"
    planetsString += f"<div>Ascendant->{data['ascmc'][0]}</div>"            
    planetsString += f"<div>MC->{data['ascmc'][1]}</div>"  
    planetsString += f"<div>Vertex->{data['ascmc'][3]}</div>"      

    return f"{planetsString}"






def display_houses(year, month, date, local_time, longi, lati, hours_difference):
    
    positionData = chart(year, 
                  month, 
                  date, 
                  local_time,
                  longi, 
                  lati, 
                  hours_difference
                  )
    housesArrays = []
    housesString = ""
    # Parse the JSON string
    data = json.loads(positionData)

    # Extract the first element from the "Planets" list
    houses = data["Houses"]
    # Print the result

  
    if isinstance(houses, list): 
        i=1
        for  hposition in houses:
            housesArrays.append(hposition)
                
        for  house in housesArrays:
            housesString += f"<div>{i}->{house}</div>"
            i+=1
    
    
    return f"{housesString}"






                      