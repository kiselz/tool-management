takeToolSelect = document.querySelector('#takeToolSelect');
takeToolForm = document.querySelector('#takeToolForm');
takeToolAmmount = document.querySelector('#takeToolAmmount');

returnToolSelect = document.querySelector('#returnToolSelect');
returnToolForm = document.querySelector('#returnToolForm');
returnToolAmmount = document.querySelector('#returnToolAmmount')


async function takeTool() {
    event.preventDefault();

    const data = {
        firstname: CURRENT_USER,
        ammount: Number.parseInt(takeToolAmmount.value),
        toolname: takeToolSelect.value,
    }

    const response = await postRequest(URL_API_TAKE_TOOL, data);
    sessionStorage.setItem("showToast", "true");
    sessionStorage.setItem("toastMessage", response.message)
    console.log(response);
    location.reload();
}
if (takeToolForm) takeToolForm.onsubmit = takeTool;


// returnToolForm
function setMaxAmmountToReturn() {
    toolname = returnToolSelect.value
    ammount = Number.parseInt(document.querySelector(`#${toolname}-ammount`).textContent);

    returnToolAmmount.setAttribute('max', ammount);
}
if (returnToolSelect) returnToolSelect.onchange = setMaxAmmountToReturn;

async function returnTool() {
    event.preventDefault();

    const data = {
        firstname: CURRENT_USER,
        ammount: Number.parseInt(returnToolAmmount.value),
        toolname: returnToolSelect.value,
    }

    const response = await postRequest(URL_API_RETURN_TOOL, data);
    sessionStorage.setItem("showToast", "true");
    sessionStorage.setItem("toastMessage", response.message)
    console.log(response);
    location.reload();
}
if (returnToolForm) returnToolForm.onsubmit = returnTool;