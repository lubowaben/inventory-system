// main.js

// Navbar active link highlighting
document.addEventListener('DOMContentLoaded', function() {
    var currentPath = window.location.pathname;
    var navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    navLinks.forEach(function(link) {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Toggle password visibility on registration and login forms
document.querySelectorAll('.toggle-password').forEach(button => {
    button.addEventListener('click', function() {
        let passwordField = document.querySelector(this.dataset.target);
        let icon = this.querySelector('i');

        if (passwordField.type === 'password') {
            passwordField.type = 'text';
            icon.classList.remove('fa-eye');
            icon.classList.add('fa-eye-slash');
        } else {
            passwordField.type = 'password';
            icon.classList.remove('fa-eye-slash');
            icon.classList.add('fa-eye');
        }
    });
});

// Confirmation before performing actions like logout
document.querySelectorAll('.confirm-action').forEach(button => {
    button.addEventListener('click', function(e) {
        let message = this.dataset.confirmMessage || "Are you sure you want to proceed?";
        if (!confirm(message)) {
            e.preventDefault();
        }
    });
});

// Automatically hide alert messages after a few seconds
document.addEventListener('DOMContentLoaded', function() {
    let alert = document.querySelector('.alert');
    if (alert) {
        setTimeout(() => {
            alert.classList.add('fade-out');
        }, 5000);
    }
});
// main.js

// Navbar active link highlighting
document.addEventListener('DOMContentLoaded', function() {
    var currentPath = window.location.pathname;
    var navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    navLinks.forEach(function(link) {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Toggle password visibility on registration and login forms
document.querySelectorAll('.toggle-password').forEach(button => {
    button.addEventListener('click', function() {
        let passwordField = document.querySelector(this.dataset.target);
        let icon = this.querySelector('i');

        if (passwordField.type === 'password') {
            passwordField.type = 'text';
            icon.classList.remove('fa-eye');
            icon.classList.add('fa-eye-slash');
        } else {
            passwordField.type = 'password';
            icon.classList.remove('fa-eye-slash');
            icon.classList.add('fa-eye');
        }
    });
});

// Confirmation before performing actions like logout
document.querySelectorAll('.confirm-action').forEach(button => {
    button.addEventListener('click', function(e) {
        let message = this.dataset.confirmMessage || "Are you sure you want to proceed?";
        if (!confirm(message)) {
            e.preventDefault();
        }
    });
});

// Automatically hide alert messages after a few seconds
document.addEventListener('DOMContentLoaded', function() {
    let alert = document.querySelector('.alert');
    if (alert) {
        setTimeout(() => {
            alert.classList.add('fade-out');
        }, 5000);
    }
});
