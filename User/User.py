"""Super class or administrator and registered user
20. Manages information related to users"""

class User():
    """User type"""
    def __init__(self, name, organization, email, password, skill_level, type):
        self.__name = name
        self.__organization = organization
        self.__email = email
        self.__password = password
        self.__type = type
        if self.__type == "RegisteredUser":
            self.__skill_level = skill_level

    """Getters"""
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_organization(self):
        return self.__organization

    def get_skill(self):
        return self.__skill_level

    def get_user_type(self):
        return self.__type

    """Setters"""
    def set_name(self, n):
        self.name = n

    def set_email(self, e):
        self.__email = e

    def set_password(self, p):
        self.__password = p

    def set_organization(self, o):
        self.__organization = o

    def set_skill(self, s):
        self.__skill_level = s

    """"#set date for workshop persistance
    #download/upload reference material
    #Request connection
    # """