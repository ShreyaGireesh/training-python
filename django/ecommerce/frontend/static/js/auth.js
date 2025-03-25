async function refreshToken() {
    const refresh_token = sessionStorage.getItem("refresh_token");
    console.log("Hii")
    if (!refresh_token) {
        console.error("No refresh token found ❌");
        logout();  // If no refresh token, log the user out
        return;
    }

    try {
        console.log("Inside try")
        let response = await fetch("http://127.0.0.1:8000/users/refresh/", {  // Django refresh token URL
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ refresh: refresh_token })
        });

        if (response.ok) {
            let data = await response.json();
            sessionStorage.setItem("access_token", data.access); // Update access token
        } else {
            logout();  // If refresh fails, log the user out
            console.error("Refresh token did not return a new access token.");
            // sessionStorage.clear();
        }
    } catch (error) {
        console.error("Error refreshing token:", error);
        logout();
    }
}

function logout() {
    sessionStorage.clear();  // Clear all stored session data
    window.location.href = "login.html";  // Redirect to login
}

setInterval(refreshToken, 4 * 60 * 1000); 