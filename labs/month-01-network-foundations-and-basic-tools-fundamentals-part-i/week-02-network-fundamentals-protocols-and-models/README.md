# Week 02 - Network Fundamentals - Protocols and Models

> Adapted from the "6-Month CCNA 200-301 Study Plan" reference.

## Objectives
- Deepen your understanding of network models and protocols: specifically, know the difference between TCP and UDP (when to use each, characteristics like reliability vs speed) .
- Learn about common protocols at each layer (e.g. Ethernet at Layer2, IP at Layer3, TCP/UDP at
- Layer4, HTTP/FTP at Layer7) and how they relate to the CCNA blueprint.
- Master the concept of encapsulation : how data is packaged at each layer (e.g. what a "packet" vs
- "frame" vs "segment" is).
- Get introduced to basic device configuration: practice using Cisco IOS CLI commands for initial switch setup (hostname, interface descriptions, etc.) to prepare for upcoming network access topics.
- Start learning about Cabling and Interfaces : types of network media (fiber vs copper , Ethernet cable categories) and where they are used. Identify different interface types on routers/switches in Packet
- Tracer .

## Hands-On Labs & Mini Projects
- Lab 2.1: Inspecting Packets in Wireshark - Install Wireshark (free packet analyzer). Use Packet Tracer's built-in Sniffer or your own PC's ping. In PT: connect a PC to a PT Cloud (internet) and generate traffic, capture it. Alternatively, on your actual computer , ping a site and capture in Wireshark. Inspect an ICMP packet: identify the Ethernet frame header , IP header , and ICMP data. Expected Outcome: You can see the different protocol headers layered (Ethernet contains IP which contains ICMP). Take a screenshot labeling the layers.
- Lab 2.2: Basic Switch Configuration - In Packet Tracer , place a 2960 switch and a PC. On the switch CLI, practice commands: set hostname ( hostname Week2Switch ), set a banner message ( banner motd "Authorized Access Only" ), configure an IP on the switch's VLAN1 interface (e.g. 192.168.1.10/24) so you could manage it, and set up a login password on 78 6 the console. Also practice the show interface status and show running-config . Expected Outcome: You become familiar with user EXEC vs config mode, and you have a switch with basic settings. Save the PT file for reuse.
- Lab 2.3: Media Demonstration - If you have different cable types in Packet Tracer (copper straight-through vs crossover vs fiber), set up a simple test: e.g. connect two switches with the wrong cable type and observe link down, then correct it. This will reinforce cable differences (Copper crossover for switch-switch if no auto-MDIX, fiber needs fiber ports, etc.).

## Milestones & Checkpoints
- Milestone 1: Write a short explanation (half-page) comparing TCP vs UDP in your own words. Include an example application for each (e.g. "TCP for HTTP web pages because..., UDP for live video streaming because..."). This checks your understanding of reliability vs speed trade-offs.
- Milestone 2: Complete the Wireshark lab and save a screenshot of a dissected packet. Label the Ethernet, IP, and TCP/UDP headers in your screenshot as a mini-report.
- Milestone 3: Configure a Packet Tracer switch with a hostname and IP, and successfully ping it from a connected PC (means your config was correct). Save this PT file as "Week2_SwitchConfig.pt". Achieve at least 25/30 on the Week 2 Quiz. For any missed questions, write down an explanation after researching the answer - this will turn mistakes into learning.
- Checkpoint: You should now be comfortable with fundamental terminology and able to navigate the CLI basics. If terms like "encapsulation", "segment vs packet", or any layer functions are still confusing, revisit the OSI chart or ask for clarification on forums (Cisco Learning Network community is helpful).

## Lab Log
| Date | Lab / Config | Key Takeaways | Evidence (files/screens) |
| --- | --- | --- | --- |
|  |  |  |  |
