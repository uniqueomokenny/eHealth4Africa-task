from django.contrib.auth.decorators import login_required, user_passes_test

def is_medical_practioner(self):
    if self.is_medical_practioner:
        return True
    else:
        return False

med_login_required = user_passes_test(lambda u: True if u.is_medical_practioner else False, login_url='/sign-in')
def medical_practioner_login_required(view_func):
    decorated_view_func = login_required(med_login_required(view_func), login_url='/')
    return decorated_view_func