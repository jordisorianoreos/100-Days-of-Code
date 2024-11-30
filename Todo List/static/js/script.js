function updateStatus(element) {
    const todoId = element.dataset.id || element.value;
    let newStatus;

    const currentStatus = element.dataset.status;

    if (currentStatus === 'To Do') {
        newStatus = 'Doing';
    } else if (currentStatus === 'Doing') {
        newStatus = 'Done';
    } else if (currentStatus === 'Done') {
        newStatus = 'To Do';
    }

    fetch(`/update_status/${todoId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ status: newStatus })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            location.reload();
        } else {
            alert('Failed to update status');
        }
    });
}

function deleteTodo(element) {
    const todoId = element.dataset.id;

    fetch(`/delete/${todoId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            location.reload();
        } else {
            alert('Failed to delete todo');
        }
    });
}

function clearAllTodos() {
    fetch(`/clear_all`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            location.reload();
        } else {
            alert('Failed to clear todos');
        }
    });
}
