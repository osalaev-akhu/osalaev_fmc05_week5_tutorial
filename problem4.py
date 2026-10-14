"""
An app supports these languages:

languages = ["uzbek", "english", "russian"]

Read a language name from the user. Assume it is entered in lowercase.

Print "Available" if the language is in the list.
 Otherwise, print "Not available".

Example 1
Input:
english

Output:

Available


Example 2
Input:
french

Output:

Not available
"""

languages = ["uzbek", "english", "russian"]
lang = input("Input: ")
if lang in languages:
    print("Available")
else:
    print("Not available")
