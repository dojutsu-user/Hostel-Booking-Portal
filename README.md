# HOSTEL BOOKING PORTAL
A Simple Hostel Booking Portal Based On Django2.0 With Custom Admin Page

# INSTRUCTIONS

1. Download the zip file and extract to a new folder.
2. Open terminal and navigate to the folder which contains `manage.py` file by `cd Hostel-Booking-Portal-master`.
3. Create a new virtual environment: `virtualenv venv`.
4. Activate the virtual environment: `source ./venv/bin/activate`.
5. Install the dependencies: `pip install -r requirements.txt`.
6. Create the database: `python manage.py migrate --run-syncdb`.
7. Create super user: `python manage.py createsuperuser` and then enter `username`, `email`, and `password` for the super user.
8. Collect the static files: `python manage.py collectstatic`. (NOTE: This will create a folder named `static_cdn` on the base directory of the directory where `manage.py` is located. To change this edit the `MEDIA_ROOT` in the `VHBooking_Portal/settings.py`. And then run `python manage.py collectstatic`.)
9. Run the server: `python manage.py runserver`.

## Add A Hostel

1. Run the server: `python manage.py runserver`.
2. Navigate to `http://localhost:8000`.
3. Login with the username and password for super user.
4. Under the `HOSTEL` section, click on `Hostels` and then click on `ADD HOSTEL` button on the top right.
5. Enter the name of the hostel (for eg. VH1) and then fill the other data according to the below table:
    
      Field | What it represents
      ------------ | -------------
      Total rooms | Total numbers the hostel have.
      Total available rooms | Total rooms which are, at present, available for booking.
      Total booked rooms | Tital rooms which are already booked.
6. Click on Save.
7. Open the file `hostel/util.py` and add your hostel under the function `generate_choices_of_hostels` there in the tuple with the corresponding serial number.
8. Save the file.
9. Open the file `visitor/util.py`.
10. Edit the list on `line 23` with the names of your hostel.
11. Save the file.

## To Allow Only Specific Email Domains To Login

1. Open the file: `userAuthentication/pipeline.py`.
2. Edit the condition which checks the email in the function `check_email` on `line 8` to allow/disallow different email domains to login.

## Add Room Types

1. Open The File `visitor/models.py`.
2. Edit the tuple according to your needs. For eg. 

  ```python
  ROOM_TYPES = (  
    ('AC', 'AC'),
    ('NON AC', 'NON AC'),
)
```

## Enabling Login With Google

1. Open file `VHBooking_Portal/settings.py` and navigate to `line 166`.
2. Enter your Client ID for Google Web Application for the field `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY`.
3. On `line 167`, Enter your Secret Key for Google Web Application for the field `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET`.
4. A guide about this can be found here : [Simple Google Authentication in Django](https://medium.com/@jainsahil1997/simple-google-authentication-in-django-58101a34736b)

## Editing The Template

1. All templates files are there in the folder `templates` located at the same folder where `manage.py` files is located, edit those files according to your needs.

## To Make Admin Of The Website

1. Navigate to `http://localhost:8000`.
2. Under `AUTHENTICATION AND AUTHORIZATION` section, click on `Users`.
3. Select a user with its username.
4. Under the `Permissions` section, select `Staff status` and then click on Save.
5. Now this user will be redirected automatically to the admin page when it logins via google.

## Screenshots

Homepage : [Homepage](https://ibb.co/c7kXaJ)

User Panel : 
  * [Screenshot 1](https://ibb.co/jYLOFJ)
  * [Screenshot 2](https://ibb.co/mu3zpd)
  * [Screenshot 3](https://ibb.co/jzBupd)
  
Admin Panel :
  * [Screenshot 1](https://ibb.co/nuX9pd)
  * [Screenshot 2](https://ibb.co/bzXg2y)
  * [Scnreenshot 3](https://ibb.co/d5dkvJ)
  
