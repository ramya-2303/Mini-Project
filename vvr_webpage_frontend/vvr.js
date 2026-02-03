function showMessage() {
  alert("Welcome to VVR Enterprises! 🚀");
}

function handleSubmit(event) {
  event.preventDefault();
  alert("Thank you for contacting us! We will get back to you soon.");
}

// ⏰ Real-Time Clock
setInterval(() => {
  const clock = document.getElementById("clock");
  const now = new Date();
  clock.textContent = "🕒 " + now.toLocaleTimeString();
}, 1000);

// 🌙 Dark Mode Toggle
document.getElementById("darkModeToggle").addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});

// 📬 Newsletter Form
function subscribeNewsletter(event) {
  event.preventDefault();
  const email = document.getElementById("subscribeEmail").value;
  alert(`🎉 Thank you for subscribing, ${email}!`);
  document.getElementById("subscribeEmail").value = "";
}

// ❓ FAQ Toggle
function toggleAnswer(element) {
  const answer = element.querySelector(".answer");
  answer.style.display = answer.style.display === "block" ? "none" : "block";
}



////in components all reusable UI components are stored
///src/contexts====This is used to manage global state with React Context API.
//AuthContext.jsx
// Stores authentication info (logged-in user, tokens, etc.)
// Makes it accessible to all components without passing props manually

//📁 server.js
// This is your main backend file.
// It likely contains:
// Express server
// API routes
// CORS setup
// Middleware
// Database connection (optional)
// Authentication logic