# PART 2: Automating Tasks

## Chapter 7: Pattern Matching with Regular Expressions

### practice code 1
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: '+ mo.group())

### practice code 2
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

# TODO: Create email regex.
# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.