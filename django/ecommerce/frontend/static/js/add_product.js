document.addEventListener("DOMContentLoaded", function () {
    const addProductForm = document.getElementById("addProductForm");

    addProductForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const token = sessionStorage.getItem("access_token");
        if (!token) {
            alert("You must be logged in to add products!");
            return;
        }

        const formData = new FormData();
        formData.append("name", document.getElementById("productName").value);
        formData.append("description", document.getElementById("productDescription").value);
        formData.append("price", document.getElementById("productPrice").value);
        formData.append("stock", document.getElementById("productStock").value);
        const categories = document.getElementById("productCategories").selectedOptions;
        for (let category of categories) {
            formData.append("categories", category.value);
        }
        const fileInput = document.getElementById("productImage");
        if (fileInput.files.length > 0) {
            formData.append("image", fileInput.files[0]); // ✅ Add only if selected
        }


        

        try {
            const response = await fetch("http://127.0.0.1:8000/shop/products/", {
                method: "POST",
                headers: {
                    
                    "Authorization": `Bearer ${token}`
                },
                body: formData
            });

            // const responseData = await response.json();
            

            if (response.ok) {
                alert("✅ Product added successfully!");
                window.location.href = "index.html"; // Redirect to dashboard
            } else {
                const errorData = await response.json();
                alert(`❌ Error: ${errorData.error || "Failed to add product."}`);
            }
        } catch (error) {
            console.error("Error adding product:", error);
            alert("❌ Failed to add product. Please try again.");
        }
    });
});
