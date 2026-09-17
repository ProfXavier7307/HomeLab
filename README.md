# Alexander Rodriquez — HomeLab Portfolio

Welcome to my personal homelab portfolio. This repository documents hands-on projects I have built to strengthen my skills in IT, cybersecurity, Linux administration, networking, containerization, self-hosting, automation, and systems troubleshooting.

I use my homelab as a practical environment for learning beyond the classroom; building systems, breaking them, troubleshooting problems, and documenting the solutions.

## About Me

My name is **Alexander Rodriquez**. I am a cybersecurity student with hands-on experience in IT support, computer repair, networking, Linux, and self-hosted infrastructure.

### Certifications

- CompTIA A+
- CompTIA Network+
- CompTIA Security+
- TestOut PC Pro
- TestOut Network Pro
- TestOut Security Pro

## Technologies & Skills

This portfolio includes work involving:

- Linux administration
- Debian / Raspberry Pi OS
- Docker and containerized services
- Kubernetes / K3s
- Networking and DHCP configuration
- SSH and remote administration
- Tailscale
- Cloudflare
- Cockpit
- Self-hosted services
- Raspberry Pi projects
- Local AI / LLM deployment
- llama.cpp and GGUF models
- Windows and Linux scripting
- Bluetooth and HDMI troubleshooting
- Hardware troubleshooting and repurposing
- Cybersecurity fundamentals

## Projects

### Voltron K3s Cluster

A multi-node Kubernetes homelab built using repurposed Dell Wyse thin clients. The project focuses on Linux administration, cluster networking, K3s, SSH, DHCP reservations, distributed workloads, and low-cost infrastructure.

**Topics:** K3s, Linux, networking, clustering, container orchestration, thin clients

[View the Voltron K3s project documentation](voltron-k3s/README.md)

### Debian Laptop Server

An older HP laptop repurposed as a Debian 13 home server for Linux administration, SSH, Tailscale remote access, Cockpit, local web/file hosting, Docker experimentation, and network troubleshooting. The server also hosted shared D&D files for my gaming group to access while connected to my home network.

**Topics:** Debian 13, SSH, Tailscale, Cockpit, Docker, systemd, DNS, file hosting, networking

[View the Debian Laptop Server project documentation](debian-server/README.md)

### Portable Local AI Environment (PLAE)

A portable local-LLM environment stored on a 256 GB external NVMe drive and designed to work across Windows and Tails/Linux. PLAE uses `llama.cpp`, quantized GGUF models, and platform-specific startup scripts to provide a portable offline AI toolkit without requiring the environment to be permanently installed on each host computer.

**Topics:** Local AI, llama.cpp, GGUF, Qwen3, Windows, Tails, Bash, batch scripting, exFAT, portable computing

[View the PLAE project documentation](portable-local-ai/README.md)

### PiTV

A Raspberry Pi 4B-based custom TV interface built to turn a non-smart television into a lightweight smart-TV-style dashboard. PiTV uses Raspberry Pi OS and fullscreen Chromium for streaming shortcuts, local weather and NOAA information, radar, utility controls, HDMI audio, and Bluetooth input.

**Topics:** Raspberry Pi, Linux, Chromium, systemd, Bluetooth, HDMI, PipeWire, weather integration, UI design

[View the PiTV project documentation](pitv/README.md)

## Repository Structure

As this portfolio grows, each major project will receive its own directory containing documentation, configuration examples, diagrams, screenshots, scripts, and troubleshooting notes.

```text
HomeLab/
├── README.md
├── voltron-k3s/
├── debian-server/
├── portable-local-ai/
├── pitv/
├── networking/
└── scripts/
```

## What I Document

For each project, I aim to include:

- Project goals
- Hardware and software used
- Architecture and design decisions
- Installation and configuration steps
- Problems encountered
- Troubleshooting process
- Solutions and lessons learned
- Screenshots or diagrams where useful

## Purpose

The purpose of this repository is to demonstrate practical, hands-on experience and continuous learning in IT and cybersecurity. It is intended to serve as both a technical reference for myself and a portfolio for employers, instructors, and other IT professionals.

---

**Alexander Rodriquez**  
Cybersecurity Student | IT & Homelab Enthusiast
