from pie.utensils.loggers import logger
from functools import wraps
import re

# TODO: Add this transformation to incoming text
TOKEN_OVER_N_CHARS = re.compile(r"[^\s]{40,}")

# QUICK RETURN CONDITIONS
LESS_THAN_N_LIMIT = re.compile(r"\b\w{1,30}\b")
FULL_TEXT_CHECKS = re.compile(r"^([\d\w]{20,}|[^\d\w]+|.{,2}|{{[^\{}]+}})$")


def _easy_bake(content: str):
    r"""A function to heuristically check if an entity is in the content.
    Current checks
    - No tokens have < 30 chars
    - String is only \w\d and > 15 chars
    - There's no text nor digits
    - String is less than 3 characters.

    Returns:
        Bool: Indication of whether to return directly or not.
    """
    if any(
        [
            FULL_TEXT_CHECKS.fullmatch(content),
            not LESS_THAN_N_LIMIT.findall(content),  # no <30 char words
        ]
    ):
        logger.info(f"Msg triggered quick return. Len: {len(content)}")
        return True
    return False


def easy_bake(func):
    @wraps(func)
    def inner(self, query):
        return func(self, query) if not _easy_bake(query) else query

    return inner
