from Countries import country_db
from match import match
from typing import List, Tuple, Callable, Any

def get_year(Countries: Tuple[str, str, int, List[str]]) -> int:
    return Countries[2]

def get_leaders(Countries: Tuple[str, str, int, List[str]]) -> List[str]:
    return Countries[3]