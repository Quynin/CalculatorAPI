//Get buttons from DOM
const calcButtons = document.getElementsByClassName("button");
//Get text box from DOM
const cTBox = document.getElementById("calculatorTextBox");
//Display buttons
//console.log(calcButtons)

//Url to send server requests to
const serverUrl = 'http://127.0.0.1:5000';

//Initial test ping
fetch("http://127.0.0.1:5000/api/ping")
    .then(Response => Response.json())
    .then(data => console.log(data));

//Set button behaviours
for(const [key, val] of Object.entries(calcButtons)) {    
    //For all other buttons
    if (val.value != "=") {
        //Assign event listeners to functions; event listeners call append functions
        val.addEventListener("click", () => {appendToTextBar(cTBox, val)});
    //For equals button
    } else {
        val.addEventListener("click", equals);
    }

    console.log(`Listener assigned to button ${val.value}`);
}

//Append param to text bar
function appendToTextBar(cTBox, val) {
    console.log(cTBox);
    console.log(val);
    cTBox.value += val.value;
}

//Equals button handling; sends info to python backend
function equals() {

    //Build query params object
    const queryParams = {
        'calc_string': cTBox.value
    }
    sendRequest('api/calc', queryParams);
}

//Handles sending requests to server 
function sendRequest(apiSubUrl, queryParams) {

    //Convert parameters object to query string
    const queryString = new URLSearchParams(queryParams).toString();
    //Combine API endpoint with query parameters
    const fullUrl = `${serverUrl}/${apiSubUrl}?${queryString}`;
    //Make the GET request display response
    fetch(fullUrl)
        .then(response => response.json())
        .then(data => cTBox.value = data.result)
}