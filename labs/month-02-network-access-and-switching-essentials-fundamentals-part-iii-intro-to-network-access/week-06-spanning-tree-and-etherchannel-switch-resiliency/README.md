# Week 06 - Spanning Tree and EtherChannel (Switch Resiliency)

> Adapted from the "6-Month CCNA 200-301 Study Plan" reference.

## Objectives
- Understand the Spanning Tree Protocol (STP) : why it exists (prevent switching loops), how it elects a root bridge and manages port states (forwarding/blocking) . Learn the basics of Rapid PVST+ (the Cisco default spanning tree mode) and terms like Root Port, Designated Port, Blocking/Alternate Port
- .
- Configure STP settings on switches: not in-depth (CCNA is limited here), but know how to identify the root bridge ( show spanning-tree output) and adjust priorities to influence root election, if required.
- Learn about EtherChannel (Link Aggregation) : purpose (increase bandwidth and provide redundancy by bundling links) . Understand the protocols LACP (open standard) vs PAgP (Cisco proprietary) for negotiating EtherChannels.
- Configure a simple EtherChannel between two switches in Packet Tracer using LACP (since PT supports it). Verify with show etherchannel summary .
- Continue wireless and security fundamentals : If not covered yet, ensure understanding of how enterprise wireless differs (AP & WLC architectures, which we'll touch in Week 7) and how spanning tree and EtherChannel might interplay with Wi-Fi (mostly separate topics but complete the network access domain fully).
- Integrate knowledge with a larger lab: by now, you know VLANs, routing, STP, EtherChannel - attempt a lab combining these (see Hands-On).

## Hands-On Labs & Mini Projects
- Lab challenges : Some online resources have "challenge labs" for CCNA (like showing a network diagram and asking you to configure STP priorities, etc.). If you find one, try it out. Practice exam on L2 : If your study resources have topic-wise exams, take one on "Network Access" at the end of this week to gauge your progress on switching topics. Hands-On Labs/Projects: 89 17
- Lab 6.1: Spanning Tree Exploration - Use your Lab 5.3 topology (two switches connected by two links? If not, create a scenario with 2 switches and 2 redundant links between them, plus a couple PCs). By default STP will block one link. Use show spanning-tree on each switch to identify the root bridge, root ports, and blocked port. Task: Change the bridge priority on one switch to make it the root for VLAN1 deliberately (e.g., spanning-tree vlan 1 priority 4096). Observe how STP reconverges and which ports are now forwarding/blocking. Also test PortFast: set one of the PC access ports as PortFast ( spanning-tree portfast on Cisco). The PC's port should go into forwarding immediately on link up (in PT this might be hard to notice, but conceptually note it). Expected Outcome: You can interpret STP status and influence root election. Document which switch became root and which port got blocked and why.
- Lab 6.2: Configure EtherChannel (LACP) - Take two switches with 4 connections between them (or add additional links to an existing topology). Before EtherChannel, STP would block all but one. Now configure EtherChannel: e.g. on both switches do interface range f0/1-2 , channel-group 1 mode active (LACP active). Do same for f0/1-2 on the other switch (active or passive mode). This should form an EtherChannel bundling two ports. Verify with show etherchannel summary . Ensure you assign the EtherChannel (Port-channel1) as trunk or access appropriately. Expected Outcome: The EtherChannel comes up (flags "SU" in summary) and STP now sees it as a single link, preventing loops while both physical links carry traffic. Test by sending pings while bringing down one member link to see traffic continues.
- Lab 6.3: Integrated Network Challenge - Design a scenario that uses everything from

## Milestones & Checkpoints
- Add your own items from the study plan.

## Lab Log
| Date | Lab / Config | Key Takeaways | Evidence (files/screens) |
| --- | --- | --- | --- |
|  |  |  |  |
