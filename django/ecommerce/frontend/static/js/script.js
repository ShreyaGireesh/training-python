// main page
document.addEventListener("DOMContentLoaded", function () {
    let name = sessionStorage.getItem("name");
    async function initialize(){
        let role = sessionStorage.getItem("role"); // Get stored role
        let userId = sessionStorage.getItem("userid");
        
        userId = Number(userId)
        showRoleContent(role)
        await displayProducts(role, userId);
    }
    initialize();
    const userNameLi = document.getElementById("user-name");

    if (name && userNameLi) {
        userNameLi.textContent = name;
        userNameLi.style.display = "inline";  // Ensure it's visible
    } else {
        userNameLi.style.display = "none";
    }
    // Logout Function
    document.getElementById("logout").addEventListener("click", function () {
        sessionStorage.clear();
        window.location.href = "login.html";
    });
});

function showRoleContent(role) {
    if (role === "Admin") {
        document.getElementById("adminContent").style.display = "block";
        document.getElementById("sellerContent").style.display = "none";
        document.getElementById("customerContent").style.display = "none";
    } else if (role === "Seller") {
        document.getElementById("sellerContent").style.display = "block";
        document.getElementById("customerContent").style.display = "none";
    } else {
        document.getElementById("customerContent").style.display = "block";
        document.getElementById("sellerContent").style.display = "none";
    }
}

async function displayProducts(role, userid){
    const token = sessionStorage.getItem("access_token");
    if (!token) {
        console.error("No access token found ❌");
        return;
    }
    try {
        let response = await fetch("http://127.0.0.1:8000/shop/products/", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            }
        });
        if (response.status === 401) { // Unauthorized, token might be expired
            console.warn("Access token expired, trying to refresh... 🔄");
            await refreshToken(); // Call refresh function from auth.js
            return displayProducts(role, userid); // Retry fetching products after refresh
        }

        if (!response.ok) {
            throw new Error("Failed to fetch products ❌");
        }

        let products = await response.json();
        renderProducts(products, role, userid);
    } catch (error) {
        console.error(error);
    }
}

function renderProducts(products, role, userid){
    let productContainer = document.getElementById("productContainer");
    productContainer.innerHTML = "";

    products.forEach(product => {
        let productCard = document.createElement("div");
        productCard.classList.add("col-md-4", "mb-3");

        productCard.innerHTML = `
            <div class="card shadow-sm">
                <div class="image-container">
                    <img src="${product.image?product.image:'static/images.png'}" class="card-img-top" alt="${product.name}">
                    ${role === "Seller" && product.seller === userid ? `
                        <div class="image-overlay">
                           
                            <button class="btn btn-danger btn-sm" onclick="removeProduct(${product.id})">Delete</button>
                        </div>
                    ` : ""}
                </div>
                <div class="card-body">
                    <h5 class="card-title">${product.name}</h5>
                    <p class="card-text">${product.description}</p>
                    <p class="text-primary fw-bold">Rs. ${product.price}</p>
                    ${role === "Customer" ? `<button class="btn btn-info add-to-cart" onclick="addToCart(${product.id})">Add to Cart</button>` : ""}
                </div>
            </div>
        `;
        productContainer.appendChild(productCard);
    });

    // document.querySelectorAll(".add-to-cart").forEach(button => {
    //     button.addEventListener("click", function () {
    //         let productId = this.getAttribute("data-id");
    //         addToCart(productId);
    //     });
    // });

    if (role === "Seller" || role === "Admin") {
        document.getElementById("addProductBtn").addEventListener("click", () => {
            window.location.href = "add_product.html";
        });
    }
    if (role === "Customer") {
        document.getElementById("cartBtn").addEventListener("click", () => {
            window.location.href = "cart.html";
        });
    }
}

async function addToCart(productId) {
    console.log("Attempting to add product to cart:", productId);
    const accessToken = sessionStorage.getItem("access_token");

    if (!accessToken) {
        alert("Please log in to add items to your cart.");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/shop/cart/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${accessToken}`
            },
            body: JSON.stringify({
                product: productId,
                quantity: 1
            })
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Added to cart:", data);
            alert(`✅ Added to cart!`);
        } else {
            const errorData = await response.json();
            alert(`❌ Error: ${errorData.error || "Could not add to cart."}`);
        }
    } catch (error) {
        console.error("Error adding to cart:", error);
        alert("❌ Failed to add item. Please try again.");
    }
}

async function removeProduct(productId) {
    const token = sessionStorage.getItem("access_token");

    if (!token) {
        alert("Please log in.");
        return;
    }

    try {
        let response = await fetch(`http://127.0.0.1:8000/shop/products/${productId}/`, {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            }
        });

        if (response.status === 204) {
            alert("Product deleted");
            displayProducts();  // Refresh cart
        } else {
            alert("❌ Error deleteing product.");
        }
    } catch (error) {
        console.error("Error deleting product:", error);
        alert("❌ Failed to remove product.");
    }
}