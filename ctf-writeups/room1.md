# 🧠 CTF Challenge: Example Room 1

### 🎯 Objective
Capture the flag by exploiting a vulnerable web application.

### 🧰 Tools Used
- Nmap
- Gobuster
- Burp Suite

### 🔍 Enumeration
- nmap -sC -sV target
- discovered open ports 22,80

### ⚙️ Exploitation
- found directory /admin using gobuster
- used default creds to log in

### 🪪 Privilege Escalation
- checked sudo -l
- no escalation in this demo

### 📚 Lessons Learned
- always enumerate web directories
