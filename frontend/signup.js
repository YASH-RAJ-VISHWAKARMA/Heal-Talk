document.getElementById("signupForm").addEventListener("submit", function (e) {
  e.preventDefault();

  let name = document.getElementById("name").value.trim();
  let email = document.getElementById("email").value.trim();
  let pass = document.getElementById("password").value.trim();
  let cpass = document.getElementById("confirmPassword").value.trim();
  let msg = document.getElementById("message");

  // Password length check
  if (pass.length < 6) {
    msg.style.color = "yellow";
    msg.innerHTML = "Password must be at least 6 characters.";
    return;
  }

  // Password match check
  if (pass !== cpass) {
    msg.style.color = "red";
    msg.innerHTML = "Passwords do not match!";
    return;
  }

  // Success message
  msg.style.color = "#00ff9d";
  msg.innerHTML = "Account Created Successfully ✔ Redirecting...";

  // Redirect to login page after 1.5 sec
  setTimeout(() => {
    window.location.href = "login.html";
  }, 1500);
});