document.addEventListener('DOMContentLoaded', function() {
    const teams = [
        "Select",
        "Tech Team",
        "Creative and PR Team",
        "Executive Team"
    ];

    const selectElement = document.getElementById('teamSelect');
    teams.forEach(team => {
        const option = document.createElement('option');
        option.value = team;
        option.textContent = team;
        selectElement.appendChild(option);
    });
});
