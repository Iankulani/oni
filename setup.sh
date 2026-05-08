#!/bin/bash
# setup.sh - Complete setup script for ONI

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${RED}"
cat << "EOF"
   ╔═══════════════════════════════════════════════════════════════╗
   ║                    👹 ONI SETUP SCRIPT 👹                     ║
   ║              Cybersecurity Command Center Installer          ║
   ╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   echo -e "${YELLOW}Warning: Running as root is not recommended${NC}"
fi

# Detect OS
detect_os() {
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        OS=$ID
        VER=$VERSION_ID
    elif [[ -f /etc/alpine-release ]]; then
        OS="alpine"
    else
        OS=$(uname -s)
    fi
    echo -e "${GREEN}Detected OS: $OS${NC}"
}

# Install for Alpine Linux
install_alpine() {
    echo -e "${BLUE}Installing for Alpine Linux...${NC}"
    
    sudo apk update
    sudo apk add --no-cache \
        python3 py3-pip python3-dev \
        bash curl wget git \
        nmap nmap-scripts nikto \
        hping3 tcpdump net-tools iproute2 \
        iptables openssh-client openssh-server \
        whois bind-tools dnsmasq macchanger \
        arp-scan dsniff traceroute procps \
        netcat-openbsd socat jq vim nano \
        sudo ca-certificates build-base \
        libffi-dev openssl-dev cargo \
        linux-headers libpcap-dev pcre-dev \
        chromium chromium-chromedriver xvfb
    
    echo -e "${GREEN}✅ Alpine dependencies installed${NC}"
}

# Install for Ubuntu/Debian
install_ubuntu() {
    echo -e "${BLUE}Installing for Ubuntu/Debian...${NC}"
    
    sudo apt-get update
    sudo apt-get install -y \
        python3 python3-pip python3-dev python3-venv \
        bash curl wget git \
        nmap nikto hping3 tcpdump \
        net-tools iproute2 iptables \
        openssh-client openssh-server \
        whois dnsutils dnsmasq \
        macchanger arp-scan dsniff \
        traceroute procps netcat \
        socat jq vim nano sudo \
        ca-certificates build-essential \
        libffi-dev libssl-dev rustc \
        cargo linux-headers-generic \
        libpcap-dev libpcre3-dev \
        chromium-browser chromium-chromedriver xvfb
    
    echo -e "${GREEN}✅ Ubuntu/Debian dependencies installed${NC}"
}

# Install for RHEL/CentOS/Fedora
install_rhel() {
    echo -e "${BLUE}Installing for RHEL/CentOS/Fedora...${NC}"
    
    sudo dnf install -y \
        python3 python3-pip python3-devel \
        bash curl wget git \
        nmap nikto hping3 tcpdump \
        net-tools iproute iptables \
        openssh-clients openssh-server \
        whois bind-utils dnsmasq \
        macchanger arp-scan dsniff \
        traceroute procps-ng nc \
        socat jq vim nano sudo \
        ca-certificates gcc gcc-c++ \
        libffi-devel openssl-devel \
        cargo kernel-headers libpcap-devel \
        pcre-devel chromedriver chromium \
        xorg-x11-server-Xvfb
    
    echo -e "${GREEN}✅ RHEL dependencies installed${NC}"
}

# Install for Arch Linux
install_arch() {
    echo -e "${BLUE}Installing for Arch Linux...${NC}"
    
    sudo pacman -S --noconfirm \
        python python-pip python-virtualenv \
        bash curl wget git \
        nmap nikto hping3 tcpdump \
        net-tools iproute2 iptables \
        openssh whois bind-tools \
        dnsmasq macchanger arp-scan \
        dsniff traceroute procps-ng \
        netcat socat jq vim nano \
        sudo ca-certificates base-devel \
        libffi openssl rust \
        libpcap pcre \
        chromium chromedriver xorg-server-xvfb
    
    echo -e "${GREEN}✅ Arch dependencies installed${NC}"
}

# Install for macOS
install_macos() {
    echo -e "${BLUE}Installing for macOS...${NC}"
    
    if ! command -v brew &> /dev/null; then
        echo -e "${YELLOW}Installing Homebrew...${NC}"
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    brew install \
        python3 nmap nikto hping3 \
        tcpdump net-tools openssh \
        whois bind dnsmasq macchanger \
        arp-scan traceroute \
        netcat socat jq vim \
        ca-certificates rust libpcap \
        pcre chromedriver chromium
    
    echo -e "${GREEN}✅ macOS dependencies installed${NC}"
}

# Create virtual environment
setup_venv() {
    echo -e "${BLUE}Setting up Python virtual environment...${NC}"
    
    if [[ ! -d "venv" ]]; then
        python3 -m venv venv
    fi
    
    source venv/bin/activate
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
    
    echo -e "${GREEN}✅ Virtual environment created${NC}"
}

# Create configuration directories
create_directories() {
    echo -e "${BLUE}Creating directories...${NC}"
    
    mkdir -p ~/.oni/{config,data,logs,reports,keylogs,payloads,workspaces,scans,nikto_results,whatsapp_session,phishing_pages,phishing_templates,captured_credentials,ssh_keys,ssh_logs,time_history,wordlists,web_static,traffic_logs}
    
    echo -e "${GREEN}✅ Directories created${NC}"
}

# Create default configuration
create_config() {
    echo -e "${BLUE}Creating default configuration...${NC}"
    
    cat > ~/.oni/config/config.json << 'EOF'
{
    "version": "1.0.0",
    "web_port": 5000,
    "phishing_port": 8080,
    "api_port": 8081,
    "debug": false,
    "log_level": "INFO",
    "max_ssh_connections": 5,
    "keylogger_enabled": false,
    "traffic_monitor_enabled": true,
    "auto_block_threats": false,
    "threat_severity_threshold": "medium",
    "database": {
        "path": "~/.oni/data/oni.db",
        "backup_interval": 86400
    },
    "notifications": {
        "email": {
            "enabled": false,
            "smtp_server": "",
            "smtp_port": 587,
            "username": "",
            "password": "",
            "recipients": []
        },
        "webhook": {
            "enabled": false,
            "url": ""
        }
    },
    "bots": {
        "discord": {"enabled": false, "token": "", "prefix": "!"},
        "telegram": {"enabled": false, "api_id": "", "api_hash": "", "bot_token": ""},
        "slack": {"enabled": false, "token": "", "channel": "general"},
        "whatsapp": {"enabled": false},
        "imessage": {"enabled": false},
        "signal": {"enabled": false},
        "google_chat": {"enabled": false, "credentials_file": ""}
    },
    "spoofing": {
        "default_interface": "eth0",
        "arpspoof_enabled": true
    },
    "traffic_generation": {
        "max_duration": 300,
        "default_packet_rate": 100,
        "max_concurrent": 10
    },
    "phishing": {
        "default_port": 8080,
        "ssl_enabled": false,
        "ssl_cert": "",
        "ssl_key": ""
    }
}
EOF
    
    echo -e "${GREEN}✅ Configuration created${NC}"
}

# Create systemd service
create_service() {
    echo -e "${BLUE}Creating systemd service...${NC}"
    
    if [[ -d "/etc/systemd/system" ]]; then
        sudo cat > /etc/systemd/system/oni.service << 'EOF'
[Unit]
Description=ONI Cybersecurity Command Center
After=network.target

[Service]
Type=simple
User=oni
WorkingDirectory=/opt/oni
Environment="PATH=/opt/oni/venv/bin"
ExecStart=/opt/oni/venv/bin/python3 /opt/oni/oni.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
        
        sudo systemctl daemon-reload
        echo -e "${GREEN}✅ Systemd service created${NC}"
        echo -e "${YELLOW}Run: sudo systemctl enable oni && sudo systemctl start oni${NC}"
    fi
}

# Create Docker Compose file
create_docker_compose() {
    echo -e "${BLUE}Creating docker-compose.yml...${NC}"
    
    cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  oni-alpine:
    build:
      context: .
      dockerfile: Dockerfile.alpine
    container_name: oni-alpine
    restart: unless-stopped
    ports:
      - "5000:5000"
      - "8080:8080"
      - "8081:8081"
    volumes:
      - oni_data:/opt/oni/data
      - oni_logs:/opt/oni/logs
      - oni_reports:/opt/oni/reports
      - oni_config:/opt/oni/config
    environment:
      - ENVIRONMENT=production
      - LOG_LEVEL=INFO
      - WEB_PORT=5000
    cap_add:
      - NET_ADMIN
      - NET_RAW
      - SYS_ADMIN
    networks:
      - oni_network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  oni-ubuntu:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: oni-ubuntu
    restart: unless-stopped
    ports:
      - "5001:5000"
      - "8082:8080"
    volumes:
      - oni_ubuntu_data:/opt/oni/data
      - oni_ubuntu_logs:/opt/oni/logs
    cap_add:
      - NET_ADMIN
      - NET_RAW
    networks:
      - oni_network

  redis:
    image: redis:7-alpine
    container_name: oni-redis
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - oni_network

  postgres:
    image: postgres:16-alpine
    container_name: oni-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: oni
      POSTGRES_PASSWORD: oni_secure_password
      POSTGRES_DB: oni_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - oni_network

  nginx:
    image: nginx:alpine
    container_name: oni-nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - oni-alpine
    networks:
      - oni_network

networks:
  oni_network:
    driver: bridge

volumes:
  oni_data:
  oni_logs:
  oni_reports:
  oni_config:
  oni_ubuntu_data:
  oni_ubuntu_logs:
  redis_data:
  postgres_data:
EOF
    
    echo -e "${GREEN}✅ docker-compose.yml created${NC}"
}

# Create entrypoint script
create_entrypoint() {
    cat > entrypoint.sh << 'EOF'
#!/bin/bash

set -e

echo "👹 Starting ONI Cybersecurity Command Center"

# Create necessary directories
mkdir -p /opt/oni/data /opt/oni/logs /opt/oni/config /opt/oni/reports

# Set permissions
chmod -R 755 /opt/oni

# Check if config exists
if [ ! -f /opt/oni/config/config.json ]; then
    echo "Creating default configuration..."
    cp /opt/oni/config/config.default.json /opt/oni/config/config.json 2>/dev/null || true
fi

# Initialize database
python3 -c "
import sqlite3
import os
db_path = '/opt/oni/data/oni.db'
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    conn.execute('CREATE TABLE IF NOT EXISTS init (id INTEGER PRIMARY KEY)')
    conn.commit()
    conn.close()
    print('✅ Database initialized')
"

# Start the application
echo "Starting ONI on port ${WEB_PORT:-5000}..."
exec python3 /opt/oni/oni.py
EOF
    
    chmod +x entrypoint.sh
}

# Create Makefile
create_makefile() {
    cat > Makefile << 'EOF'
.PHONY: help install clean build run docker-build docker-run test lint

# Colors
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

help: ## Show this help
	@echo ''
	@echo '${YELLOW}ONI Cybersecurity Command Center${RESET}'
	@echo ''
	@echo '${WHITE}Commands:${RESET}'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  ${GREEN}%-15s${RESET} %s\n", $$1, $$2}'

install: ## Install dependencies
	@echo "Installing dependencies..."
	bash setup.sh

clean: ## Clean temporary files
	@echo "Cleaning..."
	rm -rf __pycache__ *.pyc .pytest_cache .mypy_cache
	rm -rf reports/* logs/*
	@echo "✅ Clean complete"

build: ## Build the project
	@echo "Building..."
	python3 -m py_compile oni.py
	@echo "✅ Build complete"

run: ## Run ONI locally
	@echo "Starting ONI..."
	source venv/bin/activate && python3 oni.py

docker-build-alpine: ## Build Alpine Docker image
	docker build -f Dockerfile.alpine -t oni:alpine .

docker-build-ubuntu: ## Build Ubuntu Docker image
	docker build -f Dockerfile -t oni:ubuntu .

docker-run-alpine: ## Run Alpine container
	docker run -d --name oni-alpine -p 5000:5000 -p 8080:8080 --cap-add=NET_ADMIN --cap-add=NET_RAW oni:alpine

docker-run-ubuntu: ## Run Ubuntu container
	docker run -d --name oni-ubuntu -p 5000:5000 -p 8080:8080 --cap-add=NET_ADMIN --cap-add=NET_RAW oni:ubuntu

docker-compose-up: ## Start with docker-compose
	docker-compose up -d

docker-compose-down: ## Stop docker-compose
	docker-compose down

docker-compose-logs: ## View docker-compose logs
	docker-compose logs -f

test: ## Run tests
	python3 -m pytest tests/ -v --cov=. --cov-report=html

lint: ## Run linter
	flake8 oni.py --max-line-length=120 --ignore=E501
	black --check oni.py

format: ## Format code
	black oni.py

security: ## Run security checks
	bandit -r . -ll
	safety check

dev: ## Run in development mode
	FLASK_ENV=development python3 oni.py

all: install build test ## Run all steps
EOF
}

# Create nginx configuration
create_nginx_config() {
    mkdir -p config
    cat > config/nginx.conf << 'EOF'
events {
    worker_connections 1024;
}

http {
    upstream oni_backend {
        server oni-alpine:5000;
        server oni-ubuntu:5001 backup;
    }

    server {
        listen 80;
        server_name oni.local;
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl http2;
        server_name oni.local;

        ssl_certificate /etc/nginx/ssl/cert.pem;
        ssl_certificate_key /etc/nginx/ssl/key.pem;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;

        location / {
            proxy_pass http://oni_backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }

        location /api/ {
            proxy_pass http://oni_backend/api/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }

        location /ws/ {
            proxy_pass http://oni_backend/ws/;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }
    }
}
EOF
}

# Create .env example
create_env_example() {
    cat > .env.example << 'EOF'
# ONI Environment Configuration

# Application
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO

# Web Server
WEB_HOST=0.0.0.0
WEB_PORT=5000
PHISHING_PORT=8080
API_PORT=8081

# Security
SECRET_KEY=your-secret-key-here-change-this
JWT_SECRET=your-jwt-secret-here
ENCRYPTION_KEY=your-encryption-key

# Database
DB_PATH=/opt/oni/data/oni.db
DB_BACKUP_INTERVAL=86400

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# Notifications
SMTP_ENABLED=false
SMTP_SERVER=
SMTP_PORT=587
SMTP_USER=
SMTP_PASS=
ALERT_EMAILS=

# Webhook
WEBHOOK_ENABLED=false
WEBHOOK_URL=

# Bots
DISCORD_ENABLED=false
DISCORD_TOKEN=
DISCORD_PREFIX=!

TELEGRAM_ENABLED=false
TELEGRAM_API_ID=
TELEGRAM_API_HASH=
TELEGRAM_BOT_TOKEN=

SLACK_ENABLED=false
SLACK_TOKEN=
SLACK_CHANNEL=general

# SSH
SSH_MAX_CONNECTIONS=5
SSH_DEFAULT_TIMEOUT=30

# Traffic Generation
TRAFFIC_MAX_DURATION=300
TRAFFIC_DEFAULT_RATE=100
TRAFFIC_MAX_CONCURRENT=10

# Spoofing
SPOOF_DEFAULT_INTERFACE=eth0
ARPSPOOF_ENABLED=true

# Phishing
PHISHING_SSL_ENABLED=false
PHISHING_SSL_CERT=
PHISHING_SSL_KEY=

# Keylogger
KEYLOGGER_ENABLED=false
KEYLOGGER_WEBHOOK=

# Threat Detection
AUTO_BLOCK_THREATS=false
THREAT_SEVERITY_THRESHOLD=medium

# API Keys
IPSTACK_API_KEY=
VIRUSTOTAL_API_KEY=
SHODAN_API_KEY=
EOF
}

# Create README
create_readme() {
    cat > README.md << 'EOF'
# 👹 ONI - Cybersecurity Command Center

[![GitLab CI](https://gitlab.com/Iankulani/oni/badges/main/pipeline.svg)](https://gitlab.com/iank/oni/-/pipelines)
[![Docker Pulls](https://img.shields.io/docker/pulls/Iankulani/oni)](https://hub.docker.com/r/Iankulani/oni)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🎯 Overview

ONI is an advanced cybersecurity command center with 5000+ security commands, multi-platform bot integration, and powerful offensive/defensive security tools.

## ✨ Features

- **5000+ Security Commands** - SSH, Nmap, Curl, Ping, Traceroute, Nikto
- **Multi-Platform Bots** - Telegram, Discord, Slack, WhatsApp, iMessage, Signal, Google Chat
- **Web Interface** - Modern dashboard with vertical command menu
- **Phishing Suite** - 100+ templates with credential capture
- **Spoofing Tools** - IP/MAC/ARP/DNS spoofing
- **Traffic Generation** - Real network traffic simulation
- **Vulnerability Scanning** - Nikto web scanner integration
- **IP Management** - Threat detection and blocking
- **Geolocation** - IP location mapping and analytics
- **Keylogger** - Remote delivery and capture
- **Password Checker** - Strength analysis and entropy calculation

## 🚀 Quick Start

### Docker (Recommended)

```bash
# Pull and run
docker pull Iankulani/oni:latest
docker run -d --name oni -p 5000:5000 -p 8080:8080 --cap-add=NET_ADMIN --cap-add=NET_RAW iank/oni:latest

# Using docker-compose
git clone https://github.com/Iankulani/oni.git
cd oni
docker-compose up -d