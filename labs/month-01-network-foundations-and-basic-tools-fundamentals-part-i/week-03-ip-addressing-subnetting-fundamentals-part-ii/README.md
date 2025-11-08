# Week 03 - IP Addressing & Subnetting (Fundamentals Part II)

> Adapted from the "6-Month CCNA 200-301 Study Plan" reference.

## Objectives
- Understand IPv4 addressing thoroughly: the format of an IPv4 address, binary representation, network vs host portions, and the role of the subnet mask.
- Learn how to subnet IPv4 networks: given requirements (like X subnets or Y hosts), be able to calculate appropriate subnet masks, network IDs, broadcast addresses, etc. This is a crucial skill for the exam and real life.
- Practice configuring IP addresses on devices (routers, PCs) and verify connectivity within and across subnets.
- Get introduced to private IP vs public IP and the need for NAT (we will configure NAT later , but concept starts here) .
- Briefly overview IPv6 basics : understand the IPv6 address format, why IPv6 was introduced, and the different address types (global, link-local, unique local, multicast) . We will do more IPv6 in Week 4, but start familiarizing now.

## Hands-On Labs & Mini Projects
- Lab 3.1: Subnetting Practice (Paper or Tool) - Not a typical lab, but spend time manually calculating subnets. For example, take a Class C network 192.168.10.0/24 and practice making: (a) 2 subnets (each /25), (b) 4 subnets (/26), (c) 8 subnets (/27). Write down the subnet ID, broadcast, and valid host range for each. Do similar for a /16. Use a whiteboard or spreadsheet if needed. Check answers with a subnet calculator to verify.
- Lab 3.2: Configure Subnets in Packet Tracer - Build a small network with 3 subnets : e.g., one for Branch1 PCs, one for Branch2 PCs, and one for the WAN link between two routers. For instance: Router A (Branch1) with PC network 192.168.1.0/24, Router B (Branch2) with PC network 192.168.2.0/24, and a /30 for the link between routers. Configure IPs on two routers' interfaces and on a PC in each subnet. Use static routes (we haven't formally covered yet, but you can guess or look up how to add a static route) to ensure the two PCs can ping each other through the routers. Expected Outcome: Both PCs, in different IP networks, communicate via the routers (verifying your addressing and basic routing config). This is a preview of Week 4's routing topics but reinforces addressing.
- Lab 3.3: IPv6 Addressing Basics - In Packet Tracer , enable IPv6 on a router and a PC: assign a global IPv6 address (e.g., 2001:DB8:1::1/64 on router , 2001:DB8:1::2/64 on PC) and a link-local (should auto-generate). Ping the link-local and global addresses to test connectivity. If unfamiliar with IPv6 config, use a guide. Expected Outcome: You can configure and verify IPv6 addressing on Cisco IOS and understand the abbreviations. Document one example of an IPv6 address you used and identify its parts (network prefix, interface ID).

## Milestones & Checkpoints
- Milestone 1: Be able to subnet a network in under 10 minutes for a given scenario. For example, "Design an IP scheme for a company with 3 departments (50 hosts, 30 hosts, 20 hosts). What subnets do you use out of 192.168.10.0/24?" - Write out your solution and rationale.
- Milestone 2: Complete Lab 3.2 (2-router , 2-PC network) and demonstrate a successful ping from a PC on Router A's network to a PC on Router B's network. This shows you can correctly assign IPs and even set a basic static route. Save this lab as "Week3_RoutingIntro.pt".
- Milestone 3: List the three private IPv4 ranges from memory and explain in a few sentences why private addresses need NAT to reach the Internet. Similarly, list at least two types of IPv6 addresses (e.g., "Link-local starts with FE80, used only on local link").
- Checkpoint: By end of Week 3, subnetting should feel more comfortable. If you still struggle, schedule extra practice - it's that important. Consider using a subnetting app or game daily for speed. Also check that you haven't neglected earlier topics: try explaining to yourself how OSI layers relate now that you've added IP (Layer3) knowledge.

## Lab Log
| Date | Lab / Config | Key Takeaways | Evidence (files/screens) |
| --- | --- | --- | --- |
|  |  |  |  |
