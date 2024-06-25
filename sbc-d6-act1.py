word_to_check = "Race Car"
xf = word_to_check.replace(" ", "").strip().lower()

is_palindrome = True

for i in range(len(xf) // 2):
    if xf[i] != xf[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("This word is a Palindrome")
else:
    print("This word is Not a Palindrome")
