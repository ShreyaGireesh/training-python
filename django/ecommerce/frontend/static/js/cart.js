document.addEventListener("DOMContentLoaded", function () {
    fetchCartItems();

    document.getElementById("logout").addEventListener("click", function () {
        sessionStorage.clear();
        window.location.href = "login.html";
    });
});

async function fetchCartItems() {
    const token = sessionStorage.getItem("access_token");
    if (!token) {
        alert("Please log in to view your cart.");
        window.location.href = "login.html";
        return;
    }

    try {
        let response = await fetch("http://127.0.0.1:8000/shop/cart/", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            }
        });
        if (response.status === 401) { // Unauthorized, token might be expired
            console.warn("Access token expired, trying to refresh... 🔄");
            await refreshToken(); // Call refresh function from auth.js
            return fetchCartItems(); // Retry fetching products after refresh
        }
        if (!response.ok) {
            throw new Error("Failed to fetch cart items ❌");
        }

        let cartItems = await response.json();
        console.log(cartItems);
        renderCart(cartItems);
    } catch (error) {
        console.error(error);
    }
}

function renderCart(cartItems) {
    let cartContainer = document.getElementById("cartContainer");
    cartContainer.innerHTML = "";

    if (cartItems.length === 0) {
        cartContainer.innerHTML = `<h4 class="text-center text-muted">Your cart is empty 🛒</h4>`;
        return;
    }

    cartItems.forEach(item => {
        let cartCard = document.createElement("div");
        cartCard.classList.add("col-md-4", "mb-3");

        cartCard.innerHTML = `
            <div class="card shadow-sm">
                <img src="${item.product_details.image ? item.product.image : 'static/images.png'}" class="card-img-top" alt="${item.product_details.name}">
                <div class="card-body">
                    <h5 class="card-title">${item.product_details.name}</h5>
                    <p class="card-text">${item.product_details.description}</p>
                    <p class="text-primary fw-bold">Rs. ${item.product_details.price}</p>
                    <p class="fw-bold">Quantity: ${item.quantity}</p>
                    <button class="btn btn-danger btn-sm" onclick="removeFromCart(${item.id})">🗑️ Remove</button>
                </div>
            </div>
        `;

        cartContainer.appendChild(cartCard);
    });
}

async function removeFromCart(cartItemId) {
    const token = sessionStorage.getItem("access_token");

    if (!token) {
        alert("Please log in.");
        return;
    }

    try {
        let response = await fetch(`http://127.0.0.1:8000/shop/cart/${cartItemId}/`, {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            }
        });

        if (response.status === 204) {
            alert("🗑️ Item removed from cart.");
            fetchCartItems();  // Refresh cart
        } else {
            alert("❌ Error removing item.");
        }
    } catch (error) {
        console.error("Error deleting cart item:", error);
        alert("❌ Failed to remove item.");
    }
}