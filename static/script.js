document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", function(e) {
  if (e.key === "Enter") sendMessage();
});

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  const chatBox = document.getElementById("chat-box");

  if (!message) return;

  appendMessage("YOU: " + message, "user");
  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await response.json();

    appendMessage("AI: " + (data.reply || data.error), "ai");
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (err) {
    appendMessage("Error: " + err.message, "ai");
  }
}

function appendMessage(text, type) {
  const chatBox = document.getElementById("chat-box");
  const msgDiv = document.createElement("div");
  msgDiv.textContent = text;
  msgDiv.classList.add("message", type);
  chatBox.appendChild(msgDiv);
}
