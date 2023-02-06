""""
This script will extract the messages that agents sends to server from log files, 
and separate them by agent number.
"""
import os
sin_path = os.path.dirname(os.path.realpath(__file__))


for root, dirs, files in os.walk(sin_path):
    for file in files:
        msg_toServer = [];
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                if "ServerComm.cpp::58" in line:
                    msg_toServer.append(line)

        with open(f"{file}ServerMsg.txt", 'a') as save:
            for line in msg_toServer:
                line = line.replace("ServerComm.cpp::58 - Message to Server : ", "")
                save.write(f"\n{line}")
