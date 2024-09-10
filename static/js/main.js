function getFileType(filename) {
    const extension = filename.split('.').pop().toLowerCase();
    if (['doc', 'docx', 'pdf', 'txt', 'xls', 'xlsx', 'ppt', 'pptx'].includes(extension)) {
        return 'documents';
    } else if (['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'].includes(extension)) {
        return 'images';
    } else if (['mp4', 'avi', 'mov', 'mkv', 'wmv'].includes(extension)) {
        return 'videos';
    } else if (['mp3', 'wav', 'aac', 'flac'].includes(extension)) {
        return 'audio';
    } else {
        return 'dirs';
    }
}

document.getElementById('file-type-filter').addEventListener('change', function () {
    const selectedType = this.value;
    const fileListItems = document.querySelectorAll('#file-list li');

    fileListItems.forEach(function (item) {
        const fileType = getFileType(item.getAttribute('data-filetype'));
        if (selectedType === 'all' || fileType === selectedType) {
            item.classList.remove('hidden');
        } else {
            item.classList.add('hidden');
        }
    });
});