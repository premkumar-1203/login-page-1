document.getElementById("submitBtn").addEventListener("click", async function () {

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    const response = await fetch("/login", {
        method: "POST",
        body: formData
    });

    const result = await response.json();
    alert(result.message);
});

