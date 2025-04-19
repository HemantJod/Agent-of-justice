function startTrial() {
  document.querySelector("button").style.display = "none";

  fetch("http://127.0.0.1:5000/trial/start")
    .then(response => response.json())
    .then(data => {
      showMessagesSequentially(data, 0);
    })
    .catch(error => {
      console.error("Error fetching trial data:", error);
      alert("Failed to start trial. Is your Flask server running?");
    });
}

function showMessagesSequentially(messages, index) {
  if (index < messages.length) {
    const messageDiv = document.createElement("div");
    messageDiv.textContent = `${messages[index].role}: ${messages[index].message}`;
    document.getElementById("trial-logs").appendChild(messageDiv);
    setTimeout(() => {
      showMessagesSequentially(messages, index + 1);
    }, 4000); // delay between messages (4 seconds)
  }
}
