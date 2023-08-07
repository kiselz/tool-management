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

    toolName = addToolName.value;
    data = {
        toolname: toolName,
    };
    
    const request = await fetch(URL_API_ADD_TOOL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });

    const response = await request.json();
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

    toolName = deleteToolName.value;
    data = {
        toolname: toolName,
    };

    const request = await fetch(URL_API_DELETE_TOOL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
    const response = await request.json();
    console.log(response);
}
deleteToolForm.onsubmit = deleteTool;