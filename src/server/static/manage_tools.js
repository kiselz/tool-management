const addToolForm = document.querySelector('#addToolForm');
const addToolName = document.querySelector('#addToolName');

const deleteToolForm = document.querySelector('#deleteToolForm');
const deleteToolName = document.querySelector('#deleteToolName')

function showToast() {
    if (sessionStorage.getItem("showToast")) {
        sessionStorage.removeItem("showToast");
        toastBody = document.querySelector('div.toast-body');
        toastBody.textContent = sessionStorage.getItem("toastMessage");
        toast = new bootstrap.Toast(document.querySelector('div.toast'));
        toast.show();
    }
}
window.onload = showToast

async function addTool() {
    event.preventDefault();

    const toolName = addToolName.value;
    const data = {
        toolname: toolName,
    };
    
    const respone = await postRequest(URL_API_ADD_TOOL, data);
    console.log(response)
    if (response["status"] === "error") {
        sessionStorage.setItem("showToast", "true");
        sessionStorage.setItem("toastMessage", response.message)
    }
    location.reload();
}
addToolForm.onsubmit = addTool;

async function deleteTool() {
    event.preventDefault();

    const toolName = deleteToolName.value;
    const data = {
        toolname: toolName,
    };
    
    const response = await postRequest(URL_API_DELETE_TOOL, data);
    console.log(response);
}
deleteToolForm.onsubmit = deleteTool;