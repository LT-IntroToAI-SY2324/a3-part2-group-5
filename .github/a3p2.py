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
