function updateskill() {
    const teamSelect = document.getElementById('teamSelect');
    const skillSelect = document.getElementById('skillSelect');

    if (teamSelect.value !== "Select") {
        skillSelect.disabled = false;
    } else {
        skillSelect.disabled = true;
    }

    skillSelect.innerHTML = '';

    let skills = [];
    if (teamSelect.value === "Tech Team") {
        skills = [
            "Select",
            "3D Animations",
            "Web Development",
            "App Development",
            "Bot Development",
            "Cloud Platform",
            "Others (Please Mention)"
        ];
    } else if (teamSelect.value === "Creative and PR Team") {
        skills = [
            "Select",
            "Content Creation",
            "Graphic Designing",
            "Video Production",
            "Social Media Presence",
            "Script Writing",
            "Others (Please Mention)"
        ];
    } else if (teamSelect.value === "Executive Team") {
        skills = [
            "Select",
            "Public Speaking",
            "Project Management",
            "Event Planning",
            "Others (Please Mention)"
        ];
    }

    skills.forEach(skill => {
        const option = document.createElement('option');
        option.value = skill;
        option.textContent = skill;
        skillSelect.appendChild(option);
    });
}