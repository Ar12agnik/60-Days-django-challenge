from django.contrib.auth.base_user import BaseUserManager



class usermanager(BaseUserManager):
    def create_user(self,phone_number,password=None,**extra):
        