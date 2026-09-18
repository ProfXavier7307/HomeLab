# Voltron K3s Cluster

> **Status:** In progress — 2 of 5 nodes currently configured and online. K3s has **not** been installed yet.

## Project Overview

Voltron is a five-node homelab cluster built from repurposed **Dell Wyse 3040 thin clients**. The long-term goal is to use the cluster as a hands-on environment for learning Linux administration, networking, SSH, Kubernetes/K3s, container orchestration, distributed workloads, and low-cost infrastructure design.

The systems are named after characters from *Voltron*. Rather than building the entire environment at once, I am bringing each node online individually, validating its hardware and network configuration, and documenting the process as the cluster develops.

## Current Status

| Component | Progress |
|---|---:|
| Nodes online | **2 / 5** |
| Debian configured | **2 / 5** |
| SSH configured | **2 / 5** |
| K3s control plane | **0 / 1** |
| K3s workers joined | **0 / 4** |
| Shared storage | **Planned** |

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
- Maintain clear technical documentation as the environment evolves

## Naming and Role Design

The cluster is named **Voltron**, with each node named after a member of the team.

The final physical-unit naming map is:

| Physical Unit | Node | Lion | Planned Role |
|---:|---|---|---|
| #1 | **Lance** | Red Lion | K3s worker |
| #2 | **Hunk** | Yellow Lion | K3s worker |
| #3 | **Allura** | Blue Lion | K3s worker |
| #4 | **Keith** | Black Lion | K3s control plane |
| #5 | **Pidge** | Green Lion | K3s worker / planned storage host |

This naming scheme makes the individual systems easier to identify than generic hostnames such as `node1` or `worker2`.

## Hardware

- **5× Dell Wyse 3040 thin clients**
- Internal eMMC storage on each node
- **Cloud-managed Gigabit Ethernet switch** for cluster connectivity
- Gigabit Ethernet networking
- Custom-made Cat6 Ethernet cables as additional nodes are brought online
- **Potential future storage:** 128 GB USB storage attached to Pidge for shared-storage experimentation

The USB storage idea is currently only a plan and has not been deployed.

## Node Plan

| Node | Voltron Role | Physical Unit | Planned Cluster Role | Current Status |
|---|---|---:|---|---|
| **Lance** | Red Lion | #1 | Worker | Offline / not configured yet |
| **Hunk** | Yellow Lion | #2 | Worker | Offline / not configured yet |
| **Allura** | Blue Lion | #3 | Worker | Offline / not configured yet |
| **Keith** | Black Lion | #4 | K3s control plane | **Online / Debian configured / SSH working** |
| **Pidge** | Green Lion | #5 | Worker / planned storage host | **Online / Debian configured / SSH working / DHCP reservation configured** |

## Current Progress

### Keith — First Node Online

Keith was the first fully configured node.

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

### Pidge — Second Node Online

Physical unit **#5** has been assigned as **Pidge**.

Completed so far:

- Assigned hostname `pidge`
- Connected the node to the wired network
- Configured a DHCP reservation corresponding to physical unit #5
- Verified the node is reachable on the local network
- Designated Pidge as a future K3s worker node

At the current stage, **Keith and Pidge are the only two nodes powered/configured for normal network use**. Lance, Hunk, and Allura are assigned but have not yet been brought online as Debian/K3s nodes.

## Windows SSH Launcher

A small Python utility was added to simplify connecting to the cluster from Windows:

[`tools/voltron_ssh.py`](tools/voltron_ssh.py)

The launcher presents all five Voltron nodes in a menu and opens the selected SSH connection in a **new Command Prompt window**, allowing multiple node sessions to remain open simultaneously. It uses the Windows OpenSSH client with the `xander` account.

Example behavior:

```text
1. Lance  (Red Lion)
2. Hunk   (Yellow Lion)
3. Allura (Blue Lion)
4. Keith  (Black Lion)
5. Pidge  (Green Lion)
```

The launcher has been tested successfully with the currently online nodes, **Keith and Pidge**.

## Networking and Addressing Plan

All five cluster nodes connect by wired Ethernet to a **cloud-managed Gigabit switch**. The switch provides the physical Layer 2 connection between the nodes and the rest of the home network, while the router provides DHCP addressing and reservations.

Each physical Wyse unit receives a predictable DHCP reservation so the nodes can be reached consistently without manually assigning static addresses inside Debian. The systems themselves remain configured for DHCP, while the router assigns the same address to each node based on its network adapter.

The addressing pattern follows the physical unit number:

| Physical Unit | Public Documentation Address | Assignment |
|---:|---|---|
| #1 | `192.168.x.101` | **Lance** |
| #2 | `192.168.x.102` | **Hunk** |
| #3 | `192.168.x.103` | **Allura** |
| #4 | `192.168.x.104` | **Keith** |
| #5 | `192.168.x.105` | **Pidge** |

The subnet is intentionally sanitized as `192.168.x.x` in the public documentation. MAC addresses and other identifying network information are kept private.

This approach provides predictable addressing while keeping network configuration centralized at the router instead of manually maintaining static IP settings on every node. Using a managed switch also leaves room for future network experiments such as port monitoring, traffic inspection, VLANs, or segmentation if those features are useful later.

## K3s Architecture — Planned

K3s is not installed yet. Once the remaining base-node work is complete, the planned architecture is:

```text
                              Home Network
                                   |
                              Router / DHCP
                                   |
                    Cloud-Managed Gigabit Switch
                                   |
           +-----------+-----------+-----------+-----------+
           |           |           |           |           |
       +--------+  +--------+  +--------+  +--------+  +--------+
       | Lance  |  | Hunk   |  | Allura |  | Keith  |  | Pidge  |
       | Agent  |  | Agent  |  | Agent  |  |  K3s   |  | Agent  |
       |        |  |        |  |        |  | Server |  |Storage |
       +--------+  +--------+  +--------+  +--------+  +--------+
```

Keith will run the K3s server/control-plane role. Lance, Hunk, Allura, and Pidge are planned as agent/worker nodes, with Pidge also serving as the planned storage host.

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

## Documentation and Security Practices

Because this repository is public, configuration details are documented without publishing credentials or sensitive network information.

Items intentionally excluded include:

- SSH private keys
- Passwords
- API keys or tokens
- MAC addresses
- Unnecessary identifying network details

Configuration examples may use sanitized addresses or placeholders where appropriate.

## Next Steps

1. Build/terminate the additional Cat6 Ethernet cables needed for the remaining nodes.
2. Bring Lance (#1), Hunk (#2), and Allura (#3) onto the network.
3. Install and configure Debian on each remaining node.
4. Configure their DHCP reservations and verify SSH access.
5. Install the K3s server on Keith.
6. Join Pidge, Lance, Allura, and Hunk as K3s agents.
7. Verify the cluster with `kubectl get nodes`.
8. Deploy a small test workload across the cluster.
9. Evaluate the 128 GB USB storage idea for Pidge and determine whether it is useful for shared or persistent storage.
10. Document workloads, failures, troubleshooting, and design changes as the cluster evolves.

## Skills Demonstrated

This project is intended to demonstrate practical experience with:

- Debian Linux administration
- SSH and remote administration
- DHCP and local network configuration
- Managed Ethernet switching
- Ethernet cable termination and physical networking
- Hostname and node management
- Windows/Python administration tooling
- Hardware troubleshooting
- Kubernetes/K3s concepts
- Container orchestration
- Shared-storage planning
- Low-cost infrastructure design
- Technical documentation
- Security-conscious public documentation

## Project Log

### September 2026 — Initial Build

- Acquired and tested five Dell Wyse 3040 systems
- Finalized node mapping: **#1 Lance, #2 Hunk, #3 Allura, #4 Keith, #5 Pidge**
- Selected physical unit #4 as **Keith**
- Installed Debian on Keith
- Configured hostname and SSH access
- Verified remote connectivity
- Designated Keith as the planned K3s control-plane node
- Established a predictable DHCP reservation scheme based on physical unit number
- Assigned physical unit #5 as **Pidge**
- Configured Pidge to use the #5 DHCP reservation (`192.168.x.105` in public documentation)
- Brought Pidge online as the second configured node
- Designated **Pidge (#5)** as the planned shared-storage host
- Added and tested a Windows Python SSH launcher that can open simultaneous SSH sessions to the Voltron nodes
- Planned all five nodes to connect through a cloud-managed Gigabit switch

---

**Project by Alexander Rodriquez**

This document will be updated as each node is brought online and the K3s cluster is built.
