# List of numbers from message.txt
nums = [128, 322, 353, 235, 336, 73, 198, 332, 202, 285, 57, 87, 262, 221, 218, 405, 335, 101, 256, 227, 112, 140, ]

result = "" # This will store the decoded message

# Loop through each number in the list 'nums'
for n in nums:
    # Step 1: apply module 37 (get the remainder)
    r = n % 37
    # Step 2: map the result to the correct character
    if 0 <= r <= 25: # 0–25 → letters A-Z
        # ord('A') gives ASCII value of 'A'
        # adding r moves forward in the alphabet
        result += chr(ord('A') + r)
    elif 26 <= r <= 35: # 26–35 → digits 0–9
        # subtract 26 to convert into correct digit
        result += str(r - 26)
    else: # 36 or larger → underscore "_"
        result += "_"

# Print result in picoCTF flag format
print("picoCTF{" + result + "}")