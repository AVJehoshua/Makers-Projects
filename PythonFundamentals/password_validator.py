# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==

chars = "!@$%&"

def is_valid(string):
    if len(string) >= 8 and any(item in chars for item in string):
        return True
    else:
        return False