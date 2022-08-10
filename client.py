import socket           # making and connecting sockets and setting the timeout value
import argparse         # input

# LEVEL 1: Able to send Initiate Packet (to the receiver or test server), and receive the Accept Packet (from the receiver or test server). 25 points.
# filename: client.py


# STEP 0: Getting the Command Line Input
# angparse was used so that there can be blank parts
# blank parts will be replaced by the default value/s
# declaration of the use of parser
parser = argparse.ArgumentParser(description='Project Input Parameters.')
# adding of argument 1: -a denotes the IP address of the receiver to be contacted
# type is str
# default value is 10.0.5.69 (given in project specifications)       
parser.add_argument("-a", "--IP_address", type=str,
                    help="IP address of the Receiver", default=f"10.0.5.69")
# adding of argument 2: -s denoting Port number used by the receiver
# type is int
# default value is is your assigned port, in my case is 6679                    
parser.add_argument("-s", "--port_receiver", type=int,
                    help="Port number used by the receiver", default=9000)
# adding of argument 3: -c denoting Port number used by the sender
# type is int
# default value is 9000 (given in project specifications)                   
parser.add_argument("-c", "--port_sender", type=int,
                    help="Port number used by the sender", default=6679)
# adding of argument 4: -i denoting Unique ID
# type is str
# default value is your_id.txt in my case your_id = 2099fba5                    
parser.add_argument("-i", "--unique_ID", type=str,
                    help="Unique ID", default='2099fba5')
args = parser.parse_args()

# STEP 2: Initiating a Transaction

# 2.1   Intent Message XXXXXXXXYYYYYYYYZVVVVVWWWWWTTTTTTTUIN_ANS
# XXXXXXXX is the unique ID given in the email
# YYYYYYYY is the transaction ID (don't care for inititate packet)
# Z is the the flag used to indicate the packet type (set to 8 for initiate packet)
# VVVVV is the the 5-digit starting byte of the requested data portion (don't care for inititate packet)
# WWWWW is the the 5-digit size of the requested data portion (don't care for inititate packet)
# TTTTTTT is the 7-digit unique identity number of the challenge question being answered (don't care for inititate packet)
# UIN_ANS is the answer to the challenge question (don't care for inititate packet)
# DATA is the decrypted data (don't care for inititate packet)

# setting up the intent message of format : 
# unique_ID + transaction_ID + type + PULL_byte + PULL_size + UIN + UIN_size + Data
# default unique_ID = "2099fba5"
transaction_ID = 'YYYYYYYY'
type = '8'
PULL_byte = 'VVVVV'
PULL_size = 'WWWWW'
UIN = 'TTTTTTT'
UIN_size = 'UIN_ANS'
separator = '/'
Data = 'DATA'
intent_message = f"{args.unique_ID}{transaction_ID}{type}{PULL_byte}{PULL_size}{UIN}{UIN_size}{separator}{Data}".encode()

# 2.2   Accept Message YYYYYYY
# accept message will be printed out once it is proven 
# that there is no alive transaction after doing 2.1
# YYYYYYY is the transaction id that allows the user to check if the transmission is valid
# socket initialization
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind socket address to port receiver
sock.bind(('', args.port_sender))
# using the intent message from 2.1 send data to address
sock.sendto(intent_message, (args.IP_address, args.port_receiver))
# store the acknowledgement number from port
acknowledgement, __ = sock.recvfrom(1024)
# timer for start of initiation
# start_time = time.time()
# decode acknowledgement number
trasaction_ID = acknowledgement.decode()
print(trasaction_ID)