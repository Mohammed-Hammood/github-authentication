function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function modalToggle(action=null){
    const modal = document.querySelector('.modal-container');
    if(modal.className.includes("hidden" || action === 'hidden')){
        modal.classList.remove("hidden");
        modal.classList.add("flex");
        modal.querySelector('button:first-child').focus();
    }else {
        modal.classList.add("hidden");
        modal.classList.remove("flex");
    }
}
function logout(){
    modalToggle('hidden');
    window.location.pathname = "/logout";
}

window.addEventListener('keyup', function(event){
    if(event.key === "Escape" || event.keyCode === 27){
        modalToggle('hidden');
    }
});