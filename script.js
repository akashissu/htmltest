document.addEventListener('DOMContentLoaded', () => {
    const ctxLesson = document.getElementById('lessonChart').getContext('2d');
    const ctxActivity = document.getElementById('activityChart').getContext('2d');

    new Chart(ctxLesson, {
        type: 'bar',
        data: {
            labels: ['Lesson 1', 'Lesson 2', 'Lesson 3'],
            datasets: [{
                label: 'Progress',
                data: [50, 70, 30],
                backgroundColor: 'rgba(54, 162, 235, 0.7)'
            }]
        }
    });

    new Chart(ctxActivity, {
        type: 'line',
        data: {
            labels: ['Week 1', 'Week 2', 'Week 3'],
            datasets: [{
                label: 'Activity',
                data: [30, 60, 45],
                borderColor: 'rgba(75, 192, 192, 1)',
                tension: 0.1
            }]
        }
    });
});