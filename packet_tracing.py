import os
from datetime import datetime

# run tshark in the terminal
# command: python3 packet.py
# for 30 seconds and save the output to a file
def run_Wireshark_tshark():
    # set filename to the current date time
    pcapng_file = f"{datetime.now().strftime('%H-%M-%S')}"
    # save as wireshark file
    os.system(f"touch {pcapng_file}.pcap")
    os.system(f"chmod o=rw {pcapng_file}.pcap")
    # run tshark for 30 seconds
    os.system(f"sudo tshark -a duration:30 -w {pcapng_file}.pcap")
# run function
run_Wireshark_tshark()