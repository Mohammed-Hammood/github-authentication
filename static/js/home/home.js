let lastUpdatedDateObj = new Date();
let lastUpdatedInSeconds = 0;

function updateDOM(data){
    const randomNum = document.querySelector('#random-number-p');
    randomNum.innerText = data.random_number;
    lastUpdatedInSeconds = data.last_updated_in_seconds;
    lastUpdatedDateObj = new Date();
}
function updateRandomNumber(){
    const fetchData = ()=> {
        fetch('/', {
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken':getCookie('csrftoken'),
            },
            mode:'same-origin'
        })
        .then(res => res.json())
        .then(data_ => updateDOM(data_))
        .catch(err => console.log(err));
    }
    setInterval(()=>{
       const seconds = (new Date() - lastUpdatedDateObj)/1000 + lastUpdatedInSeconds;
       //will send post request to the server every 5 minutes to get a new random number
       if (seconds >= 300){
            fetchData();
       }
    }, 1000);
}
window.addEventListener('load', function(){ 
    lastUpdatedInSeconds = parseInt(document.querySelector('#last_updated_in_seconds').value);
    updateRandomNumber();
});