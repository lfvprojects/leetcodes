string = "abcabcbb"
result = 0

characters = set()  # Set to track unique characters
left = 0  # Initialize the left pointer

print(f"Input String: {string}")
print(f"{'Step':<6} {'Window':<12} {'Characters in Set':<25} {'Result'}")

for right in range(len(string)):
    step = right + 1

    while string[right] in characters:
        print(f"{step:<6} {string[left:right + 1]:<12} {str(characters):<25} Removing: {string[left]}")
        characters.remove(string[left])
        left += 1

    characters.add(string[right])

    result = max(result, right - left + 1)

    print(f"{step:<6} {string[left:right + 1]:<12} {str(characters):<25} Current Result: {result}")

print("\nFinal Result:", result)