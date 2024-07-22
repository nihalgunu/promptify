document.getElementById('send-button').addEventListener('click', sendMessage);

async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return;

    const chatLog = document.getElementById('chat-log');
    const userMessage = document.createElement('div');
    userMessage.textContent = 'You: ' + userInput;
    chatLog.appendChild(userMessage);

    try {
        const response = await fetch('http://localhost:9000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ inputs: userInput })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        const botMessage = document.createElement('div');
        botMessage.textContent = 'Bot: ' + result.generated_text;
        chatLog.appendChild(botMessage);

    } catch (error) {
        console.error('Error:', error);
        const errorMessage = document.createElement('div');
        errorMessage.textContent = 'Error: ' + error.message;
        chatLog.appendChild(errorMessage);
    }

    document.getElementById('user-input').value = '';
    chatLog.scrollTop = chatLog.scrollHeight;
}
