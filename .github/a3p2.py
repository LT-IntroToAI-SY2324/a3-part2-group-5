from Countries import country_db
from match import match
from typing import List, Tuple, Callable, Any


def get_name(country: Tuple[str, str, int, List[str]]) -> str:
    return country[0]
def get_language(country: Tuple[str, str, int, List[str]]) -> str:
    return country[1]
def get_leaders(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[3]
def get_year(country: Tuple[str, str, int, List[str]]) -> int:
    return country[2]
def year_by_name(matches: List[str]) -> int:
    for country in country_db:
        if country[0] == matches:
            return country[2]
    return None
def names_by_year(year: int) -> List[str]:
    result = []
    for country in country_db:
        if country[2] == year:
            result.append(country[0])
    return result
def names_between_years(years: List[int]) -> List[str]:
    result = []
    for country in country_db:
        if country[2] >= years[0] and country[2] <= years[1]:
            result.append(country[0])
    return result
def names_after_year(year: int) -> List[str]:
    result = []
    for country in country_db:
        if country[2] > year:
            result.append(country[0])
    return result
def names_before_year(year: int) -> List[str]:
    result = []
    for country in country_db:
        if country[2] < year:
            result.append(country[0])
    return result
def language_by_name(matches: List[str]) -> List[str]:
    for country in country_db:
        if country[0] == matches:
            return country[1]
    return None

def leaders_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if get_name(country) == matches[0]:
            results = get_leaders(country)
    return results

def name_by_language(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if get_language(country) == matches[0]:
            results.append(get_name(country))
    return results
def name_by_leader(matches: List[str]) -> List[str]:
    x = []
    for country in country_db:
        for i in range(len(country[3])): 
            if country[3][i] == matches[0]:
                x.append(get_name(country))
    return x
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what coutries were founded in _"), names_by_year),
    (str.split("what countries were founded between _ and _"), names_between_years),
    (str.split("what countries were founded before _"), names_before_year),
    (str.split("what countries were founded after _"), names_after_year),
    (str.split("what is the official language of %"), language_by_name),
    (str.split("who are the leaders of %"), leaders_by_name),
    (str.split("what year was % founded in"), year_by_name),
    (str.split("when was % founded"), year_by_name),
    (str.split("what countries has % led"), name_by_leader),
    ##(["bye"], bye_action),
]

