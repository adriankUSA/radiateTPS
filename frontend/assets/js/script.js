document.getElementById("loadDataBtn").addEventListener("click", function() {
    fetch("http://127.0.0.1:5000/ct")
        .then(response => response.json())
        .then(data => {
            alert(data.message); // Show the response message
        })
        .catch(error => console.error("Error:", error));
});


document.getElementById("viewResultsBtn").addEventListener("click", function() {
    let imgElement = document.getElementById("doseImage");
    imgElement.src = "http://127.0.0.1:5000/get_image";
    imgElement.style.display = "block";
});
