#  Building Advanced Forms with Flask-WTF

Build forms using a Flask extension called Flask-WTF. It has a number of benefits over the simple HTML Form. e.g.

1. Easy Form Validation - Makes sure the user is entering data in the required format in all the required fields. e.g. checking that the user's email entry has a "@" and a "." at the end. All without having to write your own validation code.

2. Less Code - If you have a number of forms in your website, using WTForm can dramatically reduce the amount of code you have to write (or copy & paste).

3. Built in CSRF Protection - CSRF stands for Cross Site Request Forgery, it's an attack that can be made on website forms which forces your users to do unintended actions (e.g. transfer money to a stranger) or compromise your website's security if it's an admin.

Flask developers will usually choose Flask-WTF to create forms in their websites. However, in the wild, you might also see projects that are built with HTML Forms. So it's important to understand how both of them work.


## Install Flask-WTF Extension

The requirements.txt file is a file where you can specify all the dependencies (the installed packages that your project depends on) and their versions. This means that you can share your project without all the installed packages, making it a lot more lightweight. When someone downloads your project (like you have done here), the requirements.txt file tells their code editor which packages need to be installed. Read more on this here. (https://docs.google.com/document/d/e/2PACX-1vRIW_TuZ6z0ASjAoxgJgmzjGYLCDx019tKvphaTwK_Za7fnMKywUuXI0-s5wr0nQI_gprm6J6y7L9rL/pub)



2. Use the Terminal to install Flask-WTF. Installation documentation: https://flask-wtf.readthedocs.io/en/1.0.x/install/


> pip install Flask-WTF

For Windows, in Command Prompt (Admin) try to run pip install using the Python executable:

> python -m pip install Flask-WTF
>
*pip installs are always case sensitive!