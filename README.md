# todo
to-do list project<br>

This project creates a to-do list website.<br>
The website lets the users:<br>
    1. create new accounts.<br>
    2. authenticate and log in.<br>
    3. add tasks to the to-do list.<br>
    4. delete tasks.<br>
    5. check or uncheck tasks.<br>

The urls used are:<br>
    1. register/: used to register new user<br>
    2. login/: used to login an existing user<br>
    3. home/: visit the home page of the webiste displaying the to-do list of the particular user.<br>

    Note: The above mentioned urls are used to return templates to different pages of the website, to
    load the data on the website api calls are made using the api urls of the website which are mentioned below

The api (api urls) of the webiste is:<br>
    1. /base/api/login/: used to login existing user.<br>
    2. /base/api/register/: used to register new user.<br>
    3. /base/api/home/: used to load data on the home page.<br>
    4. /base/api/logout/: used to logout user.<br>
    5. /base/api/checkbox_toggle/: in case the state of tasks being checked or unchecked is changed that change is registered at the server with this url.<br>
    6. /base/api/add_task/: adds new task to the user's to-do list.<br>
    7. /base/api/delete_task/: deletes an existing task.<br>
