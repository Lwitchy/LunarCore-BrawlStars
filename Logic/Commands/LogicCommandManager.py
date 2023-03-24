import os

server_commands = {}
client_commands = {}

def loadClientCommands():
    for file_name in os.listdir('Logic/Commands/Client/'):
        if file_name.endswith('.py'):
            module_name = file_name.replace('.py', '')
            packet_class = getattr(__import__(f'Logic.Commands.Client.{module_name}', globals(), locals(), [module_name], 0), module_name)
            packet_instance = packet_class
            packet_info = packet_class(None, None, None)
            client_commands[packet_info.id] = packet_instance
    print(f"{len(client_commands)} Client Commands loaded!")   


def loadServerCommands():
    for file_name in os.listdir('Logic/Commands/Server'):
        if file_name.endswith('.py'):
            module_name = file_name.replace('.py', '')
            packet_class = getattr(__import__(f'Logic.Commands.Server.{module_name}', globals(), locals(), [module_name], 0), module_name)
            packet_instance = packet_class
            packet_info = packet_class()
            server_commands[packet_info.id] = packet_instance
    print(f"{len(server_commands)} Server Commands loaded!")


def getServerCommands():
    return list(server_commands.keys())