# Custom Python C2 Framework (Command & Control)

A lightweight, multi-threaded Command & Control (C2) framework written in Python. Designed to demonstrate the mechanics of reverse shells, beaconing, and remote command execution in Red Team engagements.

## 🧠 Educational Objective
Understanding how C2 frameworks (like Cobalt Strike or Sliver) operate under the hood is a critical skill for Red Teamers. This project demonstrates how an operator can manage multiple reverse shells simultaneously from a central listener.

## 🏗️ Architecture
- **`server.py`**: The C2 Listener. It runs on the attacker's Kali Linux machine, listens on port 4444, and uses multi-threading to handle multiple incoming connections. It provides an interactive prompt to issue commands.
- **`beacon.py`**: The Implant/Beacon. It runs on the victim machine, connects back to the server, and executes the commands received via `subprocess`.

## 🚀 Usage (In a safe local lab)
1. On your Kali machine, start the server: `python3 server.py`
2. On your victim machine (e.g., a Windows/Linux VM), run the beacon: `python3 beacon.py`
3. Once the connection is established, you can type commands (e.g., `whoami`, `ipconfig`, `ls`) into the server prompt and view the output instantly.

## 🛡️ Mitigation & Detection
To defend against such attacks, organizations should deploy Endpoint Detection and Response (EDR) tools, monitor for unusual outbound connections to non-standard ports, and restrict outbound traffic via firewalls.

## Disclaimer
This tool is strictly for authorized penetration testing, Red Team lab simulations, and educational purposes. Unauthorized use is illegal.
