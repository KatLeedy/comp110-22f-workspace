"""An example function definition."""

def my_max(a: int, b: int) -> int: 
    """Returns the largest argument."""
    if a > b: 
        return a
    else: 
        return b

user_input1: int = int(input("Please enter one number: "))
user_input2: int = int(input("Please input a second number: "))

max_from_user: int = my_max(user_input1, user_input2)
print(f"The larger value is {max_from_user}")