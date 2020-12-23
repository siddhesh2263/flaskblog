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
