from .models import MyUser
from django.contrib.auth.models import User

class EmailAuthBackend():
    def authenticate(email,password):
        try:
            user=MyUser.objects.get(email=email)
            success=user.check_password(password)
            if success:
                print('success')
                return user
        except MyUser.DoesNotExist:
            pass
        return None

    def get_user(self,uid):
            try:
                return MyUser.objects.get(pk=uid)
            except:
                return None
    
    