import re

dateRegex = re.compile(r"""
([0-3]?\d)/  #date
([0-1]?\d)/  #month
([1-2]\d\d\d)
""",re.VERBOSE)