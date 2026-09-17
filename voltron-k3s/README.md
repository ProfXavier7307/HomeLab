# Voltron K3s Cluster

> **Status:** In progress — 1 of 5 nodes currently configured and online. K3s has **not** been installed yet.

## Project Overview

Voltron is a five-node homelab cluster built from repurposed **Dell Wyse 3040 thin clients**. The long-term goal is to use the cluster as a hands-on environment for learning Linux administration, networking, SSH, Kubernetes/K3s, container orchestration, distributed workloads, and low-cost infrastructure design.

The systems are named after characters from *Voltron*. Rather than building the entire environment at once, I am bringing each node online individually, validating its hardware and network configuration, and documenting the process as the cluster develops.

## Project Goals

- Repurpose low-cost thin clients as a multi-node Linux cluster
- Install and administer Debian on each system
- Configure reliable wired networking and DHCP reservations
- Use SSH for remote administration
- Deploy K3s with a dedicated control-plane node
- Join the remaining systems as worker nodes
- Experiment with containerized and distributed workloads
- Explore inexpensive shared-storage options
- Practice troubleshooting hardware, Linux, networking, and cluster issues

## Hardware

- **5× Dell Wyse 3040 thin clients**
- Internal eMMC storage on each node
- Gigabit Ethernet networking
- Custom-made Cat6 Ethernet cables as additional nodes are brought online
- **Potential future storage:** 128 GB USB storage attached to Hunk for shared-storage experimentation

The USB storage idea is currently only a plan and has not been deployed.

## Node Plan

| Node | Voltron Role | Physical Unit | Planned Cluster Role | Current Status |
|---|---|---:|---|---|
| **Keith** | Black Lion | #4 | K3s control plane | **Online / Debian configured / SSH working** |
| **Pidge** | Green Lion | TBD | Worker | Not configured yet |
| **Lance** | Red Lion | TBD | Worker | Not configured yet |
| **Allura** | Blue Lion | TBD | Worker | Not configured yet |
| **Hunk** | Yellow Lion | TBD | Worker / possible storage experiments | Not configured yet |

## Current Progress

### Keith — First Node Online

Keith is currently the only fully configured node.

Completed so far:

- Installed a minimal Debian system to the internal eMMC
- Set the hostname to `keith`
- Configured wired networking through DHCP
- Enabled SSH remote administration
- Configured SSH key-based access
- Verified that the system is reachable remotely over the local network
- Selected Keith as the future K3s control-plane node

Basic validation:

```bash
hostname
```

Expected output:

```text
keith
```

Remote administration is performed over SSH using the node's local network address. MAC addresses, SSH keys, and other sensitive network information are intentionally not published in this repository.

## Networking Plan

Each physical Wyse unit will receive a predictable DHCP reservation so the nodes can be reached consistently without manually configuring static addressing inside Debian.

The reservation scheme is based on the physical unit number, making it easier to identify hardware while troubleshooting. Exact MAC addresses and other identifying network information are kept private.

All cluster traffic will use wired Ethernet rather than Wi-Fi.

## K3s Architecture — Planned

K3s is not installed yet. Once the remaining base-node work is complete, the planned architecture is:

```text
                         Home Network
                              |
                         Ethernet LAN
                              |
              +---------------+---------------+
              |               |               |
          +-------+        +-------+       +-------+
          | Keith |        | Pidge |       | Lance |
          | K3s   |        | Agent |       | Agent |
          |Server |        +-------+       +-------+
          +---+---+
              |
       +------+------+
       |             |
   +-------+     +-------+
   |Allura |     | Hunk  |
   | Agent |     | Agent |
   +-------+     +-------+
```

Keith will run the K3s server/control-plane role. The other four systems are planned as agents/workers.

## Why Wyse 3040 Thin Clients?

The Wyse 3040 is limited compared with a traditional server, which is part of the point of this project. The cluster is intended to explore what can be accomplished with inexpensive, low-power, repurposed hardware while working within real resource constraints.

This creates opportunities to practice:

- Resource-efficient Linux administration
- Lightweight Kubernetes deployment
- Distributed computing concepts
- Network troubleshooting
- Hardware reuse and lifecycle extension
- Designing around storage, memory, and CPU limitations

## Hardware Evaluation

During initial testing, all five systems were able to boot, although some units showed minor hardware indicators or RTC/CMOS warnings that will need additional attention as they are configured.

Rather than assuming every used system is identical or problem-free, each node is being tested individually before it becomes part of the cluster.

## Next Steps

1. Build/terminate the additional Cat6 Ethernet cables needed for the remaining nodes.
2. Bring the remaining four Wyse systems onto the network one at a time.
3. Install and configure Debian on each node.
4. Assign hostnames and DHCP reservations.
5. Configure and verify SSH access to every node.
6. Install the K3s server on Keith.
7. Join Pidge, Lance, Allura, and Hunk as K3s agents.
8. Verify the cluster with `kubectl get nodes`.
9. Deploy a small test workload across the cluster.
10. Evaluate the 128 GB USB storage idea for Hunk and determine whether it is useful for shared or persistent storage.

## Skills Demonstrated

This project is intended to demonstrate practical experience with:

- Debian Linux administration
- SSH and remote administration
- DHCP and local network configuration
- Ethernet cable termination and physical networking
- Hostname and node management
- Hardware troubleshooting
- Kubernetes/K3s concepts
- Container orchestration
- Low-cost infrastructure design
- Technical documentation

## Project Log

### September 2026 — Initial Build

- Acquired and tested five Dell Wyse 3040 systems
- Selected physical unit #4 as **Keith**
- Installed Debian on Keith
- Configured hostname and SSH access
- Verified remote connectivity
- Designated Keith as the planned K3s control-plane node
- Paused additional node deployment until more Ethernet cables are completed

---

**Project by Alexander Rodriquez**

This document will be updated as each node is brought online and the K3s cluster is built.