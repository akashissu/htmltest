document.addEventListener('DOMContentLoaded', () => {
    const toggleDarkMode = document.querySelector('.profile-menu');
    toggleDarkMode.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
    });
    // Example chart setup
    const ctx = document.getElementById('salesChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
                label: 'Sales',
                data: [12, 19, 3, 5, 2, 3, 9],
                borderColor: 'rgba(75, 192, 192, 1)',
                tension: 0.1
            }]
        }
    });
});