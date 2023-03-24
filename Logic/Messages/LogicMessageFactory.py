import os

packets = {}
for file_name in os.listdir('Logic/Messages/Client/'):
    if file_name.endswith('.py'):
        module_name = file_name.replace('.py', '')
        packet_class = getattr(__import__(f'Logic.Messages.Client.{module_name}', globals(), locals(), [module_name], 0), module_name)
        packet_instance = packet_class
        packet_info = packet_class(None, None, None)
        packets[packet_info.id] = packet_instance
print(f"{len(packets)} Packets loaded!")


def getPackets():
    return list(packets.keys())