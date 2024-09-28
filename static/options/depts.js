document.addEventListener('DOMContentLoaded', function() {
    const courses = [
        "Select",
        "BBA",
        "BCA",
        "B.A. AID",
        "B.A. Economics",
        "B.A. English",
        "B.A. ELL",
        "B.A. Geography",
        "B.A. Hindi",
        "B.A. History",
        "B.A. Political Science",
        "B.A. Sociology",
        "B.Com Accounts",
        "B.Com Vocational B&I",
        "B.Com Vocational OMSP",
        "B.Sc. Botany",
        "B.Sc. Chemistry",
        "B.Sc. Computer Application",
        "B.Sc. BioTechnology",
        "B.Sc. Geology",
        "B.Sc. Information Technology",
        "B.Sc. Mathematics",
        "B.Sc. Physics",
        "B.Sc. Statistics",
        "B.Sc. Zoology",
        "B.Voc Fashion Technology",
        "BJMC",
        "BRM",
        "BFMO",
        "M.A. Economics",
        "M.A. English",
        "M.A. Geography",
        "M.A. Hindi",
        "M.A. History",
        "M.A. Political Science",
        "M.Com Accounts"
    ];

    const selectElement = document.getElementById('deptSelect');
    courses.forEach(course => {
        const option = document.createElement('option');
        option.value = course;
        option.textContent = course;
        selectElement.appendChild(option);
    });
});
