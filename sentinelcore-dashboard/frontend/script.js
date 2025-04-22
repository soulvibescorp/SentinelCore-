document.addEventListener('DOMContentLoaded', () => {
  fetchLogs();
  setInterval(fetchLogs, 5000);  // refresh every 5s
});

function fetchLogs() {
  fetchAndDisplay('/logs/firewall', 'firewall-log');
  fetchAndDisplay('/logs/antivirus', 'av-log');
  fetchAndDisplay('/logs/encryption', 'enc-log');
  fetchAndDisplay('/logs/auth', 'auth-log');
  fetchAndDisplay('/logs/ip', 'ip-log');
}

function fetchAndDisplay(endpoint, elementId) {
  fetch(`http://127.0.0.1:5000${endpoint}`)
    .then(response => response.json())
    .then(data => {
      document.getElementById(elementId).innerText = data.join('\n');
    })
    .catch(() => {
      document.getElementById(elementId).innerText = '⚠️ Server Error';
    });
}
