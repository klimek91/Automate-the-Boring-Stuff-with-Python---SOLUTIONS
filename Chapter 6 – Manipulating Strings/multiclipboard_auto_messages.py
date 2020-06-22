#!python

import sys, pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) > 1:
        keyphrase = sys.argv[1]
        if keyphrase in TEXT:
                pyperclip.copy(TEXT[keyphrase])
        else:
            print("No such phrase")