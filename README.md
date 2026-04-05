# Network-Port-Scanning-Tool
A Network Port Scanner is a cybersecurity tool used to scan a computer or network to identify open ports, closed ports, and filtered ports. Ports are communication endpoints through which network services such as HTTP, FTP, SSH, and SMTP run.    Attackers often exploit open ports to gain unauthorized access.

1. Introduction
A Network Port Scanner is a cybersecurity tool used to scan a computer or network to identify open ports, closed ports, and filtered ports. Ports are communication endpoints through which network services such as HTTP, FTP, SSH, and SMTP run. Attackers often exploit open ports to gain unauthorized access, so port scanning is an important part of network security and vulnerability assessment.

The main purpose of this project is to design and develop a tool that scans a target IP address and identifies which ports are open and what services are running on them.

2. Problem Statement
In computer networks, open ports can become entry points for cyber attacks if not properly secured. Network administrators need a method to identify open ports and services running on systems to prevent security vulnerabilities. Therefore, the project aims to develop a Network Port Scanner that scans target systems and reports open ports and associated services.

3. Objectives of the Project
The main objectives of the Network Port Scanner project are:
To scan a target IP address or hostname.
To identify open, closed, and filtered ports.
To detect services running on open ports.
To generate a scan report.
To help in network security assessment and vulnerability detection.

4. Scope of the Project
This project can be used by:
Network administrators
Cybersecurity students
Ethical hackers
System administrators

The scanner can be used in:
Vulnerability assessment
Network monitoring
Security auditing
Penetration testing (ethical hacking)

5. Working
The Network Port Scanner works in the following steps:

User enters target IP address or domain name.
The scanner selects a range of ports (e.g., 1–1024).
The program sends TCP/UDP connection requests to each port.
If the port responds → Port is Open.
If the port rejects → Port is Closed.
If no response → Port is Filtered.
The scanner identifies services running on open ports.
The results are displayed or saved in a report.

6. Tools and Technologies Used
Common tools and technologies:
Programming Language: Python / C / Java
Socket Programming
Networking Protocols (TCP, UDP)
Operating System: Linux / Windows
Libraries: Python socket, threading, nmap 

7. Features of Network Port Scanner
Scan single host
Scan multiple ports
Fast scanning using multithreading
Service detection
Report generation
User-friendly interface

8. Applications
Network Security Testing
Vulnerability Assessment
Ethical Hacking
System Administration
Firewall Testing
Network Monitoring

9. Conclusion
The Network Port Scanner project helps in identifying open ports and services running on a system, which is very useful for network security and vulnerability detection. This project provides practical knowledge of networking, socket programming, and cybersecurity concepts.
