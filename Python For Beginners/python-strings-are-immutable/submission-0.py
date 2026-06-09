def remove_fourth_character(word: str) -> str:
    new_message = word[:3]+word[4:]
    return new_message



# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
