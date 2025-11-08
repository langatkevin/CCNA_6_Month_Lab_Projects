# Week 10 - Device Security and Access Control

> Adapted from the "6-Month CCNA 200-301 Study Plan" reference.

## Objectives
- Learn about basic device hardening : setting strong passwords (console, VTY, enable secret) , using password policies (minimum length, complexity, etc.) , and the importance of disabling unused services. Configure these on a lab router/switch.
- Understand AAA (Authentication, Authorization, Accounting) concepts : not configure in depth (that's CCNP), but know that AAA can use local or external (RADIUS/TACACS+ servers). Understand how a
- Cisco device can use a central server to authenticate admins. Possibly configure a simple local AAA authentication for login as practice.
- Configure SSH on a Cisco device: generate RSA keys, set up username/password or AAA, and verify
- SSH login. Ensure Telnet is disabled (only SSH allowed).
- Implement Port Security on a switch : limit MAC addresses on a port (e.g., only allow one MAC and shutdown if violation). Test by connecting a different device to see the violation.
- Implement ACLs (Access Control Lists) on a router : Standard ACL vs Extended ACL differences.
- Practice creating a standard ACL to filter traffic (e.g., block one network from accessing another) and an extended ACL (e.g., permit HTTP but block Telnet). Apply ACLs inbound or outbound on interfaces appropriately and test.
- Understand ACL best practices and how they're used for security (basic firewalling) and for control plane (e.g., line VTY ACL to limit who can SSH).
- Cover Device login banners (MOTD) for legal warning, and the concept of physical security (briefly).
- This week is heavy on configuration - it solidifies as you do it practically.

## Hands-On Labs & Mini Projects
- Lab 10.1: Secure Management Config - Take a lab router/switch, configure: an enable secret, local user account with privilege 15, console login using local, VTY login using local with transport input SSH only, generate RSA keys, and test SSH from a PC. Also set service password-encryption (so your line passwords are encrypted in config). Finally, set a login banner (MOTD). Expected Outcome: You can only access the device via SSH with the correct user/pass, and console also requires login. The config should show encrypted passwords. Document these steps as if making a checklist (will be useful later).
- Lab 10.2: Port Security Demo - On a switch, pick an access port connected to a PC. Configure switchport port-security (default allows one MAC) and maybe violation shutdown . Connect the PC, see it works. Now disconnect that PC and connect a different device (or change the MAC in PT by replacing the NIC or using another PC). The port should go into err-disable. Check show port-security interface X to see the violation count. Then re-enable the port ( shutdown/no shutdown ) and possibly set it to violation protect mode to see difference (in protect, won't shut, but drops unknown MAC traffic). Expected Outcome: Understanding how port security can block devices beyond the first.
- Lab 10.3: ACL Practice - a) Standard ACL : On a router with two subnets (A and B), create a standard ACL to block traffic from one specific host or subnet A from reaching subnet B. Apply it inbound on interface toward B. Test with pings: the blocked host should fail, others succeed. b) Extended ACL : e.g., block HTTP from one network to a server , but allow other traffic. Use an extended ACL applied appropriately. Alternatively, implement an ACL on VTY lines to allow only a specific IP range to telnet/SSH to the router (for management plane security). Expected Outcome: You can write ACL statements (with correct wildcard masks, host vs any keywords) and apply them correctly (right interface, right direction) to achieve desired filtering. Use show access-lists to see hit counts after tests.
- Lab 10.4: Layer 2 Security - If Packet Tracer supports, try enabling DHCP Snooping on a switch (specify trusted ports vs untrusted) and then simulate a rogue DHCP (PT might not easily simulate rogue server , but you can place a second DHCP server in a VLAN and see if snooping blocks it). Similarly, DAI needs ARP packets - may skip actual test, but know config. If not feasible, at least review how to enable those (e.g., ip dhcp snooping globally and per VLAN).
- Lab 10.5: Wireless Security - On a wireless router/AP in PT, try setting different security modes (WEP, WPA2, etc.) to see how a client connects with each. Note how a weak security (like WEP) could be cracked (just conceptually). If possible, show that without knowing passphrase, client can't connect - obvious, but demonstrates necessity of proper Wi-Fi auth. (Project) Security Audit Checklist: Create a checklist for securing a small network device: e.g., "1. Set enable secret, 2. Disable unused ports or put in unused VLAN, 3. Apply port security on access ports, 4. Use SSH not Telnet, 5. Use strong passwords and maybe AAA, 6. Implement ACLs to limit access to network segments, 7. Enable logging and NTP for time sync (for accurate logs), etc." This can be compiled from Cisco best practices. Use this list to verify your own labs have no glaring holes.

## Milestones & Checkpoints
- Milestone 1: Harden a device and verify: e.g., a switch that only allows SSH login with a specific user , and has console secured. Attempt to telnet (should fail), attempt SSH with wrong user (fail), right user (success). If possible, get a peer to try to "break in" (or just simulate by trying defaults) to ensure it's secure.
- Milestone 2: Successfully use port security to shut down a port on unauthorized device connection. Check that you know how to bring it back ( errdisable recovery or manual shut/no shut).
- Milestone 3: Implemented ACLs that work as intended. Document one example: "Standard ACL 10 blocking Network X applied on interface G0/0 inbound blocked traffic successfully as shown by ping tests." Also note ACL best practice (like placing, and remember implicit deny at end).
- Milestone 4: Quick-fire: be able to answer "How to mitigate X?" for the common threats: e.g., MAC flooding -> Port Security, rogue DHCP -> DHCP Snooping, ARP Poisoning -> DAI, brute-force on device -> strong passwords & login delay, etc. You don't need to know deep, just a one-liner mitigation.
- Milestone 5: Achieve ~80% across security quizzes. If there's any term or tech you missed, review it. For instance, if you blanked on "what does SNMPv3 add" (security), just note it down. If ACL logic confused you (like order of lines or implicit deny), clarify with more practice.
- Checkpoint: At this point, you have completed an initial pass through all CCNA domains . Congrats! You likely have a pile of notes, lab configs, and flashcards. For the remainder of Month 4 and in Month 5, we'll focus on automation plus heavy review and practice exams to solidify everything. Use this checkpoint to identify your weakest areas - maybe it's OSPF, or ACLs, or subnetting under time. Flag them for extra attention in coming weeks.

## Lab Log
| Date | Lab / Config | Key Takeaways | Evidence (files/screens) |
| --- | --- | --- | --- |
|  |  |  |  |
