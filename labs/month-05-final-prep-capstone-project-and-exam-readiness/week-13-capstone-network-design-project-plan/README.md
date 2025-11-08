# Week 13 - Capstone Network Design Project - Plan

> Adapted from the "6-Month CCNA 200-301 Study Plan" reference.

## Objectives
- Begin a capstone project : designing a small enterprise network from scratch, incorporating most technologies learned. This week, focus on planning and design on "paper" (or software) before implementation next week.
- Scenario: You are tasked to design a network for a small company with, say, 3 departments (like 71 39
- Admin, Engineering, Sales), two sites (HQ and Branch), and internet connectivity. They require: VLANs per department, inter-site routing, internet access for all via HQ, secure remote access for a few employees (VPN), and basic network security measures.
- Create a network diagram of this topology: likely includes routers at each site, switches, maybe a firewall (optional, or use router ACL as firewall), an ISP cloud, and maybe a server network.
- Plan IP addressing: assign subnets to each VLAN and site, ensuring summarization if possible and avoiding overlaps. Perhaps use private IPs internally and one public range for NAT at HQ.
- Choose and justify routing: e.g., use OSPF between sites (maybe over a simulated WAN), static default to internet, etc. - Plan out where to apply security: e.g., port security on user ports, ACL on router to filter internet traffic, VPN using perhaps Packet Tracer's VPN feature (if any, else just conceptual).
- Essentially, write a network design document : including network requirements, IP scheme, device roles, protocols, and security measures.
- Get feedback if possible: if you have a mentor or friend in networking, show them the design for critique. If not, self-review by comparing to reference architectures from Cisco (e.g., Enterprise Network
- Model).

## Hands-On Labs & Mini Projects
- Add your own items from the study plan.

## Milestones & Checkpoints
- Milestone 1: Complete a network diagram of the proposed design, showing all subnets and VLAN IDs, device names, interfaces, and relevant IP addresses. This is the blueprint for your implementation.
- Milestone 2: Write out the IP addressing plan : e.g., "192.168.10.0/24 - Admin VLAN 10 at HQ (50 users), 192.168.20.0/24 - Eng VLAN 20 at HQ (30 users), 192.168.30.0/24 - Sales VLAN 30 at HQ (20 users), 192.168.40.0/24 - Branch office LAN (30 users). WAN: 10.0.0.0/30 between HQ and Branch." Ensure the sizing fits (no VLAN has more IPs than needed but leave some growth).
- Milestone 3: Enumerate the technologies to use: "OSPF area 0 between HQ and Branch routers; Inter- VLAN routing via multilayer switch at HQ or router-on-a-stick; PAT on HQ router for internet; Port security on access ports (max 2 MAC for phones+PC maybe); DHCP from HQ server/router; ACL on HQ 40 router to block certain ports (e.g., disallow telnet from outside); Site-to-site VPN planned (conceptual)." This list will guide config.
- Checkpoint: Validate the plan against CCNA topics: did you include at least something from each domain? Likely yes: VLANs (Network Access), OSPF (IP Connectivity), NAT/DHCP (IP Services), ACL/ security (Security Fundamentals), maybe mention of automation (like "we will use SSH and maybe network scripts for config backup" for Automation, albeit light). The aim is to demonstrate holistic understanding. Next step will be implementing and testing this design in Week 14.

## Lab Log
| Date | Lab / Config | Key Takeaways | Evidence (files/screens) |
| --- | --- | --- | --- |
|  |  |  |  |
