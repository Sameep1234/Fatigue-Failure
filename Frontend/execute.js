function executePy() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('GET', "http://localhost:5000/plot")
    xhttp.send();
    xhttp.onreadystatechange = function() {
        console.log(responseText);
    }
}