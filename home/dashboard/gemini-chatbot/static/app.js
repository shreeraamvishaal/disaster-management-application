document.getElementById('send-button').addEventListener('click', async () => {
    const inputField = document.getElementById('user-input');
    const userMessage = inputField.value.trim();
    
    if (userMessage === '') return;

    // Display the user message in the chat area
    addMessage('You', userMessage);

    try {
        // Send the message to the chatbot
        const response = await getChatbotResponse(userMessage);
        addMessage('Chatbot', response);
    } catch (error) {
        console.error('Error fetching response:', error);
        addMessage('Chatbot', 'Sorry, there was an error.');
    }

    // Clear the input field
    inputField.value = '';
});

async function getChatbotResponse(message) {
    const apiUrl = 'http://localhost:5000/chat'; // Backend endpoint

    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: message }),
    });

    if (!response.ok) {
        throw new Error('Network response was not ok');
    }

    const data = await response.json();
    return data.response || 'Sorry, I could not understand that.';
}

function addMessage(sender, text) {
    const chatArea = document.getElementById('chat-area');
    const messageElement = document.createElement('div');
    messageElement.className = `mb-2 p-2 rounded-lg ${sender === 'You' ? 'bg-blue-100 text-blue-800' : 'bg-gray-100 text-gray-800'}`;
    messageElement.textContent = `${sender}: ${text}`;
    chatArea.appendChild(messageElement);
    chatArea.scrollTop = chatArea.scrollHeight;
}
