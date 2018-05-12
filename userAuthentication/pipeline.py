from django.shortcuts import render

def check_email(details, *args, **kwargs):
    """
    to check the email of the user registering so as to allow only college students.
    """
    email = details.get('email')
    if not email.endswith('@iiita.ac.in'):
        error_msg = 'Please Login With Your College Email'
        return render(kwargs.get('request'), 'registration/login.html', {'error_msg': error_msg})
