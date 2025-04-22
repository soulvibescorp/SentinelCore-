SentinelCore/
├── core/
│   ├── encryption.py         # AES-256-GCM w/ secure key storage
│   ├── firewall.py           # Dynamic rule engine + port monitor
│   ├── scanner.py            # Advanced mock AV + hash DB
│   ├── auth.py               # Password vault, 2FA (TOTP/Duo ready)
│   └── utils.py              # Logger, Hasher, Config Loader
├── ui/
│   ├── qt_main.py            # Futuristic PyQt6 interface
│   ├── styles.qss            # Government-grade neon dark mode
│   └── icons/                # SVG icons for UI
├── cli/
│   └── sentinel_cli.py       # Full-featured terminal utility
├── config/
│   └── config.json           # Port rules, security levels, logs
├── storage/
│   └── vault.db              # Encrypted local key vault (sqlite + AES)
├── logs/
│   └── sentinel.log          # Activity + threat logs
├── tests/
│   ├── test_encryption.py
│   ├── test_firewall.py
│   └── test_scanner.py
├── scripts/
│   └── start_gui.sh          # One-click launcher (cross-platform)
├── requirements.txt
├── README.md
└── LICENSE
