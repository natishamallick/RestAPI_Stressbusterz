StressBusterz - Group Mini Project 
Team Members- Natisha Mallick & Mohammed Abdullah
https://www.youtube.com/watch?v=3fEtdyr8YOU 

This is an application built using Python, Flask and uses Google Cloud.
<br />

To run the application follow the following steps.
<br />



> **Step #1** - Clone sources (this repo)

```bash
$ # Clone the sources
$ git clone https://github.com/iMuhammadAbdullah/stressbusterz.git
$ cd stressbusterz
```

<br />

> **Step #2** - Creating a virtual environment

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> **Step #3** - Installing dependencies

```bash
$ # Install requirements
$ pip3 install -r requirements.txt
```

<br />

> **Step #4** - Creating Tables (SQLite persistance)

```bash
$ # Create tables
$ flask shell
$ >>> from app import db
$ >>> db.create_all()
```

<br />

> **Step #5** - Starting the project

```bash
$ # Run the application
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the app in browser: http://127.0.0.1:5000/
```

## Code-base structure

Following is the structure of the code.

```bash
< PROJECT ROOT >
   |
   |-- app/
   |    |-- static/
   |    |    |-- <css, images>    # CSS files(Custom file)
   |    |
   |    |-- templates/
   |    |    |
   |    |    |-- index.html           # Index File
   |    |    |-- login.html           # Login Page
   |    |    |-- register.html        # Registration Page
   |    |    
   |    |
   |   config.py                      # Provides APP Configuration 
   |   forms.py                       # Defines the login and register Forms 
   |   models.py                      # Defines the models of the app 
   |   views.py                       # App Routes 
   |
   |-- requirements.txt
   |-- run.py
   |
   |-- ************************************************************************
```
