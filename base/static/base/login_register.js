// this file contains all the javascript functions for login_register page of this project
// the file is invoked with the login_register page template





// sends request to log in user
async function login(){
    let email = document.getElementById('login_email').value;
    let password = document.getElementById('login_password').value;

    if (email == null || password == null){
        alert('specify both email and password');
        return;
    }

    let url = '/api/login/';
    let cookie = document.cookie.split(';');    
    let csrftoken = cookie[0].split('=')[1];

    let promise = await fetch(url, {
        method: 'post',
        body: JSON.stringify({
            'email': email,
            'password': password
        }),
        headers: {
            'Content-Type': 'application/json;',
            'X-CSRFToken': csrftoken
        }
    })

    if (promise.ok){
        window.location.href = '/';
    }
    else if (promise.status == 403){
        alert('Incorrect username or password');
    }
    else {
        alert('internal server error, please try again');
    }
    
    let response = promise.json();
}


// sends request to register new user
async function register(){
    let email = document.getElementById('register_email').value;
    let password = document.getElementById('register_password').value;
    let first_name = document.getElementById('first_name').value;
    let last_name = document.getElementById('last_name').value;

    let url = '/api/register/';
    let cookie = document.cookie.split(';');    
    let csrftoken = cookie[0].split('=')[1];

    if (email == null || password == null || first_name == null || last_name == null){
        alert('specify all the information');
    }

    console.log(email, password, first_name, last_name);

    let response = await fetch(url, {
        method: 'post',
        body: JSON.stringify({
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
        }),
        headers: {
            'Content-Type': 'application/json;',
            'X-CSRFToken': csrftoken
        }
    })

    let message = await response.json();

    if (promise.ok){
        window.location.href = '/';
    }
    else if (promise.status == 403){
        alert('Incorrect username or password');
    }
    else {
        alert('internal server error, please try again');
    }    
}