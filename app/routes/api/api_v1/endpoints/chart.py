# Route definitions
from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
import datetime

from .....helper.h_v1.sinastry import synastry, synastry_houses,compatibility

from .....model.model import User
from .....db.db import get_db
#from .....model.users import Users

router = APIRouter()





@router.get("/" )
async def get_items(db = Depends(get_db)):

    #year = 1983         # Define your Birth year
    #month = 10          # Define your Birth month
    #date = 5            # Define your Birth day
    #local_time = 23.30  # Define your local time
    #longi = 18.063326
    #lati = 59.300866
    #hours_difference = 1  # Replace with the number of hours difference
    first_person_planets = display_planets(1989, 8, 15, 2.4,  18.063326, 59.300866, 2)
    second_person_planets = display_planets(1989, 4, 27, 21.38, 18.063326, 59.300866, 2)
    first_person_houses = display_houses(1989, 8, 15, 2.4,  18.063326, 59.300866, 2)
    second_person_houses = display_houses(1989, 4, 27, 21.38, 18.063326, 59.300866, 2)

    html_content = f"""
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
                 <h2> First person </h2>
                 </div>{first_person_planets}</div>
                 <h2> Second person </h2>
                 <div>{second_person_planets}</div>

                <h2> First person </h2>
                 </div>{first_person_houses}</div>
                 <h2> Second person </h2>
                 <div>{second_person_houses}</div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@router.get("/planets" )
async def get_items():
    first_person_planets = prep_array_planets(1983, 10, 5, 23.30,  18.063326, 59.300866, 1)
    second_person_planets = prep_array_planets(1989, 2, 10, 4.12, 18.063326, 59.300866, 1       )
    return synastry(first_person_planets, second_person_planets)


@router.get("/compatibility" )
async def get_items():
    first_person_planets = prep_array_planets(1983, 10, 5, 23.30,  18.063326, 59.300866, 1)
    second_person_planets = prep_array_planets(1989, 2, 10, 4.12, 18.063326, 59.300866, 1)
    first_person_houses = prep_array_houses(1983, 10, 5, 23.30,  18.063326, 59.300866, 1)
    second_person_houses = prep_array_houses(1989, 2, 10, 4.12, 18.063326, 59.300866, 1)
    return compatibility(synastry(first_person_planets, second_person_planets),
                         synastry_houses(first_person_planets, second_person_houses),
                         synastry_houses(second_person_planets, first_person_houses)
                         )

@router.get("/suited" )
async def get_items():
    date = datetime.datetime(1988,9,8,12,4,5)
    ret = {'sexualcompability' : 0,'toxicity' :0, 'marriage':0, 'friendship':0}
    for i in range(6000): 
        date += datetime.timedelta(days=1)
   
        first_person_planets = prep_array_planets(1983, 10, 5,  23.3,  18.063326, 59.300866, 1)
        second_person_planets = prep_array_planets(date.year, date.month, date.day, 4.12, 18.063326, 59.300866, 1)
        first_person_houses = prep_array_houses(1983, 10, 5,  23.30,  18.063326, 59.300866, 1)
        second_person_houses = prep_array_houses(date.year, date.month, date.day, 4.12, 18.063326, 59.300866, 1)
        result =  compatibility(synastry(first_person_planets, second_person_planets),
                         synastry_houses(first_person_planets, second_person_houses),
                         synastry_houses(second_person_planets, first_person_houses),
                         False)
        if (result['sexualcompability'] >= ret['sexualcompability'] and result["toxicity"] <= ret["toxicity"]
            and result["marriage"] >= ret["marriage"]
            and result["friendship"] >= ret["friendship"]
            ):
            ret = result
            ret['date'] = date

    return ret



@router.get("/planets/first_person" )
async def get_items():
    first_person_planets = prep_array_planets(1983, 10, 5, 23.30,  18.063326, 59.300866, 1)
    second_person_planets = prep_array_planets(1989, 2, 10, 4.12, 18.063326, 59.300866, 1)
    return first_person_planets

@router.get("/houses" )
async def get_items():
    first_person_houses = prep_array_houses(1983, 10, 5, 23.30,  18.063326, 59.300866, 1)
    second_person_houses = prep_array_houses(1989, 2, 10, 4.12, 18.063326, 59.300866, 1)
    return f"first_person {first_person_houses} second_person {second_person_houses}"

@router.get("/synastry_houses" )
async def get_items():
    first_person_planets = prep_array_planets(1983, 10, 5, 23.30,  18.063326, 59.300866, 1)
    second_person_planets = prep_array_planets(1989, 2, 10, 14.12, 18.063326, 59.300866, 1)
    first_person_houses = prep_array_houses(1983, 10, 5, 23.30,  18.063326, 59.300866, 1)
    #second_person_houses = prep_array_houses(1989, 2, 10, 4.12, 18.063326, 59.300866, 1)
    second_person_houses = prep_array_houses(1989, 2, 10, 14.12, 18.063326, 59.300866, 1)
    
    return f"""first person planets in second person houses 
            {synastry_houses(first_person_planets, second_person_houses)}
            second person planets in first person houses 
            {synastry_houses(second_person_planets, first_person_houses)}
    """""
