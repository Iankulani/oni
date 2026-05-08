# oni

<img width="436" height="424" alt="oni" src="https://github.com/user-attachments/assets/6feedcde-a154-4cbb-892c-adab129fba42" />

oni







[![GitHub stars](https://img.shields.io/github/stars/Iankulani/oni?style=for-the-badge&logo=github)](https://github.com/Iankulani/oni/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Iankulani/oni?style=for-the-badge&logo=github)](https://github.com/Iankulani/oni/network)
[![GitHub watchers](https://img.shields.io/github/watchers/Iankulani/oni?style=for-the-badge&logo=github)](https://github.com/Iankulani/oni/watchers)
[![GitHub contributors](https://img.shields.io/github/contributors/Iankulani/oni?style=for-the-badge&logo=github)](https://github.com/Iankulani/oni/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/Iankulani/oni?style=for-the-badge&logo=git)](https://github.com/Iankulani/oni/commits/main)
[![Docker Pulls](https://img.shields.io/badge/docker-available-blue?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/iankulaniking_phisher) <!-- Replace with actual Docker Hub link for oni if available -->
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-blue?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Iankulani/oni)
[![Python Version](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)








Local Installation
bash
# Clone repository
```bash
git clone https://github.com/Iankulani/oni.git
```
```bash
cd oni
```
# Run setup script
chmod +x setup.sh install.sh
./setup.sh

# Start ONI
python3 oni.py
Alpine Linux
bash
# Install directly on Alpine
apk add python3 py3-pip bash curl wget git nmap nikto hping3
pip3 install -r requirements.txt
python3 oni.py
📦 Installation Methods
# 1. Docker (Alpine-based)
```bash
docker build -f Dockerfile.alpine -t oni:alpine .
docker run -it --rm --cap-add=NET_ADMIN --cap-add=NET_RAW oni:alpine
```
# 2. Docker (Ubuntu-based)
```bash
docker build -f Dockerfile -t oni:ubuntu .
docker run -it --rm --cap-add=NET_ADMIN --cap-add=NET_RAW oni:ubuntu
```
# 3. Batch Installation Script
# One-command installation
```bash
curl -sSL https://gitlab.com/Iankulani/oni/-/raw/main/install.sh | bash
```

# Or with sudo
```bash
sudo bash install.sh --all
```

# 🔧 Configuration
```bash
Edit ~/.oni/config/config.json:

json
{
    "web_port": 5000,
    "phishing_port": 8080,
    "debug": false,
    "auto_block_threats": true,
    "bots": {
        "discord": {"enabled": true, "token": "YOUR_TOKEN"}
    }
}

```
# 📚 Commands
Category	Commands
* Network	ping, scan, nmap, traceroute, whois, dns
* Security	password, keylogger, nikto, traffic
* Spoofing	spoof_ip, arp_spoof, dns_spoof, spoof_mac
* SSH	ssh_add, ssh_exec, ssh_list, ssh_connect
* Phishing	generate_phishing_for_*, phishing_start_server
# System	status, threats, report, history
*🌐 Web Dashboard
```bash
Access the web interface at http://localhost:5000
```
# Features:

* Real-time terminal

* Statistics dashboard

* Charts and analytics

* Quick command buttons

# 🤖 Bot Configuration
Discord
```bash
# Start Discord bot
```bash
discord_token = "YOUR_BOT_TOKEN"
discord_prefix = "!"
```
# Telegram

# Start Telegram bot
```bash
telegram_api_id = 123456
telegram_api_hash = "YOUR_HASH"
telegram_bot_token = "BOT_TOKEN"
```
# WhatsApp
# Requires QR scan on first run
```bash
whatsapp_enabled = true
```
# 🛠️ Development

# Setup development environment
```bash
make install
make dev
```
# Run tests
```bash
make test
```
# Lint code
```bash
make lint
```
# Build Docker
make docker-build-alpine
📊 Monitoring
Prometheus metrics available at :5000/metrics

Health check endpoint at :5000/health

Real-time traffic monitoring

# 🔒 Security
Always use ONI in authorized environments only. Features include:

IP blocking and threat detection

Audit logging

Command history tracking

SSH key management

Encrypted configuration

📄 License
Accurate  Cyber Defense License

# ⚠️ Disclaimer
This tool is for educational and authorized security testing only. Users are responsible for compliance with all applicable laws.

# 📞 Support
Issues: GitLab Issues

Documentation: 
Email: 





























# How to clone the repo


# How to run
```bash
python oni
```
# Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Iankulani/oni&type=Date)](https://star-history.com/#Iankulani/oni&Date)
