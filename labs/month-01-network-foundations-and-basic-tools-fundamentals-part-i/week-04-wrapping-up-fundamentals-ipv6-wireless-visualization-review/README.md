# Week 04 - Wrapping up Fundamentals (IPv6, Wireless, Visualization, Review)

> Adapted from the "6-Month CCNA 200-301 Study Plan" reference.

## Objectives
- Solidify understanding of IPv6 : cover address types in more detail (global unicast, unique local, link- local, multicast, anycast) and IPv6 configuration on Cisco devices (SLAAC, DHCPv6 concepts).
- Learn basic network troubleshooting tools : ping, traceroute , and OS commands to verify IP configuration ( ipconfig /ifconfig on host OSes) . By CCNA blueprint, you should know how to verify IP parameters on Windows, Mac, Linux.
- Explore wireless fundamentals : non-overlapping Wi-Fi channels (2.4GHz vs 5GHz), what an SSID is, basics of Wi-Fi security (WPA2). This ties into Network Fundamentals (1.11 wireless principles) and
- Security Fundamentals (5.9 wireless security protocols) .
- Introduction to network virtualization : concepts of VLAN (virtual LAN) vs VRF vs VPN (just definitions; we will configure VLANs in Month 2, but here understand that virtualization allows multiple networks on same physical infrastructure). Also understand what a server virtualization and container means in networking contexts (to meet 1.12 blueprint).
- Conduct a Month 1 review : revisit all main topics (devices, OSI, TCP/UDP, addressing). Identify any weak areas before moving to Month 2.

## Hands-On Labs & Mini Projects
- Lab 4.1: IPv6 Neighbor Discovery - Extend Lab 3.3 (the IPv6 lab). Configure two routers connected via IPv6. Enable OSPFv3 or simply static routes for IPv6 to see end-to-end connectivity. Also, test the SLAAC feature: on a router interface, enable it to advertise a prefix (turn on IPv6 unicast-routing and use ipv6 address prefix/64 eui-64 on interface, or SLAAC configs). Configure a PC to get an IPv6 address automatically. Expected Outcome: The PC autoconfigures a global IPv6 address (stateless) and can reach the router . Check the PC's IPv6 config to see link- local and autoconfigured addresses.
- Lab 4.2: Wireless Router in Packet Tracer - PT has generic wireless routers. Set up a PT home wireless router , give it an SSID "Week4WiFi" with WPA2 password, and add a PC with a PT wireless NIC to connect to it. See if you can ping between wireless PC and a wired PC on that router . Expected Outcome: Understand how a wireless client associates via SSID/security to an AP. (This lab is limited but gives a conceptual demo. Real gear would be needed for full effect, but PT can simulate a bit.)
- Lab 4.3: Basic Troubleshooting Scenarios - Deliberately break things in a small PT network and practice troubleshooting: e.g., take a simple two-router network and misconfigure IP on one side, or use wrong default gateway on a PC, then use ping and traceroute from the devices to identify the issue. Document one scenario: describe the symptoms (e.g., PC1 can't reach PC2), your troubleshooting steps (ping X, got no reply, etc.), the identified problem, and the fix. (Project) Fundamentals Summary Mind-Map: As a wrap-up for Month 1, create a visual mind- map or diagram that connects the concepts learned: Show how OSI layers relate to specific protocols (HTTP at Layer7, TCP at Layer4, IP at Layer3, Ethernet at Layer2), list device types and where they operate, illustrate an IPv4 vs IPv6 address example, and indicate how subnetting breaks a network. Making this map will reinforce the holistic view.

## Milestones & Checkpoints
- Milestone 1: Configure IPv6 on two routers and two PCs (as in Lab 4.1) so that all devices can ping each other's IPv6 global addresses. This confirms understanding of IPv6 addressing and basic routing. Save lab "Week4_IPv6.pt".
- Milestone 2: Write a short explanation of a real-world scenario using each wireless security protocol 12 (e.g., "WPA2 is currently common for home Wi-Fi, WPA3 is newer and more secure, WEP is obsolete"). Also list 3 non-overlapping channels in 2.4GHz (1, 6, 11) to demonstrate wireless basics knowledge.
- Milestone 3: Complete the Month 1 practice exam (50 Qs) with a score of ~80% or higher . Review each wrong answer and write down why the correct answer is correct. If score < 80%, identify weak areas and plan a revision in Week 5 (we can allocate some review time then).
- Checkpoint: Fundamentals phase complete! You should now be confident in network foundational concepts. Verify that you have: a solid grasp of IP addressing and can do subnetting relatively quickly; familiarity with the CLI; understanding of how different network components function and interact. Any lingering confusion here should be addressed before moving on, as Months 2-4 will build on this foundation. Don't hesitate to use community forums or study groups to clarify doubts.

## Lab Log
| Date | Lab / Config | Key Takeaways | Evidence (files/screens) |
| --- | --- | --- | --- |
|  |  |  |  |
