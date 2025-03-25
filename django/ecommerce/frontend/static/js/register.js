document.addEventListener("DOMContentLoaded", function() {
    let roleSelect = document.getElementById("role");
    let businessLicenseContainer = document.getElementById("businessLicenseContainer");
    let businessLicenseInput = document.getElementById("businessLicense");

    // Show/Hide Business License Field
    roleSelect.addEventListener("change", function() {
        if (roleSelect.value === "Seller") {
            businessLicenseContainer.classList.remove("d-none");
            businessLicenseInput.setAttribute("required", "required");
        } else {
            businessLicenseContainer.classList.add("d-none");
            businessLicenseInput.removeAttribute("required");
        }
    });

    // Form Submission
    document.getElementById("registerForm").addEventListener("submit", async function(e) {
        e.preventDefault();

        let formData = new FormData();
        formData.append("name", document.getElementById("fullName").value);
        formData.append("email", document.getElementById("email").value);
        formData.append("password", document.getElementById("password").value);
        formData.append("role", document.getElementById("role").value);

        // If Seller, append Business License file
        if (document.getElementById("role").value === "seller") {
            let businessLicenseFile = document.getElementById("businessLicense").files[0];
            if (businessLicenseFile) {
                formData.append("business_license", businessLicenseFile);
            }
        }

        let response = await fetch("http://127.0.0.1:8000/users/add/", {
            method: "POST",
            body: formData
        });

        let data = await response.json();

        if (response.ok) {
            alert("Registration Successful ✅");
            window.location.href = "login.html";
        } else {
            document.getElementById("errorMessage").textContent = data.error || "Something went wrong!";
        }
    });
});
