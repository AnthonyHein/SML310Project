import git
import os
import requests
import urllib.parse
from typing import List, Tuple

BASE_DIR = git.Repo(os.getcwd(), search_parent_directories=True).working_dir
BASE_DIR

import sys

sys.path.append(f'{BASE_DIR}/src/')

from geocoding_client.response import Geometry, Location, Response, Result, Status

def get_course_geometry(course: str, country_code: str =None) -> Tuple[Geometry, str]:

    query = course + " racecourse"
    safe_query = urllib.parse.quote_plus(query)
    url = f"https://maps.googleapis.com/maps/api/geocode/json?key={os.environ['GEOCODING_API_KEY']}&address={safe_query}&country={country_code}"

    response = requests.request("GET", url)
    if not response.ok:
        return (None, "could not request URL")

    response_dict: Response = response.json()

    status: Status = response_dict['status']
    if status != Status.OK.value:
        return (None, status)

    results: List[Result] = response_dict['results']
    if len(results) != 1:
        return (None, "several results returned, the query is ambiguous")

    return (results[0]['geometry'], None)

def get_course_location(course: str, country_code: str =None) -> Tuple[Location, str]:
    
    geometry, err = get_course_geometry(course, country_code)

    if err != None:
        return None, err

    return (geometry['location'], None)

if __name__ == "__main__":
    geometry, err = get_course_geometry("Southwell (AW)", "GB")
    if err != None:
        print(f"ERROR: Southwell (AW) GB- {err}")
    else:
        print(geometry)

    location, err = get_course_location("Southwell (AW)", "GB")
    if err != None:
        print(f"ERROR: Southwell (AW) GB - {err}")
    else:
        print(location)
