const addUserForm = document.querySelector('#addUserForm');
const addUserName = document.querySelector('#addUserName');

const deleteUserForm = document.querySelector('#deleteUserForm');
const deleteUserSelect = document.querySelector('#deleteUserSelect');

const userToolForm = document.querySelector('#userToolForm');
const userToolFirstname = document.querySelector('#userToolFirstname');
const userToolName = document.querySelector('#userToolName');
const userToolAmmount = document.querySelector('#userToolAmmount');

async function addUser() {
    event.preventDefault();
    
    const data = {
        firstname: addUserName.value,
    }

    const response = await postRequest(URL_API_ADD_USER, data);
    console.log(response);
    location.reload();
}
addUserForm.onsubmit = addUser;

async function deleteUser() {
    event.preventDefault();
    
    const data = {
        firstname: deleteUserSelect.value,
    }

    const response = await postRequest(URL_API_DELETE_USER, data);
    console.log(response);
    location.reload();
}
deleteUserForm.onsubmit = deleteUser;

async function changeAmmount() {
    event.preventDefault();
    
    const data = {
        firstname: userToolFirstname.value,
        toolname: userToolName.value,
        ammount: userToolAmmount.value,
    }
    const response = await postRequest(URL_API_CHANGE_AMMOUNT, data);
    console.log(response);
    location.reload();
}
userToolForm.onsubmit = changeAmmount;