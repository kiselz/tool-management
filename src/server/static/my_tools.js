// console.log(URL_API_GET_AVAILABLE)

takeToolSelect = document.querySelector('#takeToolSelect');
takeToolForm = document.querySelector('#takeToolForm');
takeToolAmmount = document.querySelector('#takeToolAmmount');

returnToolSelect = document.querySelector('#returnToolSelect');
returnToolForm = document.querySelector('#returnToolForm');
returnToolAmmount = document.querySelector('#returnToolAmmount')

// takeToolForm
async function setMaxAmmountToTake() {
    toolname = takeToolSelect.value;

    const response = await fetch(URL_API_GET_AVAILABLE, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({toolname: toolname})
    });
    const availableAmmount = await response.json();
    
    takeToolAmmount.setAttribute('max', availableAmmount);
}
if (takeToolSelect) takeToolSelect.onchange = setMaxAmmountToTake;


async function takeTool() {
    event.preventDefault();

    data = {
        firstname: CURRENT_USER,
        ammount: Number.parseInt(takeToolAmmount.value),
        toolname: takeToolSelect.value,
    }
    const response = await fetch(URL_API_TAKE_TOOL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    console.log(result);
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

    data = {
        firstname: CURRENT_USER,
        ammount: Number.parseInt(returnToolAmmount.value),
        toolname: returnToolSelect.value,
    }


    const response = await fetch(URL_API_RETURN_TOOL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
    const result = await response.json();
    console.log(result);
    location.reload();
}
if (returnToolForm) returnToolForm.onsubmit = returnTool;