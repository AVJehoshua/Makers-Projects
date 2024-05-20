# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#   4. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# We recommend that you store the passwords in a dictionary, where the keys are
# the service names and the values are the passwords.
#
# Example usage:
#   > password_manager = PasswordManager()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.get_for_service('not_real')
#   None
#   > password_manager.get_for_service('twitter')
#   None
#   > password_manager.list_services()
#   ['gmail', 'facebook']
#

# == YOUR CODE ==

# PLAN - 
# function 1 - init, no parameters no return value
# function 2 - add password - only if valid, 2 parameters, no return value
# function 3 - get service - 1 parameter, return value of specified key(string)
# function 4 - list services - return list of all services which user has pword


chars = "!@$%&"

class PasswordManager():

    def __init__(self):
        self.avdict = {}

    def add(self, service, pword):
        if len(pword) >= 8 and any(item in chars for item in pword):
            self.avdict[service] = pword
        
    def get_for_service(self, service):
        if service in self.avdict:
            return self.avdict.get(service)
        else:
            return None
        
    def list_services(self):
        return self.avdict.keys()