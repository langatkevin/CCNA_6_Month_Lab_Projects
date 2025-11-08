# Week 11 - Automation & Programmability Fundamentals

> Adapted from the "6-Month CCNA 200-301 Study Plan" reference.

## Objectives
- Grasp why network automation and programmability are emerging: the need for scale, consistency, and integration with DevOps. Understand terms like SDN (Software-Defined Networking) - separating control plane and data plane, and APIs (Application Programming Interfaces) - how software can interact with network devices.
- Learn about REST APIs in the context of networking: e.g., Cisco's RESTful APIs (like those on Cisco
- DNA Center or even some on IOS-XE). Understand what CRUD means (Create, Read, Update, Delete) and that these map to HTTP verbs (POST, GET, PUT/PATCH, DELETE).
- Get exposure to data formats like JSON (JavaScript Object Notation) and maybe XML - CCNA expects you to recognize JSON output and basic structure (key:value pairs, nested). Practice reading a
- JSON snippet and locating a piece of data (like an IP address in a JSON of interface info).
- Explore network automation tools : Know of Puppet, Chef, Ansible (just what they are, not how to use) . Ansible is popular for network automation (YAML playbooks). Puppet/Chef are more used in server world but Cisco wants you aware.
- Basic scripting intro: write a very simple Python script to retrieve or configure something, or just parse some output. If you're new to coding, at least understand a provided Python script that uses a library like netmiko or requests to call a REST API. We won't become coders in a week, but break the ice.
- Use Cisco's DevNet resources if possible: maybe use the Cisco DevNet sandbox or their always-on sandboxes for DNA Center or CSR1000v API to try a sample API call (alternatively, use Packet Tracer's new REST-based multiuser feature if exists, or just conceptual).
- Tie back to exam: ensure you can answer conceptual Qs like "What is the benefit of controller-based networking?" , "What is an example of southbound API vs northbound API?" (Southbound: e.g.,
- OpenFlow, NETCONF; Northbound: REST API to controller). Recognize JSON and interpret it.
- This week is more about reading/understanding than heavy lab, unless you're comfortable to try some coding.

## Hands-On Labs & Mini Projects
- Lab 11.1: Explore a REST API - Use a tool like Postman (install on your computer) or Python requests library to GET data from an API. If you don't have a Cisco device API, use something like httpbin or a dummy JSON API. Alternatively, many Cisco devices have an HTTP interface you could enable (not secure, but for test). If you can, enable REST API on a DevNet sandbox or CSR1000v VM (this might be advanced - if not, skip doing it yourself). At least, open a sample JSON file (maybe Odom's book has one, or find on DevNet) and try to pick out key info. Expected Outcome: You understand how an API call returns structured data (JSON) and how it differs from CLI show output. 108 65 35
- Lab 11.2: Simple Python Script - Write or copy a short script that does something like "print all IP addresses in this JSON" or "SSH to router and run show ip int brief (using netmiko)". If you've never coded, ask a programmer friend or find a ready script from DevNet Code Exchange. Running it successfully and seeing output is the goal. If not comfortable, at least go through the thought: how would automation save time vs manual CLI (imagine configuring 100 VLANs on 10 switches - script can do it faster with less error).
- Lab 11.3: Controller Demo - If possible, watch a demo or recording of Cisco DNA Center or Packet Tracer's SDN Controller (PT has a "Controller" object for SDN but not sure how functional). At least conceptually: one central controller can push VLAN configs to all switches or do dynamic path optimization. Recognize how this differs from logging individually.
- Lab 11.4: JSON Parsing Exercise - Create a small JSON structure (or use sample) that includes network info, e.g.: {"interface": "Gig0/1", "ip_address": "10.0.0.1", "status": "up"}. Write down how you'd access the IP address field (answer: by key "ip_address"). Maybe test with a Python one-liner if possible: import json; data=json.loads(<jsonstring>); print(data["interface"]) to print values. Expected Outcome: Not to memorize syntax but to demystify JSON (it's just text with keys/values, often easier than parsing CLI output). (Project) Automation Strategy Proposal: Imagine you manage 50 switches - list 3 tasks you would script/automate (e.g., backup configs nightly, bulk update SNMP community, verify interfaces up). For each, describe how automation helps (less error , schedule it, etc.). This isn't on exam, but thinking this way prepares you for real network engineering in modern environments and gives context to why Cisco added this domain.

## Milestones & Checkpoints
- Milestone 1: Write a short explanation (4-5 sentences) of the difference between traditional networking vs controller-based. E.g., "Traditional: each device configured individually (CLI), control plane distributed; Controller-based: central brain (controller) tells devices how to forward, devices are simpler , easier to enforce policies network-wide." If you can articulate that, you got the core idea .
- Milestone 2: Interpret a given JSON. For instance, take: {"device": {"name": "R1", "interfaces": [{"name": "Gig0/0", "ip":"10.0.0.1"}, {"name":"Gig0/1","ip":"10.0.1.1"}]}} . Answer: how many interfaces does R1 have and what are their IPs? (Should be: 2 interfaces, IPs 10.0.0.1 and 10.0.1.1). If you can do that, you're good for JSON interpretation .
- Milestone 3: (Optional but cool) Successfully run a simple network automation action - whether it's an API GET retrieving something or using a script to login and run a command. If accomplished, celebrate you've stepped into netprog! If not, at least know what such a script would generally look like.
- Milestone 4: Complete the full practice exam and identify improvement areas. Suppose you scored, say, 70% - not bad for first full attempt; list which sections had wrong answers. Make a plan to review those (which we'll do Week 12 and Month 5). If you scored 90% - great, but still review any misses and note if it was luck on some guesses; ensure those are solidified.
- Checkpoint: Content learning phase is nearly done. All topics are covered. The focus shifts to reinforcing knowledge, practicing scenarios, and test readiness . Compare where you were at Month 1 vs now - impressive progress, right? The next step: refine until you're consistently exam-ready and confident in practical skills too. Use Month 5 for that polishing, plus a capstone project to apply everything.

## Lab Log
| Date | Lab / Config | Key Takeaways | Evidence (files/screens) |
| --- | --- | --- | --- |
|  |  |  |  |
