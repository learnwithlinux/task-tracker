document.getElementById('taskForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const taskInput = document.getElementById('taskInput');
    const formData = new FormData();
    formData.append('task', taskInput.value);

    try {
        const response = await fetch('/', {
            method: 'POST',
            body: formData
        });
        if (response.ok) {
            taskInput.value = '';
            location.reload(); // Simple reload for demo; use AJAX for prod
        }
    } catch (error) {
        console.error('Error adding task:', error);
    }
});

// Fetch tasks on load (for dynamic updates)
fetch('/api/tasks')
    .then(response => response.json())
    .then(tasks => {
        const taskList = document.getElementById('taskList');
        taskList.innerHTML = tasks.map(task => `<li>${task.task} <span>(ID: ${task.id})</span></li>`).join('');
    });
