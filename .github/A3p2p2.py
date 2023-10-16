from Countries import country_db
from match import match
from typing import List, Tuple, Callable, Any

def get_year(country: Tuple[str, str, int, List[str]]) -> int:
    return country[2]

def get_leaders(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[3]

def get_name(country: Tuple[str, str, int, List[str]]) -> str:
    return country[0]

def get_language(country: Tuple[str, str, int, List[str]]) -> str:
    return country[1]

def languange_by_name(matches: List[str]) -> List[str]:
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
