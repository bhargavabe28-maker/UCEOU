$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

    // Mock click events for tiles
    $('.tile').on('click', function() {
        const title = $(this).find('h4').text();
        alert('Navigating to ' + title + ' section...');
    });

    // Handle logout
    $('.logout-link').on('click', function(e) {
        if(!confirm('Are you sure you want to log out?')) {
            e.preventDefault();
        }
    });
});
