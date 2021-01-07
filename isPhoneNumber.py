# PRACTICE WITH REGEXES

import re  # Import the regex object

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # Create the regex object w/ re.compile() function
mo = phoneNumRegex.search("my number is 631-697-5186.") # Pass the string into a match obj (mo usually) into search()
print('phone number found: ' + mo.group()) # call the match objects group() method to return the string of the
# matched text

# Regex with groups
numRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo2 = numRegex.search('My phone number is (631) 697-5186')
areaCode, mainNumber = mo2.groups()
print("Area code is: " + areaCode)
print("Number is: " + mainNumber)

# Using the pipe -- returns first occurance
heroRegex = re.compile(r'Batman|Bruce Wayne')
mo3 = heroRegex.search('Batman and Bruce Wayne')
print(mo3.group())


