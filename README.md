# Brute Force MITM Attack

## Objective
I co-authored the article "**Advanced Persistent Threats and WLAN Security: An In-depth Exploration of Attack Surfaces and Mitigation Techniques**" alongside Dr. Hosam Alamleh, Dr. Shadman Sakib Arnob, and Dr. Ali Abdullah S. AlQahtan. My contributions focused on analyzing the attack surfaces of WLANs, where I conducted tests on man-in-the-middle (MITM) and dictionary-based attacks on Wi-Fi networks, including KRACK and Downgrade Attacks.

## Abstract
Wi-Fi-enabled Wireless Local Area Networks (WLANs) are critical to modern connectivity, with a growing number of Wi-Fi devices worldwide. Ensuring the security of WLANs is of utmost importance, as they support a wide range of activities. This paper provides a comprehensive analysis of WLAN attack surfaces, categorizing them into three main areas:
1. **Radio Access Network**  
2. **Compromised Insider Nodes**  
3. **Gateway to the Internet Service Provider**  

We examine how Advanced Persistent Threats (APTs) can amplify attacks on these surfaces and pose substantial risks to individuals and organizations. The paper also evaluates current WLAN implementations' ability to mitigate APTs and explores future design strategies to improve security. Our findings highlight the challenges of securing WLANs due to their extensive attack surface and propose methods to strengthen Wi-Fi security.

## Code Overview
The script, written in Python, is designed for use in **Kali Linux** and allows for Wi-Fi password cracking through brute-force and dictionary attacks. The script generates a **custom password dictionary** by combining words from up to four user-specified files, along with numbers and special characters, to create all possible permutations. Here’s a breakdown of how it works:

1. **Loading Files**: The program loads words from the user-provided files and strips any whitespace, storing them in lists.
2. **Generating Numbers and Special Characters**: It generates a list of three-digit numbers (ranging from 000 to 999) and adds special characters like `!`, `@`, `#`, etc.
3. **Creating Word Combinations**: It creates 2-word, 3-word, and 4-word combinations by selecting words from different files, producing all possible arrangements (e.g., "catred" or "dogblue").
4. **Adding Numbers and Special Characters**: The program appends numbers and special characters to each word combination, creating more permutations. Examples include "catdog123", "123catdog", "$catdog123", and others.
5. **Output**: The generated permutations are written to a file named **dictionary.txt**, which can be used in security testing or password-cracking exercises.

This script demonstrates **combinatorics**, **file manipulation**, and **string formatting** in Python, providing a practical tool for Wi-Fi security testing.

## Attack Methodology
### Wi-Fi Password Cracking
To perform a Wi-Fi password cracking attack using Kali Linux, attackers typically target the **Pre-shared Key (PSK)** authentication process, which is vulnerable to both online and offline attacks.

1. **Online Attacks**: These attacks are conducted in real time by interacting directly with the network. Tools like **Aircrack-ng** can capture data packets during Wi-Fi activity and attempt to guess the password using methods such as dictionary or brute-force attacks. However, these attacks are limited by network traffic and the access point’s ability to handle multiple requests, making them slower and more detectable.

2. **Offline Attacks**: These are more efficient and discreet. They begin by capturing the **4-way handshake** between a client and the Wi-Fi access point, which can be done with tools like **Airodump-ng**. The handshake contains critical cryptographic information such as:
   - Anonce (random number from the access point)
   - Snonce (random number from the client)
   - PMK (Pairwise Master Key)
   - PTK (Pairwise Transient Key)

   Once the handshake is captured, it can be used for offline attacks using tools like **Hashcat** or **John the Ripper**, making these attacks faster and stealthier since they don't depend on live network activity.

### Advanced Attacks
1. **KRACK Attack (Key Reinstallation Attack)**: This attack exploits vulnerabilities in the WPA2 protocol's implementation, allowing an attacker to force a victim to reinstall an already-used encryption key, enabling the decryption of intercepted traffic. This attack doesn’t require the victim’s password, making it particularly dangerous.

2. **Downgrade Attacks**: By forcing devices to switch from WPA3 to the less secure WPA2, attackers can exploit known vulnerabilities, making it easier to crack the network.

### Scaling the Attack
To increase the effectiveness of these attacks, especially when moving from online to offline methods, attackers often use **GPU-based cracking** tools like **Hashcat** to accelerate password cracking. While brute-force attacks can be resource-intensive, they are still effective if the password isn’t too complex. Dictionary attacks, relying on precompiled lists of common passwords, are faster but less effective if the target’s password is unique.

### Summary
Kali Linux offers powerful tools for both online and offline Wi-Fi password cracking. Offline attacks, which rely on captured handshakes, are faster, stealthier, and more efficient than online attacks, as they utilize local computational power instead of depending on live network activity.

## Conclusion
This project demonstrates the importance of securing WLANs and provides insights into how attackers exploit vulnerabilities in Wi-Fi networks. Through the use of Python scripting and Kali Linux tools, we can simulate attacks and better understand the methods and resources required to conduct both online and offline Wi-Fi password cracking attempts.
