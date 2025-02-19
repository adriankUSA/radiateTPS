document.getElementById("loadDataBtn").addEventListener("click", function() {
    fetch("http://127.0.0.1:5000/load_data")
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        });
});

document.getElementById("computeDoseBtn").addEventListener("click", function() {
    fetch("http://127.0.0.1:5000/compute_dose")
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            document.getElementById("doseImage").src = "http://127.0.0.1:5000/static/SimpleDose.png";
            document.getElementById("doseImage").style.display = "block";
        });
});
