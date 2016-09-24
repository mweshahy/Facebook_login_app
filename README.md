# Facebook_login_app
This is just a test project
Requirements list:

1. Please use Python / Django and MySQL (innoDB) as database. Make sure to implement a clean, well-structured and high-performance database scheme
2. The user should connect/login with Facebook (logout accordingly) (Note: Plugins can be used)
3. The Facebook app should simply provide the following output: the name and profile picture of the logged-in user
4. The token, which will be stored for the user in the database, should be a long living access token
5. If the user removes the Facebook app, the user shall be marked as "is_active = false" in the database (Note: Facebook deauth callback)
6. Please be efficient when writing your code and commit your code in a github.com repository. Pay attention to clean commits

As required to send result after 5 hours of work, many requirements are not satisfied.
The main package used for the app: Python Social Auth
https://python-social-auth.readthedocs.io/en/latest/
https://github.com/omab/python-social-auth

In order to test the application:
go inside the outer mysite folder where manage.py exists and run the following commands:
python3 manage.py migrate
python3 manage.py runserver

Then open your browser and type:
http://localhost:8000/
and enjoy!