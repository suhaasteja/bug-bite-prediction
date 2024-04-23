function uploadImage() {
    const form = document.getElementById('uploadForm');
    const formData = new FormData(form);
    console.log("upload image", formData);
    fetch('/predict', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('results').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error:', error));
}
