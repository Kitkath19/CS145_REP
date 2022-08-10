# CS145 Replacement Project 1
This project was made by Kathryn Cantor from Lab-2 of CS145 A.Y.2021-2022B.
The program created is an implementation of the sender side of a protocol. The network protocol 
used in tis project is a pipelined protocol built on top of UDP. The goal is for the payload of
the sender to reach the receiver of the test server. The program is created in Python 3.


# Level of implementation: 1


# Files Included
- client.py - sender code to be used throughout the project
  - command: python3 python3 client.py -a 10.0.5.69 -s 9000 -c 6679 -i 2099fba5 
- packet_tracing.py - Wireshark/Tshark tracefile generator used in the project
  - command: python3 packet_tracing.py
  
  
# Project Implementation
1. Open 2 (two) terminals
  - Terminal A: running the sender code
  - Terminal B: running the packet tracing code (wireshark/tshark)

2. Connect to the AWS serve
  - SSH in the terminal using the command: ssh -i "<key>" ubuntu@<PUBLIC IP address>
  - in my case it is: ssh -i "kdlc.pem" ubuntu@<PUBLIC IP address>

3. Connect to GitHub
  - once connected always do a "git pull" to update the files in the current directory

4. Send in the command to Terminal B first, make sure you do this first
  - command: python3 packet_tracing.py

5. Once, tracefile is being generated, Send in the command to Terminal A
  - command: 	python3 client.py -a 10.0.5.69 -s 9000 -c 6679 -i 2099fba5 
         	-a    	IP address of the receiver
          	-s    	port used by the receiver
         	-c    	port used by the sender
          	-i	unique ID

6. "git push" so that you can access the tracefile

7. Check if the transaction ID printed is found in the website http://18.143.61.154:5000/transactions. (Note that the Duration would be 120 and Result is Failed to send data since this is a level 1 implementation.)

8. for additional experiments, go back to step 3
