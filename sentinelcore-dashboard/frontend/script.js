document.addEventListener('DOMContentLoaded', () => {
  // Simulate dynamic data pull
  fetchLogs();
  setInterval(fetchLogs, 4000);
});

function fetchLogs() {
  document.getElementById('firewall-log').innerText = fakeFirewallLogs();
  document.getElementById('av-log').innerText = fakeAVLogs();
  document.getElementById('enc-log').innerText = fakeEncLogs();
  document.getElementById('auth-log').innerText = fakeAuthLogs();
  document.getElementById('ip-log').innerText = fakeIPLogs();
}

function fakeFirewallLogs() {
  return `[PORT 8080] Intrusion Attempt Blocked\n[PORT 22] SSH Brute Force Blocked\nStatus: Secured`;
}

function fakeAVLogs() {
  return `Scan Complete: 5 threats removed\nDB Version: 2.8.1\nNext Scan: In 24hrs`;
}

function fakeEncLogs() {
  return `Folder /docs/vault locked 🔒\nDrive D:/Encrypted\nAES-256 encryption complete`;
}

function fakeAuthLogs() {
  return `Login: Success (admin) [2FA verified]\nAccess Blocked: Unknown device (3 attempts)`;
}

function fakeIPLogs() {
  return `Trace: 192.168.1.13 (Local Host)\nBlocked: Malicious IP 185.12.23.4 (Russia)`;
}
