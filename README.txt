Phone number and email address extractor

1. Get the text off the clipboard
2. Find all the phone numbers and emails in the text
3. Paste them onto the clipboard

The code will need:
1. Use pyperclip module to copy and paste strings
2. Create regexes- one for phone numbers and the other for emails
3. Findall matches (not just the first match)
4. Neatly format the strings into a single string to paste
5. Display a message if no matches were found in the text