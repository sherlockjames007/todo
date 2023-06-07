// this file contains javascript functions for the home page of this project
// this file is invoked by the template of the home page





// this is the function called after clicking the logout button on the home page
// the function sends request to the /api/logout/ url of the website, gets the response, checks it
// if everything is ok in the response the user is logged out otherwise an error alert is displayed
async function logout(){
    let url = '/api/logout/';
    let cookie = document.cookie.split(';');    
    let csrftoken = cookie[0].split('=')[1];

    let promise = await fetch(url, {
        method: 'post',
        body: JSON.stringify({
            
        }),
        headers: {
            'Content-Type': 'application/json;',
            'X-CSRFToken': csrftoken
        }
    });

    if (!promise.ok){
        alert('something went wrong');
    }
    else {
        window.location.href = '/login/';
    }
}


// when the add task button is clicked on the home page the add task dialog box is displayed with this function
// called by the add task button
function show_add_task(){
    let el = document.getElementById('add-task-div');
    if (el.style.visibility == 'hidden'){
        el.style.visibility = 'visible';
        el.style.height = 'initial';
        el.style.marginBottom = '3vh';
    }
    else {
        el.style.visibility = 'hidden';
        el.style.height = '0vh';
        el.style.marginBottom = '0vh';
    }    
}


// this function is invoked when the user clicks on the "Add" button in the add task box
// sends request to the server and performs the necessary actions
async function add_task(){
    let url = '/api/add_task/';
    let cookie = document.cookie.split(';');
    let csrftoken = cookie[0].split('=')[1];

    let el1 = document.getElementById('add-task-title');
    let el2 = document.getElementById('add-task-desc');

    let response = await fetch(url, {
        method: 'post',
        body: JSON.stringify({
            'title': el1.value,
            'description': el2.value,
        }),
        headers: {
            'Content-Type': 'application/json;',
            'X-CSRFToken': csrftoken
        }
    })

    if (!response.ok){
        alert('something went wrong, try again!!');
    }
    window.location.reload();

    let el = document.getElementById('add-task-div');
    el.style.visibility = 'hidden';
    el.style.height = '0vh';
    el.style.marginBottom = '0vh';
}


// deletes a task from the server
// reloads the page afterwards
async function delete_task(task_id){
    let url = '/api/delete_task/';
    let cookie = document.cookie.split(';');
    let csrftoken = cookie[0].split('=')[1];

    let response = await fetch(url, {
        method: 'post',
        body: JSON.stringify({
            'task_id': task_id,
        }),
        headers: {
            'Content-Type': 'application/json;',
            'X-CSRFToken': csrftoken
        }
    })

    if (!response.ok){
        alert('something went wrong, try again!!');
    }
    window.location.reload();
}


// in case the checkbox is toggled this function is used to signal the server about that
// the server saves the change
async function checkbox_toggle(checked, task_id){    
    let url = '/api/checkbox_toggle/';
    let cookie = document.cookie.split(';');
    let csrftoken = cookie[0].split('=')[1];

    let response = await fetch(url, {
        method: 'post',
        body: JSON.stringify({
            'task_id': task_id,
            'checked': checked,
        }),
        headers: {
            'Content-Type': 'application/json;',
            'X-CSRFToken': csrftoken
        }
    })

    if (!response.ok){
        alert('something went wrong, try again!!');
    }
    window.location.reload();
}

// creates a "div" for a new task in the html page
function create_todo_task(data){
    let div5 = document.createElement('div');
    div5.className = 'div-5';

    let div6 = document.createElement('div');
    div6.className = 'div-6';
    
    let chkbx = document.createElement('input');
    chkbx.setAttribute('type', 'checkbox');

    let title = document.createElement('span');
    title.className = 'span-3';

    let desc = document.createElement('span');
    desc.className = 'span-4';

    let delbtn = document.createElement('button');
    delbtn.innerText = 'Delete';
    delbtn.className = 'button-3';
    
    chkbx.checked = data['checked'];
    
    title.innerText = data['title'];
    desc.innerText = data['description'];    

    delbtn.addEventListener("click", () =>  delete_task(data['id']));
    chkbx.addEventListener("change", () => checkbox_toggle(chkbx.checked, data['id']));

    div6.appendChild(chkbx);
    div6.appendChild(title);
    div6.appendChild(delbtn);
    div5.appendChild(div6);
    div5.appendChild(desc);

    // console.log(div5);
    return div5;
}

// gets the to-do list saved by the user
async function get_todo_list(){
    let url = '/api/home/';
    let response = await fetch(url);

    let data = await response.json();
    
    if (!response.ok){
        alert('Something went wrong, try again later!!!!');
        return;
    }

    let todo = document.getElementById('todo-list');

    for (key in Object.keys(data)){
        let div = create_todo_task(data[key]);
        todo.appendChild(div);
    }
}

// the get_todo_list() function is called by this script whenever the home page is loaded.
get_todo_list();