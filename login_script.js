document.getElementById('btnSubmit').addEventListener('click', function() {
    const username = document.getElementById('txtUsername').value;
    const password = document.getElementById('txtPassword').value;

    if (!username || !password) {
        alert('Please enter both Hall Ticket Number and Password.');
        return;
    }

    // Mock login logic
    console.log('Login attempt with:', username);
    
    // In a real scenario, this would post to the server.
    // For this clone, we just show a message.
    alert('Login feature is a demonstration. Redirecting to dashboard...');
    window.location.href = 'index.html'; // Fallback to the dashboard we built earlier if it still exists
});
