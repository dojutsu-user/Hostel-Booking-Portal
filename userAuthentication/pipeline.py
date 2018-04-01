from django.http import HttpResponse


def check_email(details, *args, **kwargs):
    print(details)
    email = details.get('email')
    if not email.endswith('@iiita.ac.in'):
        return HttpResponse("INVALID EMAIL. PLEASE SIGN IN WITH YOUR '@iiita.ac.in' EMAIL")
