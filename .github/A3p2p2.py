from Countries import country_db
from match import match
from typing import List, Tuple, Callable, Any

def get_year(country: Tuple[str, str, int, List[str]]) -> int:
    return country[2]

def get_leaders(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[3]

def languange_by_name(matches: List[str]) -> List[str]:
    for country in country_db:
        if country[0] == matches:
            return country[1]
    return None
