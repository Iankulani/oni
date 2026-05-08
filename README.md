# oni

<img width="436" height="424" alt="oni" src="https://github.com/user-attachments/assets/6feedcde-a154-4cbb-892c-adab129fba42" />




[![GitHub stars](https://img.shields.io/github/stars/Iankulani/oni?style=for-the-badge&logo=github)](https://github.com/Iankulani/oni/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Iankulani/oni?style=for-the-badge&logo=github)](https://github.com/Iankulani/oni/network)
[![GitHub watchers](https://img.shields.io/github/watchers/Iankulani/oni?style=for-the-badge&logo=github)](https://github.com/Iankulani/oni/watchers)
[![GitHub contributors](https://img.shields.io/github/contributors/Iankulani/oni?style=for-the-badge&logo=github)](https://github.com/Iankulani/oni/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/Iankulani/oni?style=for-the-badge&logo=git)](https://github.com/Iankulani/oni/commits/main)
[![Docker Pulls](https://img.shields.io/badge/docker-available-blue?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/iankulaniking_phisher) <!-- Replace with actual Docker Hub link for oni if available -->
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-blue?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Iankulani/oni)
[![Python Version](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)




ONI (オニ) is not merely a cybersecurity tool—it is a paradigm shift in how security professionals, ethical hackers, and researchers interact with the digital battlefield. Named after the fearsome demons of Japanese folklore, ONI embodies the perfect balance of destruction and protection, chaos and order, offense and defense. Like its mythological namesake who punishes evil while protecting the righteous, ONI serves as both a sword and a shield in the hands of those who understand its power.

This comprehensive cybersecurity command center integrates over 5,000 security commands, spanning everything from basic network reconnaissance to advanced exploitation techniques, all wrapped in a sleek, demonic interface that demands respect. Whether you are a Black Hat seeking to understand vulnerabilities, a Red Hat conducting authorized penetration tests, or a White Hat defending critical infrastructure, ONI becomes an extension of your will—a digital Oni that fights alongside you in the eternal battle for cyberspace supremacy.

🎭 THE LEGEND OF ONI
Mythological Origins
In Japanese mythology, the Oni (鬼) are fearsome demons known for their immense strength, magical abilities, and dual nature. They punish the wicked, guard the gates of hell, yet can become protectors of temples and loyal servants to those who earn their respect. They are creatures of raw power, unpredictability, and absolute loyalty to their master.

ONI the cybersecurity tool embodies these same characteristics:

Mythological Trait	Cybersecurity Parallel
Supernatural Strength	5000+ security commands at your fingertips
Shapeshifting Ability	Multi-platform integration (Telegram, Discord, Slack, WhatsApp, iMessage, Signal)
Demonic Cunning	Advanced social engineering and phishing suite
Hellfire Breath	Real traffic generation and stress testing
Protective Nature	Threat detection, IP blocking, security monitoring
Loyalty to Master	Complete command history, audit trails, reporting
Terror Inducing	Psychological impact on adversaries during red team exercises
🔥 THE DEMON'S PURPOSE
Why ONI Exists
The digital world has become a battleground where nation-states, criminal organizations, hacktivists, and lone wolves clash daily. Traditional security tools are fragmented—you need Nmap for scanning, Metasploit for exploitation, Burp Suite for web testing, and dozens more tools for different tasks. This fragmentation creates inefficiency, slows response times, and leaves gaps in security postures.

ONI unifies the battlefield.

Imagine commanding an entire cybersecurity arsenal from a single terminal. Imagine executing complex penetration tests from your phone via Telegram while commuting. Imagine your Discord server becoming a security operations center where commands flow like poetry and results appear like magic. Imagine launching social engineering campaigns, generating realistic traffic, spoofing identities, and detecting threats—all from one unified interface.

This is ONI.

🗡️ CORE CAPABILITIES
1. The Command Arsenal (5000+ Security Commands)
ONI's command system is built like a demon's grimoire—ancient, powerful, and extensive. Every command is optimized for speed, reliability, and comprehensive output formatting.

# Network Reconnaissance Commands
```bash
ping <target>              - ICMP echo requests for host discovery
scan <target> [ports]      - Comprehensive port scanning (1-1000 default)
nmap <target> [flags]      - Full Nmap integration with all options
traceroute <target>        - Network path discovery and latency analysis
whois <domain>             - Domain ownership and registration lookup
dns <domain>               - DNS record enumeration (A, AAAA, MX, TXT, NS)
dig <domain> [type]        - Advanced DNS interrogation
resolve <hostname>         - IP resolution and reverse DNS
location <ip>              - IP geolocation, ISP, coordinates
subdomain <domain>         - Subdomain enumeration (1000+ wordlist)
crt <domain>               - Certificate transparency log search
shodan <query>             - Shodan IoT search engine integration
censys <query>             - Censys internet-wide scan database
Vulnerability Assessment
text
nikto <target>             - Complete web server vulnerability scanning
nikto_ssl <target>         - SSL/TLS misconfiguration detection
nikto_sql <target>         - SQL injection vulnerability scanning
nikto_xss <target>         - Cross-site scripting detection
nikto_cgi <target>         - CGI vulnerability assessment
nuclei <target>            - Nuclei template-based scanning
whatweb <target>           - Web technology fingerprinting
wpscan <target>            - WordPress vulnerability scanner
joomscan <target>          - Joomla security assessment
droopescan <target>        - CMS vulnerability scanner
Exploitation Framework
ssh_add <name> <host> <user> [pass] - Add SSH target to arsenal
ssh_exec <id> <command>             - Execute remote commands stealthily
ssh_brute <target> <wordlist>       - SSH credential brute-forcing
ssh_tunnel <id> <local> <remote>    - SSH port forwarding tunnel
reverse_shell <lhost> <lport>       - Generate reverse shell payloads
bind_shell <port>                   - Create bind shell listener
web_shell <url> <param> <cmd>       - Web shell command execution
```
# 2. Multi-Platform Demon Integration
ONI doesn't confine you to a single terminal. It spreads across communication platforms like a demon possessing multiple vessels, allowing you to command your cybersecurity army from anywhere.

# Discord Integration

python
# ONI becomes a Discord bot with full permissions
```bash
!ping 8.8.8.8           # Executed in any Discord channel
!scan target.com        # Results returned as formatted messages
!traffic                # Real-time network statistics
!status                 # Complete system status
!phishing facebook      # Generate Facebook phishing page
```
# Discord commands support:

Role-based access control (only authorized users can execute commands)

* Rich embeds for formatted command outputs

* Thread support for long-running commands

* Slash commands for native Discord integration

* Voice channel alerts for critical threat detections

# Telegram Integration
```bash
/ssh_list               # List all managed SSH servers
/ssh_exec myserver ls -la  # Execute on remote server
/nikto example.com      # Vulnerability scan via Telegram
/report                 # Generate and send security report
/add_ip 192.168.1.100   # Add IP to monitoring
```
# Telegram features:

* Inline keyboards for command suggestions

* File uploads for downloading scan results

* Voice commands (Telegram voice-to-text)

* Bot API 5.0+ support with full features

* Secret chats for sensitive command output

* Slack Integration
```bash
!whois example.com        # WHOIS lookup in Slack channel
!location 8.8.8.8       # IP geolocation
!threats                # Recent threat intelligence
!block_ip 1.2.3.4       # Block suspicious IP
```
# Slack capabilities:

* Interactive buttons for command execution

* Modal dialogs for complex command parameters

* Workflow integration with Slack automation

* Enterprise Grid support for large organizations

# WhatsApp Integration
```bash
> ping cloudflare.com    # WhatsApp message to ONI
> status                 # System health check
> keylogger start        # Start keylogging (authorized only)
> traffic_status         # Active traffic generators
```
# iMessage Integration (macOS only)
```bash
$ ssh_connect myserver   # iMessage command
$ generate_phishing gmail
$ phishing_start_server abc123
```
# Signal Integration
```bash
% nmap -sV target.com    # Signal private messenger
% report                 # Encrypted security report
```
# Google Chat Integration
```bash
@oni ping 1.1.1.1        # Google Chat mention
@oni status              # Workspace integration
@oni list_ips            # IP management
```
# 3. Social Engineering Suite - The Demon's Deception
Like the mythological Oni who disguises itself to trick humans, ONI's social engineering module is designed for authorized security awareness training and red team operations.

Phishing Template Library (100+ Templates)
ONI comes pre-loaded with 100+ professionally crafted phishing templates for:

# Social Media Platforms:

* Facebook (complete clone with OAuth flow simulation)

* Instagram (mobile-responsive clone)

* Twitter/X (dark mode and light mode variants)

* LinkedIn (corporate login portal clone)

* TikTok (youth-targeted template)

* Snapchat (camera-focused design)

* Reddit (Reddit Premium phishing)

# Email Services:

* Gmail (modern Material Design UI)

* Outlook/Office 365 (corporate login portal)

* Yahoo Mail (legacy and new versions)

* ProtonMail (privacy-focused template)

* iCloud (Apple ecosystem login)

# Financial Services:

* PayPal (complete transaction simulation)

* Bank of America (regional variants)

* Chase Bank (credit card login portal)

* Wells Fargo (business banking template)

* Crypto Wallets (MetaMask, TrustWallet, Coinbase)

* Bitcoin exchanges (Binance, Coinbase Pro, Kraken)

# E-commerce:

* Amazon (Prime login and payment)

* eBay (seller portal and buyer login)

* Alibaba (B2B login portal)

* Shopify (admin login clone)

* Walmart (shopping account phishing)

# Corporate Services:

* Microsoft 365 (Azure AD login)

* Google Workspace (G Suite admin portal)

* Salesforce (CRM login portal)

* Zoom (meeting authentication)

* Teams (Microsoft Teams login)

* Slack (workspace sign-in)

* Dropbox (file access phishing)

* Box (enterprise storage login)

# Custom Templates:

Generic VPN login (BYOD policies)

IT Support Portal (help desk simulation)

HR Benefits Portal (employee data harvesting)

COVID-19 Health Screening (health data phishing)

Software Update Portal (credential harvesting)

Wi-Fi Captive Portal (rogue AP simulation)

Credential Capture System
python
# Each captured credential includes:
```bash
{
    "timestamp": "2024-01-15 14:23:45",
    "username": "victim@example.com",
    "password": "UserPassword123!",
    "ip_address": "192.168.1.100",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "geo_location": "New York, NY",
    "referer": "https://facebook.com/login",
    "session_id": "abc123def456",
    "screen_resolution": "1920x1080",
    "browser_fingerprint": "hash_of_browser_features"
}
```
# QR Code Generation
ONI generates QR codes for phishing links, enabling:

* Mobile device targeting (scan to login)

* Print-based phishing (posters, flyers)

* Physical penetration testing (badge QR codes)

* Event-based social engineering (conference Wi-Fi)

* URL Shortening Integration
* TinyURL - Basic shortening

* Bit.ly - Click tracking and analytics

* Rebrandly - Custom branded domains

* Short.io - Analytics and geotargeting

* Custom short domains (your-own-domain.com/abc)

# 4. Spoofing Engine - The Demon's Disguise
ONI's spoofing capabilities allow security professionals to test network defenses against impersonation attacks.

IP Spoofing
```bash
spoof_ip 192.168.1.100 10.0.0.1 8.8.8.8
Spoofs source IP address in crafted packets
```

Bypasses simple IP-based allowlisting

Tests network intrusion detection systems

Identifies trust-based authentication weaknesses

# MAC Address Spoofing

```bash
spoof_mac eth0 00:11:22:33:44:55
Changes network interface MAC address
```
Bypasses MAC filtering

Tests port security configurations

Evades network access controls

ARP Spoofing (Man-in-the-Middle)
```bash
arp_spoof 192.168.1.100 192.168.1.1
```
Intercepts traffic between target and gateway

Enables traffic inspection and modification

Tests ARP inspection security features

Simulates MITM attack scenarios

DNS Spoofing
```bash
dns_spoof facebook.com 192.168.1.50
```
Redirects domain queries to malicious servers

Tests DNS security configurations

Simulates DNS poisoning attacks

Validates DNSSEC implementations

# 5. Real Traffic Generation
Like the Oni's ability to create chaos wherever it walks, ONI can generate realistic network traffic for testing and simulation.

# Traffic Types Available
* Traffic Type	Protocol	Description	Use Case
* ICMP	ICMP	Ping flood simulation	DDoS testing, firewall rules
* TCP SYN	TCP	Half-open connection flood	SYN flood mitigation testing
* TCP ACK	TCP	Acknowledgment packet flood	Stateful firewall testing
* TCP Connect	TCP	Full connection flood	Load balancer testing
* UDP	UDP	Datagram flood	Amplification attack testing
* HTTP GET	HTTP	Web page requests	Web server stress testing
* HTTP POST	HTTP	Form submission flood	Application DDoS testing
* HTTPS	HTTPS	Encrypted web traffic	SSL/TLS performance testing
* DNS	DNS	Recursive query flood	DNS server stress testing
* ARP	ARP	Address resolution flood	Switch CAM table overflow
 
# Traffic Generation Example

# Generate 60 seconds of HTTP GET traffic to web server
```bash
generate_traffic http_get 192.168.1.100 60 80 500
```
# Simulate DNS amplification attack (authorized testing)
```bah
generate_traffic dns 8.8.8.8 30 53 1000
```
# Test firewall with mixed traffic types
```bash
generate_traffic tcp_syn target.com 120
generate_traffic udp target.com 120 53
generate_traffic icmp target.com 120
```
# 6. Keylogger - The Silent Watcher
ONI's keylogger module operates like a hidden Oni watching from the shadows.

# Features
* Real-time keystroke capture with timestamps
* Window title tracking (which application is active)
* Toggle activation (F9 key enables/disables)
* Remote delivery via webhook (Discord, Slack, Telegram)
* Encrypted local storage (AES-256)
* Batch delivery (50 keystrokes per batch)
* Special key recording (Enter, Backspace, Tab, Arrows)

# Ethical Use Only
ONI's keylogger includes:

* Visual indicators when logging (terminal messages)

* Consent verification before activation

* Audit logging of all logging periods

* Auto-shutdown after specified duration

* Remote kill switch capability

# 🎭 THE THREE FACES OF ONI
Like the mythological Oni who serves different masters, ONI adapts to the user's ethical alignment.

Black Hat Oni - The Destructive Demon
For security researchers understanding attacker methodologies:

# Reconnaissance phase
```bash
> scan corporate.target.com -p- -T4
> whois corporate.target.com
> subdomain corporate.target.com
```
# Vulnerability identification
```bash
> nikto corporate.target.com
> generate_phishing_for_office365
```
# Exploitation (authorized)
```bash
> generate_traffic http_get target.com 300
> arp_spoof 192.168.1.100 192.168.1.1
```
Warning: Black Hat use is illegal without authorization. ONI includes logging that documents all activities for legal compliance.

Red Hat Oni - The Testing Demon
For authorized penetration testers and red team operators:

# Authorized assessment
```bash
> ssh_add o365test login.microsoftonline.com testuser
> ssh_exec o365test "whoami /all"
```
# Social engineering simulation
```bash
> generate_phishing_for_linkedin
> phishing_start_server link_id 8080
```
# Traffic generation for load testing
```bash
> generate_traffic https corporate.com 300 443
```
# Red Hat features include:

* Comprehensive audit trails for client reports

* Scheduled scans for continuous testing

* Automated reporting (PDF, HTML, JSON)

* Remediation tracking (retest capabilities)

* White Hat Oni - The Protective Demon

For defenders and security operations:

# Threat detection
```bash
> add_ip 45.33.22.11 "Suspicious scanner"
> block_ip 45.33.22.11 "Port scan detected"
> threats                    # Review recent threats
```
# Security monitoring
```bash
> traffic                   # Network traffic analysis
> status                    # System health check
```
# Incident response
```bash
> report                    # Generate incident report
> history 100              # Review command history
> keylogger start          # Capture attacker activity
```
# White Hat capabilities include:

* Threat intelligence integration

* Automated blocking of malicious IPs

* Real-time alerting via multiple platforms

# Forensic evidence collection

* Compliance reporting (GDPR, HIPAA, PCI-DSS)

# 🏛️ USE CASES AND APPLICATIONS
# Cybersecurity Drills and Exercises


# Capture The Flag (CTF) Events
CTF challenges can be executed via ONI commands

Team collaboration through Discord/Slack integration

Score tracking and leaderboard integration

Automated challenge deployment

* Red Team vs Blue Team Exercises
* Red Team uses offensive modules (spoofing, phishing, exploitation)

* Blue Team uses defensive modules (monitoring, blocking, detection)

* Real-time communication between teams

# Automated after-action reports

# Military and Government Training
* Secure deployment on classified networks
* Custom module development
* Integration with existing training ranges
* Compliance with DoD/NCSC standards

# Corporate Security Testing
Internal Penetration Testing

# Corporate intranet assessment
```bash
> scan 10.0.0.0/24
> ssh_add finance-server 10.0.0.50 admin
> ssh_exec finance-server "cat /etc/passwd"
```
# External Penetration Testing

# Internet-facing assets
```bash
> nmap -sV -sC company.com
> nikto company.com
> generate_phishing_for_sharepoint
```
# Educational Institutions
Cybersecurity Courses
* Students learn security concepts through hands-on commands
* Instructors monitor student activity via Discord/Slack
* Automated grading of security assignments
* Virtual lab integration
* Security Awareness Training
* Simulated phishing campaigns using 100+ templates

# User behavior analytics and reporting

* Automated retraining for vulnerable users

* ROI-based security metrics

* Security Operations Centers (SOC)
# Incident Response

* Rapid deployment of blocking rules

* Automated threat hunting queries

* Integration with SIEM platforms

* Real-time collaboration tools

# Threat Hunting

* Proactive compromise assessment

* IOC scanning across enterprise

* Suspicious behavior detection

* Advanced persistent threat (APT) hunting

# 📊 TECHNICAL ARCHITECTURE
# System Requirements
# Minimum (Container/Docker)
* 1 CPU core

* 1 GB RAM

* 1 GB storage

# Network: Standard outbound/inbound

# Recommended (Production)

* 4+ CPU cores

* 8+ GB RAM

* 20+ GB SSD storage

* 1 Gbps network connection

# Supported Platforms

* Platform	Support Level	Notes
* Alpine Linux	Full	Recommended for containers
* Ubuntu 20.04+	Full	Best for bare metal
* Debian 11+	Full	Stable and reliable
* CentOS 7+	Partial	Some packages limited
* RHEL 8+	Partial	Enterprise support
* Arch Linux	Full	Rolling release
* macOS 11+	Partial	Limited network features
* Windows 10+	Limited	WSL2 required
* Database Schema
# ONI uses SQLite3 for lightweight, zero-configuration storage:

-- Command history (all commands executed)
```bash
CREATE TABLE command_history (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    command TEXT,
    source TEXT,  -- local, discord, telegram, etc.
    platform TEXT,
    success BOOLEAN,
    output TEXT,
    execution_time REAL
);
```
-- SSH server management
```bash
CREATE TABLE ssh_servers (
    id TEXT PRIMARY KEY,
    name TEXT,
    host TEXT,
    port INTEGER,
    username TEXT,
    password TEXT,
    key_file TEXT,
    use_key BOOLEAN,
    status TEXT,
    last_used DATETIME
);
```
-- Phishing campaign tracking
```bash
CREATE TABLE phishing_links (
    id TEXT PRIMARY KEY,
    platform TEXT,
    phishing_url TEXT,
    created_at DATETIME,
    clicks INTEGER,
    active BOOLEAN
);

-- Captured credentials
CREATE TABLE captured_credentials (
    id INTEGER PRIMARY KEY,
    phishing_link_id TEXT,
    timestamp DATETIME,
    username TEXT,
    password TEXT,
    ip_address TEXT,
    user_agent TEXT
);

-- Threat intelligence
CREATE TABLE threats (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    threat_type TEXT,
    source_ip TEXT,
    severity TEXT,
    description TEXT,
    action_taken TEXT
);

-- Managed IPs (blocking/monitoring)
CREATE TABLE managed_ips (
    id INTEGER PRIMARY KEY,
    ip_address TEXT UNIQUE,
    added_by TEXT,
    added_date DATETIME,
    is_blocked BOOLEAN,
    block_reason TEXT,
    alert_count INTEGER
);
```
# API Endpoints
ONI provides a RESTful API for integration:

# Endpoint	Method	Description
```bash
/api/command	POST	Execute security command
/api/stats	GET	System statistics
/api/threats	GET	Recent threat list
/api/ips	GET	Managed IPs
/api/block	POST	Block IP address
/api/report	GET	Generate security report
/api/health	GET	Health check
/api/metrics	GET	Prometheus metrics
```
# 💀 THE ONI MANIFESTO
# Our Philosophy
ONI was created with a simple belief: security tools should be accessible, powerful, and ethical.

We reject the gatekeeping that keeps security tools locked behind expensive licenses. We reject the fragmentation that forces professionals to learn dozens of incompatible interfaces. We reject the notion that security must choose between power and usability.

ONI is for everyone who fights for a safer internet.

# Ethical Guidelines
#  Users of ONI must adhere to:

* Never test without permission - Always obtain written authorization

* Protect captured data - Credentials and sensitive data must be destroyed after testing

* Report responsibly - Discovered vulnerabilities go to proper disclosure channels

* Respect boundaries - Do not attack infrastructure you don't own or have permission to test

* Leave no trace - Remove backdoors, shells, and test artifacts after completion

# The Warning
"With great power comes great responsibility. ONI is a weapon—treat it as such. The creators assume no liability for misuse. You alone are responsible for your actions. Always follow the law. Always act ethically."

# 🚀 GETTING STARTED


# How to clone the repo
```bash
git clone https://github.com/Iankulani/oni.git
cd oni
```
# How to run
```bash
python oni.py
```            
# After installation, type:
```bash
help                    # View all commands
status                  # Check system status
ping 8.8.8.8           # Test connectivity
scan localhost          # Scan your own system
```
# Connect Your Bots

# Discord
```bash
discord_token = "YOUR_BOT_TOKEN"
```
# Telegram
```bash
telegram_api_id = 123456
telegram_api_hash = "YOUR_HASH"
```
# Start all bots simultaneously

# 🔮 THE FUTURE OF ONI

* AI-Powered Suggestions - Machine learning command recommendations

* Blockchain Audit Trails - Immutable command logging

* Cloud Deployment - AWS, Azure, GCP native support

* Mobile App - iOS and Android native command center

* Plugin System - Community-developed modules

* Dark Web Monitoring - OSINT integration

* Zero-Day Exploit Database - Curated exploit collection


Export Controls
ONI contains strong cryptography and may be subject to export controls in certain jurisdictions. Users are responsible for compliance.

# 📞 FINAL WORDS
ONI is more than a tool—it's a companion in the never-ending battle for digital security. Whether you're defending a multinational corporation, teaching the next generation of security professionals, or testing the resilience of critical infrastructure, ONI stands ready.

The Oni watches. The Oni protects. The Oni strikes when necessary.

Welcome to the demon's army.

# Connect With Us
* Website: 
* GitLab: 
* Discord: 
* Telegram: 
* Signal: 
* Twitter/X: 
* Email: 


# Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Iankulani/oni&type=Date)](https://star-history.com/#Iankulani/oni&Date)
