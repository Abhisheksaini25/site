document.getElementById('saveButton').addEventListener('click', function() {
    const textInput = document.getElementById('textInput').value;
    const savedText = document.getElementById('savedText');

    if (textInput.trim() !== '') {
        savedText.textContent = textInput;
    } else {
        savedText.textContent = 'No text saved yet.';
    }

    document.getElementById('textInput').value = ''; // Clear the text box
});
