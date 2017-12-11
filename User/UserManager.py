"""
18. Delegates task in subsystem
19. Handle Errors
"""
from User import User

class UserManager:
    user_list = []

    def update_userList(self, us, name, organization, email, password, skill_level, type):
        us = User(name, organization, email, password, skill_level, type)
        us.set_name(name)
        us.set_organization(organization)
        us.set_email(email)
        us.set_password(password)
        us.set_skill(skill_level)

    def create_user(self, name, organization, email, password, skill_level, type):
        uList = self.get_userList()
        newUser = User(name, organization, email, password, skill_level, type)
        self.add_user(newUser, uList)
        #Update db
        #create user and add it to list and update db

    def add_user(self, us, uList):
        uList.append(us)
        #update db

    def delete_user(self, us, uList):
        uList.remove(us)
        #update db

    def get_userList(self):
        return self.user_list

