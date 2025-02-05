document.getElementById("userInput").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        const userInput = this.value;
        this.value = "";

        // Display user message
        const userMessage = document.createElement("div");
        userMessage.className = "message user-message";
        userMessage.textContent = userInput;
        document.getElementById("chatbox").appendChild(userMessage);

        // Send user input to the server and get the response
        fetch("/get_response", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ user_input: userInput }),
        })
            .then((response) => response.json())
            .then((data) => {
                // Display bot response
                const botMessage = document.createElement("div");
                botMessage.className = "message bot-message";
                botMessage.textContent = data.response;
                document.getElementById("chatbox").appendChild(botMessage);

                // Scroll to the bottom of the chatbox
                document.getElementById("chatbox").scrollTop = document.getElementById("chatbox").scrollHeight;
            });
    }
});