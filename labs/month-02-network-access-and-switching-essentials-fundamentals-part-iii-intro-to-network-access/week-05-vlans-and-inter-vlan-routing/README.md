# Week 05 - VLANs and Inter-VLAN Routing

> Adapted from the "6-Month CCNA 200-301 Study Plan" reference.

## Objectives
- Understand VLAN concepts : what VLANs are, how they provide network segmentation at Layer 2, and default VLAN behavior .
- Learn to configure VLANs on Cisco switches: create VLANs, assign switch ports to VLANs (access ports) , understand the concept of the management VLAN and native VLAN.
- Implement Inter-VLAN routing : since different VLANs are different subnets, you need a router or
- Layer 3 switch to route between them. We'll configure Router-on-a-Stick (a router with subinterfaces for each VLAN) to enable devices in different VLANs to communicate.
- Practice troubleshooting VLAN issues : e.g., mismatched VLANs, incorrect IP addressing for VLANs.
- Reinforce subnetting with a real config: design IP subnets for each VLAN in a network and apply them.

## Hands-On Labs & Mini Projects
- Lab manual: "31 Days Before CCNA" - see if there's a day on VLANs or trunking and do the exercises. Research Papers/Articles: Cisco Document: "Configuring VLANs" - official Cisco docs on VLAN config (on Catalyst switches). Skim for any best practices (like naming VLANs, using VLAN 1 or not, etc.). "The Death of VLAN 1" (blog) - an article explaining why you should not use VLAN 1 for management (common security advice). This adds real-world flavor to your VLAN knowledge. Cisco Support Forum thread on Router-on-a-Stick - read a Q&A or troubleshooting case to see common mistakes (e.g., forgetting to set the router port as trunk or mismatched native VLAN). (Design) "LAN Segmentation and VLANs" - chapter from an older Cisco design guide or whitepaper explaining how VLANs are used in network design. Focus on the rationale (security, reduce broadcasts, etc.).
- Lab 5.1: VLAN Configuration and Ping Test - In Packet Tracer , set up one switch with 3 PCs on it. Create 2 VLANs (say VLAN10 and VLAN20). Put 2 PCs on VLAN10, and 1 PC on VLAN20. Assign IP addresses such that PCs in different VLANs are on different subnets (e.g., VLAN10 uses 192.168.10.0/24, VLAN20 uses 192.168.20.0/24). Initially, do not configure any router . Verify that 16 14 two PCs in the same VLAN can ping each other (should work), but PCs in different VLANs cannot (expected, since no inter-VLAN routing yet). This shows VLAN segmentation.
- Lab 5.2: Router-on-a-Stick - Extend Lab 5.1 by adding a Router (2911 or similar in PT) and connecting the switch to the router with one link. Configure that switch port as a trunk (switchport mode trunk ) and on the router configure subinterfaces: e.g. Gig0/0.10 for VLAN10, Gig0/0.20 for VLAN20, assign 192.168.10.1 and 192.168.20.1 respectively. Don't forget encapsulation dot1Q 10 etc. Now set each PC's default gateway to the router's subinterface IP (PCs in VLAN10 use 192.168.10.1). Expected Outcome: PCs in different VLANs can now ping each other through the router . Also test pinging the router gateways. Save this lab as "Week5_VLAN_RouterOnStick.pt".
- Lab 5.3: Trunking and Native VLAN - Add a second switch to Lab 5.2, connected via a trunk link to the first switch. Put one PC on the second switch on VLAN10. Ensure trunk is up (use show interfaces trunk ). The PC on switch2 VLAN10 should communicate with PCs on switch1 VLAN10. Experiment by changing native VLAN on one side and see the effect (noticing errors or ping issues if mismatched). Then set them correctly. Expected Outcome: Understanding of how trunks carry multiple VLANs and the importance of matching native VLANs.
- (Mini-Project) VLAN Design Document: Imagine a small office network for a company with 3 departments (e.g., Sales, Engineering, Guest WiFi). Sketch a simple network diagram showing 3 VLANs, how they connect to a router or L3 switch for inter-VLAN routing, and propose an IP range for each. Write a paragraph justifying the VLAN segmentation (e.g., "to isolate guest traffic from internal", etc.). This is a design exercise to apply VLAN knowledge conceptually.

## Milestones & Checkpoints
- Milestone 1: Successfully implement a router-on-a-stick with at least 2 VLANs and verify connectivity between VLANs via the router . Confirm by screenshotting ping tests from a PC in VLAN10 to a PC in VLAN20, along with a show ip interface brief on the router showing subinterfaces up.
- Milestone 2: Describe in your notes the difference between an Access Port and a Trunk Port . List the commands to configure each. Also note the typical native VLAN (default 1) and how to change it. 15
- Milestone 3: Score 80%+ on the VLAN/Inter-VLAN quizzes. If any VLAN concept is wrong (for example, confusion about extended VLAN range or how trunk tagging works), revisit that portion in Odom or
- Checkpoint: You've now done substantial switch configuration. Ensure you can confidently navigate show vlan , show interfaces trunk , and understand what it means. If possible, discuss with a peer or in a forum one of your labs (explaining what you did helps cement knowledge). Heading into Week 6, we'll tackle Spanning Tree and EtherChannel, which build on the VLAN/trunk knowledge. Make sure trunking is solid in your mind (we'll see why STP is needed when redundancy is introduced).

## Lab Log
| Date | Lab / Config | Key Takeaways | Evidence (files/screens) |
| --- | --- | --- | --- |
|  |  |  |  |
