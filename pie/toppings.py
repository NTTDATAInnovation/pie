import re


def apply_toppings(text):
    """Applies tasty regex toppings to a text"""
    for key, topping in TOPPINGS.items():
        text = topping.sub(key, text)
    return text


# "{{LOCATION}}": re.compile(
#     "(?:[A-Za-zÆæØøÅå\\.-]+){3,3}(?:\\s?[Vv]ej[^r](?:en)?|[Gg]ade|s?\\s[
# P]lads|\\s?[Aa]ll[é])(?:\\s?\\d{1,})?"
# ),

TOPPINGS = {
    "{{PHONE}}": re.compile(
        "((?:\\+\\d{2}[-\\.\\s]??|\\d{4}[-\\.\\s]??)?(?:\\d{3}[-\\.\\s]??\\d{3}[-\\.\\s]??\\d{4}|\\(\\d{3}\\)\\s*\\d{3}[-\\.\\s]??\\d{4}|\\d{3}[-\\.\\s]??\\d{4}))"
    ),
    "{{EMAIL}}": re.compile("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[\\.\\w\\d]+\\.\\w{2,}"),
    "{{LINK}}": re.compile(
        "((http|https)\\:\\/\\/)?[a-zA-Z0-9\\.\\/\\?\\:@\\-_=#]{2,}\\.([a-zA-Z]){2,6}([a-zA-Z0-9\\.\\&\\/\\?\\:@\\-_=#])*"
    ),
    "{{CPR NUMBER}}": re.compile("[0-3]\\d[0-1]\\d{3}\\-\\d{4}"),
}

# LARGE TOKEN MASKING
CHAR_LIMIT = 40
CHAR_LIMITER = re.compile(rf"[^\s]{{{CHAR_LIMIT},}}")
