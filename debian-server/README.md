# Debian Laptop Server

> **Status:** Active homelab / learning project. Core Debian, SSH, local web administration, and file-hosting functions were configured. Some Docker-based services remained experimental or planned.

## Project Overview

This project repurposed an older HP laptop into a Debian-based home server for learning Linux administration, remote management, networking, self-hosting, file delivery, and service troubleshooting.

Instead of leaving the laptop unused, I converted it into a practical homelab system that could stay online, be administered remotely, and host local services and files. The project also gave me experience working within the limitations of older consumer hardware.

## Hardware

- **Platform:** HP Notebook
- **Processor:** AMD E2-7110
  - 4 cores
  - 1.8 GHz
- **Memory:** 16 GB DDR3-1600
- **Storage:** 500 GB Western Digital 5400 RPM SATA HDD
- **Graphics:** AMD Radeon R2
- **Drive health:** SMART testing passed with no reported bad sectors during setup

The hardware is modest by modern server standards, but it is more than adequate for lightweight Linux services, administration practice, and small self-hosted workloads.

## Operating System

- **Debian 13 (Trixie)**
- LXDE desktop environment
- Hostname: `debianlaptop`
- Remote administration through SSH

The system was configured to remain available as a server rather than behaving like a normal laptop. Sleep behavior and lid-close sleep were disabled so closing the display would not unexpectedly take hosted services offline.

## Project Goals

- Repurpose existing hardware instead of purchasing a dedicated server
- Practice Debian/Linux system administration
- Configure reliable remote access with SSH
- Learn service management with `systemd`
- Host files and local web resources
- Use browser-based server administration tools
- Experiment with Docker and Docker Compose
- Improve local networking and DNS knowledge
- Learn how hardware and network limitations affect real workloads

## Core Services and Configuration

### SSH

SSH was configured so the system could be administered remotely from other computers on the local network.

This allowed most server management to be completed without needing to work directly from the laptop keyboard and display.

### Cockpit

Cockpit was installed for browser-based system administration and monitoring. It provided another way to inspect and manage the Debian system in addition to the command line.

A local hostname was used to make the service easier to access from the network.

### Local Web and File Hosting

The server was configured to serve local files and web content, including a directory used for D&D-related files.

Caddy was used during this setup to provide local web serving and HTTPS. My experience with Caddy on this system was limited and primarily focused on getting the service working rather than advanced reverse-proxy administration, so I do not treat Caddy as one of my core technologies.

This project was still useful for learning how web services, DNS names, file paths, ports, certificates, and service startup behavior fit together.

### Docker

Docker and Docker Compose were installed as part of the server environment so I could experiment with containerized services.

An `/opt/homelab` workspace was used while exploring services such as:

- Homepage dashboards
- File Browser
- Kiwix / offline knowledge hosting
- Other small self-hosted utilities

These Docker-based services were experimental or planned during the documented period and are not presented here as permanent production deployments.

## Networking

The server used a predictable local network address so SSH and hosted services could be reached consistently.

For public documentation, the exact subnet is sanitized:

```text
debianlaptop -> 192.168.x.15
```

During the early setup, the laptop was connected over Wi-Fi through a bridge/extender. For larger transfers, I later used wired Ethernet because of the substantial performance improvement.

Local DNS/host mappings were also used so services could be accessed with readable names rather than requiring the IP address every time.

## Architecture

```text
                         Home Network
                              |
                    Router / Local DNS
                              |
                     +----------------+
                     |                |
               SSH / Web Access   File Transfers
                     |                |
                     +-------+--------+
                             |
                      +-------------+
                      | Debian      |
                      | Laptop      |
                      | Server      |
                      +------+------+ 
                             |
              +--------------+--------------+
              |              |              |
           Cockpit      Local Web       Docker /
                        & File Host      Experiments
```

The laptop is a standalone server on the home network. Other systems connect to it remotely for administration, file access, and hosted services.

## Real-World File Transfer Use

One of the more practical workloads for this server involved hosting and transferring an archived Minecraft server world of approximately **26 GB**.

When transferring the archive over the slower wireless connection, the estimated transfer time was roughly **14 hours**. Switching the laptop to wired Ethernet reduced the estimated transfer time to around **1 hour**.

This was a useful real-world demonstration of how the network connection can become the bottleneck even when the server itself is functioning correctly.

## Reliability and Server Behavior

Because the device began life as a consumer laptop rather than a dedicated server, several configuration choices were necessary to make it behave reliably in a server role:

- Disabled automatic sleep
- Disabled suspend on lid close
- Used a predictable LAN address
- Enabled remote SSH administration
- Configured services to start automatically where appropriate
- Checked disk health before relying on the existing hard drive

These changes helped turn ordinary laptop hardware into a system that could remain available for homelab use.

## What I Learned

This project gave me practical experience with:

- Debian installation and administration
- Linux command-line troubleshooting
- SSH and remote administration
- `systemd` service management
- Local DNS and hostname mapping
- Static/predictable LAN addressing
- Browser-based administration with Cockpit
- Web and file hosting
- Basic HTTPS/service configuration
- Docker and Docker Compose fundamentals
- Storage and disk-health checks
- Diagnosing network throughput bottlenecks
- Repurposing older hardware for server workloads

## Planned / Experimental Ideas

Ideas explored for the server included:

- A self-hosted dashboard
- Browser-based file management
- Offline Wikipedia/knowledge hosting with Kiwix
- Additional Docker services
- Better monitoring and backup workflows
- Additional local storage and file-sharing roles

These are documented as ideas or experiments rather than completed production services unless they are added to the project log later.

## Documentation and Security

Because this repository is public, sensitive configuration information is intentionally excluded or sanitized.

This includes:

- Passwords
- SSH private keys
- API tokens
- MAC addresses
- Exact private-network details where unnecessary
- Private certificates or credentials

## Project Log

### July 2026 — Initial Server Build

- Repurposed the HP laptop as a Debian server
- Installed Debian 13 (Trixie)
- Set hostname to `debianlaptop`
- Configured a predictable LAN address
- Configured SSH remote administration
- Disabled sleep and lid-close suspend behavior
- Installed Cockpit
- Configured local web/file serving
- Installed Docker / Docker Compose for self-hosting experiments
- Verified the existing 500 GB hard drive passed SMART checks

### August 2026 — Large File Hosting / Transfer

- Used the laptop to host and transfer an approximately 26 GB archived Minecraft server world
- Identified wireless networking as a major transfer bottleneck
- Switched to Ethernet and reduced the estimated transfer time from roughly 14 hours to around 1 hour

---

**Project by Alexander Rodriquez**

This document will be updated as the Debian server changes or additional services are deployed.