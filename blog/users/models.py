from django.contrib.auth.models import AbstractUser

#class CustomUser(AbstractUser):
    # Personal information
    # AbstractBaseUser provides: first_name, last_name, user_name, email, password
#    pass

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
    
