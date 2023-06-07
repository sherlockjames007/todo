# todo
to-do list project

This project creates a to-do list website.
The website lets the users:
    1. create new accounts.
    2. authenticate and log in.
    3. add tasks to the to-do list.
    4. delete tasks.
    5. check or uncheck tasks.

The urls used are:
    1. register/: used to register new user
    2. login/: used to login an existing user
    3. home/: visit the home page of the webiste displaying the to-do list of the particular user.

    Note: The above mentioned urls are used to return templates to different pages of the website, to
    load the data on the website api calls are made using the api urls of the website which are mentioned below

The api (api urls) of the webiste is:
    1. /base/api/login/: used to login existing user.
    2. /base/api/register/: used to register new user.
    3. /base/api/home/: used to load data on the home page.
    4. /base/api/logout/: used to logout user.
    5. /base/api/checkbox_toggle/: in case the state of tasks being checked or unchecked is changed that change is registered at the server with this url.
    6. /base/api/add_task/: adds new task to the user's to-do list.
    7. /base/api/delete_task/: deletes an existing task.
