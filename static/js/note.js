const host = window.location.hostname;
const api = host + '/api/v1/'

console.log(api);

document.addEventListener('DOMContentLoaded', function () {
    const mainContent = document.getElementById('main-content');
    const saveMemoryButton = document.getElementById('saveMemoryButton');
    const updateMemoryButton = document.getElementById('updateMemoryButton');
    const memoryTemplate = document.getElementById('memoryTemplate');

    saveMemoryButton.addEventListener('click', function () {
        const memoryTitle = document.getElementById('memoryTitle').value.trim();
        const memoryDescription = document.getElementById('memoryDescription').value.trim();
        const memoryLocation = document.getElementById('memoryLocation').value.trim();

        if (memoryTitle && memoryDescription && memoryLocation) {
            const clone = memoryTemplate.cloneNode(true);

            clone.querySelector('.memory-title').innerText = memoryTitle;
            clone.querySelector('.memory-description').innerText = memoryDescription;
            clone.id = '';
            clone.classList.remove('d-none');

            clone.querySelector('.edit-memory-button').addEventListener('click', function () {
                document.getElementById('editMemoryId').value = clone.querySelector('.memory-title').innerText;
                document.getElementById('editMemoryTitle').value = memoryTitle;
                document.getElementById('editMemoryDescription').value = memoryDescription;
                document.getElementById('editMemoryLocation').value = memoryLocation;
            });

            mainContent.innerHTML = '';
            mainContent.appendChild(clone);

            $('#addMemoryModal').modal('hide');
            document.getElementById('addMemoryForm').reset();
        }
    });

    updateMemoryButton.addEventListener('click', function () {
        const editMemoryId = document.getElementById('editMemoryId').value;
        const editMemoryTitle = document.getElementById('editMemoryTitle').value.trim();
        const editMemoryDescription = document.getElementById('editMemoryDescription').value.trim();
        const editMemoryLocation = document.getElementById('editMemoryLocation').value.trim();

        if (editMemoryTitle && editMemoryDescription && editMemoryLocation) {
            const memoryItems = mainContent.querySelectorAll('.memory-title');

            memoryItems.forEach(function (item) {

            if (item.innerText === editMemoryId) {
                    item.innerText = editMemoryTitle;
                    item.parentElement.querySelector('.memory-description').innerText = editMemoryDescription;
                }
            });

            $('#editMemoryModal').modal('hide');
            document.getElementById('editMemoryForm').reset();
        }
    });
});



