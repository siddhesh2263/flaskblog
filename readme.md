# Flask Blog by Corey Schafer

## Setting up the flask app:

* After writing the initial code, make sure to add the following at the bottom:
```
if __name__ == '__main__':
	app.run(debug=True)
```

Then run the following:
```
python flask_blog.py
```
---

## Update 18-12-2020

* `url_for('home')` is used to go to routes defined by their function names.
* To generate a SECRET_KEY, we can use the following snippet:
```
import secrets
secrets.token_hex(16)
```
* Use of flask wtforms for making forms, performing validation.
* Flash messages using bootstrap classes.
* register and login html pages made in such a way that any design changes can be done easily.

---

## Update 20-12-2020

* Introduction to Flask-SQLAlchemy - ORM (object relational mapping)
* One to Many relationship between User and Post class
* def __repr__ function
* The database was populated using command line:
```
from flask_blog import db
```

---

## Update 22-12-2020

* Converting modules into package
* This is done to avoid issues of circular imports.
* The `init.py` file signifies that the folder is a package. It initialises the classes and other models at application startup.

---

## Update 23-12-2020

* Added user authentication with the help of the `login-flask` module
* Added validation checks for username and email in forms.py
* Used the `Bcrypt` module to hash passwords:
```
from flask_bcrypt import Bcrypt
hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
bcrypt.check_password_hash(hashed_password, 'password')
# True
```

---

## Update 24-12-2020

* Updated Account settings page
* Used the Pillow library  to compress image
* Made a new UpdateAccountInfo form
* Used the `os` and `secrets` package for saving and renaming pictures


---


## Update 25-12-2020

* Create, update and delete posts
* Bootstrap Modals were used to provide confirmation before deleting posts
* `url_for` is used a lot of times here
* Check that only the current user is able to update/delete posts


---


## Update 26-12-2020

* Added pagination using Pagination method
* Click on user, get posts by that user only
* This was a complicated part, need to look into it more closely


--- 


## Update 27-12-2020

* Added password reset functionality, but there was this error that I currently cannot resolve:
```
    smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials 84sm33253316pfy.9 - gsmtp')
```

* After turning off the "Allow less secure apps access feature", the problem won't go.

* We discussed a way to securely store credentials in the environment variables, and then accessing them using the `os ` library:
```
import os
id = os.environ.get('VARIABLE_NAME')
```

* This is done so that the credentials are not visible in the repositories.

* Tokens are valid for a certain amount of time, and the duration can be modified:
```
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
s = Serializer(app.config['SECRET_KEY'], expires_sec)
token = s.dumps({'user_id': 1}).decode('utf-8')
s.loads(token)
```

* The error needs to be looked into.