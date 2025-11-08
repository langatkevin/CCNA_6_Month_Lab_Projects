# Week 14 - Capstone Network Implementation and Test

> Adapted from the "6-Month CCNA 200-301 Study Plan" reference.

## Objectives
- Implement the designed network in Packet Tracer (or real gear if accessible) step-by-step.
- Configure VLANs and trunking at HQ, set up inter-VLAN routing (either a layer 3 switch SVIs or a router-on-a-stick). Configure OSPF between HQ and Branch routers, ensure routes exchanged.
- Set up DHCP server (maybe at HQ for all subnets, using DHCP relay to branch). Set up NAT on HQ for internet access simulation (use a loopback or cloud as Internet).
- Apply security: port security on switches, ACL on HQ router for traffic filtering, secure device configs (SSH login). If possible, configure an IPsec VPN between HQ and Branch (PT might have a "VPN easy" option on routers - if not, simulate by just allowing direct since it's lab).
- Test end-to-end: from a PC in each VLAN, ping others, ping branch, ping internet (maybe simulate internet as a server in a different network beyond HQ router). Test fail-safes if any (e.g., if you did HSRP with two routers at HQ, shut one to see continuity).
- Troubleshoot any issues encountered - this is likely. It's part of learning: maybe OSPF adjacency fails due to passive interface or NAT issues. Work through them systematically (like you would on exam sims or real world).
- Once stable, document the configuration : save config files, and perhaps write an executive summary of the network to accompany the diagram.
- This project is also material you can mention in interviews or on a resume (it's home lab, but it shows initiative and skills).

## Hands-On Labs & Mini Projects
- Add your own items from the study plan.

## Milestones & Checkpoints
- Milestone 1: All critical configs done: VLANs, OSPF, NAT, DHCP, ACLs, port security. The network should be functioning as intended. For example: Users get IP via DHCP, can reach resources in other VLANs and branch, internet pings go out (maybe not real internet but a fake server), and disallowed traffic is indeed blocked by ACL.
- Milestone 2: Testing results documented. Make a table: each VLAN PC -> where should it reach and 41 not reach? Test ping/HTTP etc. E.g., "PC in Sales VLAN -> should reach Branch server (ping ok), should browse internet (http ok, tested by HTTP to fake server), should NOT telnet outside (tried telnet, blocked as expected by ACL)." Do this for key scenarios. All tests should align with design goals.
- Milestone 3: Configuration review: run show run on each device and ensure no glaring issues (e.g., default passwords, missing service encryption, etc.). Also note resource usage: Did you use small subnets efficiently? Are there any routing table oddities? Clean up if necessary (like remove any test ACL lines, etc.).
- Milestone 4: Save your final Packet Tracer file and also export configs (for your portfolio). Create a brief Network Implementation Report with the diagram, summary of addressing, summary of protocols, and verification outputs (like OSPF neighbor table, NAT translation sample, etc.). Even if just for yourself, this consolidates what you've built.
- Checkpoint: Congratulate yourself - you've essentially simulated the job of setting up an enterprise network! This capstone ties together months of learning. It should boost your confidence that not only can you answer exam questions, you can actually apply the knowledge. This is the bridge from certification to real-world skill. Use this accomplishment as a talking point in interviews and as personal validation of your abilities.

## Lab Log
| Date | Lab / Config | Key Takeaways | Evidence (files/screens) |
| --- | --- | --- | --- |
|  |  |  |  |
