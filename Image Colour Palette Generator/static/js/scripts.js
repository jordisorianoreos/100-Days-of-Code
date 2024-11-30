function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        showNotification('Copied to clipboard: ' + text);
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}

function showNotification(message) {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.style.display = 'block';
    setTimeout(function() {
        notification.style.display = 'none';
    }, 2000);
}
