document.getElementById("entryForm").onsubmit = async (e) => {
    e.preventDefault();

    const data = {
        student_id: document.getElementById("student_id").value,
        rc: document.getElementById("rc").value,
        licence: document.getElementById("licence").value
    };

    const res = await fetch('/entry', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });

    const result = await res.json();
    alert(result.status);
};