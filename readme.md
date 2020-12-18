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
