ch = input("Enter any character: ")
if ch.isalpha() and len(ch) == 1:
    if ch in 'aeiouAEIOU':
        print(f"'{ch}' is Vowel.")
    else:
        print(f"'{ch}' is Consonant.")
else:
    print(f"'{ch}' is not an alphabet.")
