with open('output_1.txt','r') as f:
    chatting = f.readlines()

with open('output_2.txt','w') as y:
    for msg in chatting:
        y.write(msg.split(":")[-1])
        y.write("\n")