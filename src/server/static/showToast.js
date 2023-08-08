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
