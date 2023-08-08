const addToolForm = document.querySelector('#addToolForm');
const addToolName = document.querySelector('#addToolName');

const deleteToolForm = document.querySelector('#deleteToolForm');
const deleteToolName = document.querySelector('#deleteToolName')


async function addTool() {
    event.preventDefault();

    const toolName = addToolName.value;
    const data = {
        toolname: toolName,
    };
    
    const response = await postRequest(URL_API_ADD_TOOL, data);
    console.log(response)
    sessionStorage.setItem("showToast", "true");
    sessionStorage.setItem("toastMessage", response.message);
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
    sessionStorage.setItem("showToast", "true");
    sessionStorage.setItem("toastMessage", response.message);
    location.reload();
}
deleteToolForm.onsubmit = deleteTool;