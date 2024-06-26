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
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime

chars = "!@$%&"

class PasswordManager2():

    def __init__(self):
        self.avdict = {}


    def add(self, service, pword):
        if len(pword) >= 8 and any(item in chars for item in pword) and pword not in self.avdict.values():
            self.avdict[service] = pword


    def remove(self, service):
        del self.avdict[service]


    def update(self, service, pword):
        if len(pword) >= 8 and any(item in chars for item in pword) and pword not in self.avdict.values():
            self.avdict.update({service:pword})
    

    def list_services(self):
        return list(self.avdict)
    
        
    def sort_services_by(self, service, rev = ""):
        lst = []
        
        if service == "added_on" and rev == "reverse":
            for item in self.avdict:
                lst.append(item)
            return list(lst[::-1])
        
        elif service == "service" and rev == "reverse":
            for item in self.avdict:
                lst.append(item)
            return sorted(lst, reverse=True)
        
        elif service == "service":
            for item in self.avdict:
                lst.append(item)
            return sorted(lst)
        
        else:
            service == "service" and rev == "added_on"
            for item in self.avdict:
                lst.append(item)
            return list(lst)


    def get_for_service(self, string):
        return self.avdict.get(string)


# return get() function directly instead of using if conditionals
# if string in self.avdict:
#    return self.avdict.get(string)
# else:
#    return None