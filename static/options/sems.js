document.addEventListener('DOMContentLoaded', function() {
    const sems = [
        "Select",1,2,3,4,5,6,7,8
    ];

    const selectElement = document.getElementById('semSelect');
    sems.forEach(sem => {
        const option = document.createElement('option');
        option.value = sem;
        option.textContent = sem;
        selectElement.appendChild(option);
    });
});
