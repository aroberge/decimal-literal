"""Experimental syntax notation for decimal literal

n D -> Decimal(n) where n is any number
"""

import token_utils  # Need to be installed separately

__version__ = "0.0.1"

import_statement = "from decimal import Decimal"


def transform_source(source):
    tokens = token_utils.tokenize(source)
    if len(tokens) < 2:
        return source
    for first, second in zip(tokens, tokens[1:]):
        if first.is_number() and second == "D":
            first.string = f"Decimal('{first.string}')"
            second.string = ""

    return token_utils.untokenize(tokens)


if __name__ == "__main__":
    original = "a = 0.33D"
    transformed = "a = Decimal('0.33')"
    assert transform_source(original) == transformed
    print("Looks good")
