import socket

def algo():
    # Key Set 
    keyset = [(["a", "b", "c", "d", "e"], ["f", "g", "h", "i", "j"], ["k", "l", "m", "n", "o"],
                ["p", "q", "r", "s", "t"], ["u", "v", "w", "x", "y"], ["z"]),  # lowcase keyset
                (["1", "2", "3", "4", "5"], ["6", "7", "8", "9", "0"]),    # numeric keyset
                ([".", ",", "?", "/", "#"], ["'", ":", ";", "@", "+"], ["-", "%", "*", "(", ")"],  # punctuation keyset
                ["=", "&", "£", "$"])]

    count = 0 # For iteration in a keyset
    key = 0 # For iteration between keysets
    
    try: 
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # For UDP
        #udp_host = "100.71.209.169"  # Host IP (IPv4 Address)
        #udp_port = 12345 # Specified port to connect

        s.bind(("192.168.1.180", 1234))
        print ("Sever open, waiting for client input...\n")
       
        while True:
            data, addr = s.recvfrom(1024) # Receive data from client
            i = data.decode()
            try:
                if i == "21":
                    print(keyset[key][count][0], end="")
                elif i == "20":
                    print(keyset[key][count][1], end="")
                elif i == "16":
                    print(keyset[key][count][2], end="")
                elif i == "26":
                    print(keyset[key][count][3], end="")
                elif i == "19":
                    print(keyset[key][count][4], end="")
                elif i == "13":
                    print(" ", end="")
                elif i == "12": # Ensures the count loops back to 0 when the end of the keyset is found
                    if count < len(keyset[key])-1: 
                        count += 1
                    else:
                        count = 0
                elif i == "6": # Iterators between keysets RESETS COUNT TO RESTART ITERATION WHEN SWITCHING KEYSETS
                    if key < len(keyset)-1:
                        count = 0
                        key += 1
                    else:
                        count = 0
                        key = 0
                else:
                    pass
            except IndexError: # Ensures last indexes don't cause errors
                pass
    except Exception as e:
        print(e)


if __name__ == "__main__":
    algo()

# CODE NEEDED FOR GUI?
