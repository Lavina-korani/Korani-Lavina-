document.getElementById('infoButton').addEventListener('click', function() {
    const infoDiv = document.getElementById('info');
    if (infoDiv.style.display === 'none') {
        infoDiv.style.display = 'block';
        infoDiv.innerHTML = `
            <p>Welcome to the Sentiment Analysis Application!</p>
            <p>Choose one of the modules to start analyzing:</p>
            <ul>
                <li><strong>Text Sentiment Analysis:</strong> Analyze the sentiment of textual content.</li>
                <li><strong>Audio Sentiment Analysis:</strong> Analyze the sentiment of spoken words.</li>
                <li><strong>Image Sentiment Analysis:</strong> Analyze the sentiment conveyed in images.</li>
            </ul>
        `;
    } else {
        infoDiv.style.display = 'none';
    }
});