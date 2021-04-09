function runPyScript(){
    var jqXHR = $.ajax({
        type: "GET",
        url: "/main.py",
        async: false,
    }).done(function() {
        alert("RUNNING");
    })

    return jqXHR.responseText;
}

function testPyScript() {
    response = runPyScript();
    alert(response);
}