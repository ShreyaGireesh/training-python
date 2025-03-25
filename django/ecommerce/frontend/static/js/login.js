document.getElementById("loginForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let errorMessage = document.getElementById("errorMessage");

    let response = await fetch("http://127.0.0.1:8000/users/login/", {  // Django API URL
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password }) // 🔹 Send email instead of username
    });

    let data = await response.json();

    if (response.ok) {
        console.log("After login:", data.access);
        sessionStorage.setItem("access_token", data.access);   // Save access token
        sessionStorage.setItem("refresh_token", data.refresh); // Save refresh token
        await fetchUserRole();
        errorMessage.textContent = ""; 
        window.location.href = "index.html"; 
    } else {
        errorMessage.textContent = "Invalid email or password ❌";
    }
});

async function fetchUserRole() {
    const token = sessionStorage.getItem("access_token");
    if (!token) {
        console.error("No access token found ❌");
        return;
    }
    let response = await fetch("http://127.0.0.1:8000/users/user-role/", {  // Django API URL
        method: "GET",
        headers: { 
            "Authorization": `Bearer ${token}`
        }
    });

    if (response.ok) {
        let data = await response.json();
        sessionStorage.setItem("role", data.role); 
        sessionStorage.setItem("name",data.name);
        sessionStorage.setItem("userid", data.userid);

// Redirect based on role
    } else {
        console.error("Failed to fetch user role");
    }
}

