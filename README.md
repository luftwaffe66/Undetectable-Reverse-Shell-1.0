# Undetectable Reverse Shell – Single Mode Edition

![Undetectable Reverse Shell](https://github.com/1603160/Undetectable-Reverse-Shell-1.0/blob/main/reverse-shell-undetectable-1.0.png?raw=true)

## Overview

This tool generates a powerful, obfuscated reverse shell payload using **CMD + PowerShell**, encoding the final payload in **Base64** and using **dynamic variable renaming** for stealth and detection evasion. The goal is to produce a payload that can be executed directly via CMD with a high success rate in bypassing basic detection mechanisms.

Created and maintained by: [luftwaffe66](https://github.com/luftwaffe66)

---

## Table of Contents

1. [Features](#features)  
2. [Requirements](#requirements)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Payload Characteristics](#payload-characteristics)  
6. [License](#license)  
7. [Disclaimer](#disclaimer)

---

## Features

- Single-mode payload: **CMD + PowerShell + Base64**
- Full obfuscation via randomized variable names
- Clean, minimal interaction
- Compatible with all modern Windows environments
- Automatically generates ready-to-execute CMD payload

---

## Requirements

- Python 3.x
- A target Windows machine
- A listener configured (e.g., `nc -lvnp <port>` or Metasploit multi/handler)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/1603160/Undetectable-Reverse-Shell-1.0.git
cd Undetectable-Reverse-Shell-1.0
```

---

## Usage

Run the generator using Python 3:

```bash
python3 generador.py
```

You will be prompted for:

- **Target IP or Hostname**
- **Port**

The script will output a fully obfuscated, Base64-encoded reverse shell payload ready to execute directly via CMD.

---

## Payload Characteristics

- **Memory-resident**: No files dropped to disk
- **Hidden execution**: Launches silently without opening a visible PowerShell window
- **Obfuscated**: Random variable names and full Base64 encoding
- **Customizable**: Easy to embed in other payloads or attack chains

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Disclaimer

This tool is provided for educational and authorized testing purposes only. The authors assume no responsibility for any misuse or damage caused by this software. Use it responsibly and only in environments where you have explicit permission to do so.
