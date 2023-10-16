from Countries import country_db
from match import match
from typing import List, Tuple, Callable, Any


def get_name(country: Tuple[str, str, int, List[str]]) -> str:
    return country[0]
def get_language(country: Tuple[str, str, int, List[str]]) -> str:
    return country[1]
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
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what coutries were founded in _"), names_by_year),
    (str.split("what countries were founded between _ and _"), names_between_years),
    (str.split("what countries were founded before _"), names_before_year),
    (str.split("what countries were founded after _"), names_after_year),
    # note there are two valid patterns here two different ways to ask for the director
    # of a movie
    (str.split("who directed %"), director_by_title),
    (str.split("who was the director of %"), director_by_title),
    (str.split("what movies were directed by %"), title_by_director),
    (str.split("who acted in %"), actors_by_title),
    (str.split("when was % made"), year_by_title),
    (str.split("in what movies did % appear"), title_by_actor),
    (str.split("what movies had % and % "), title_by_two_actors),
    (str.split("what movies had these actors: %"), title_by_actors),
    (["bye"], bye_action),
]

