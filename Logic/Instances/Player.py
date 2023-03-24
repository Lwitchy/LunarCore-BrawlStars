class ServerConfiguration:
    pass
    
class Player:
    # Auth Information
    high_id = 0
    low_id = 1
    token = "Nothing"

    # Player Information Phase 1
    name = "Guest"
    name_set = False
    trophies = 0
    high_trophies = 0
    collected_trophyroad = 1
    exp_points = 0
    thumbnail = 0
    name_color = 0
    region = "AZ"

    offers = [
    ]

    # Unlocked Data
    unlocked_brawlers = [0,8]
    unlocked_skins = []
    unlocked_accessories = []
    unlocked_pins = []

    # Selected Data
    selected_brawler = 0
    brawler_newtags = {}
    selected_skins = {}
    selected_pins = {}
    selected_gadgets = {}
    selected_sp = {}

    # Brawler Data
    brawlers_level = {}
    brawlers_powerpoints = {}
    brawlers_trophies = {}
    brawlers_high_trophies = {}

    # CSV Data
    # Phase 1
    all_brawlers = []
    all_skins = []

    # Phase 2
    brawler_skins = {}
    skin_prices = {}
    brawler_cardID = {}

    # Phase 3
    maps_all = {}
    maps_gem = []
    maps_showdown = []
    maps_brawlball = []
    maps_siege = []
    maps_heist = []
    maps_hotzone = []
    maps_bounty = []
    maps_biggame = []


    # Server Settings: Don't Edit

    last_playerLowID = 0
    last_playerHighID = 0
    last_clubID = 0
    last_gameRoom = 0

    server_commands = {}
    client_commands = {}

    slot_data = [
    ]

    def updateData():
        # Update data
        for id in Player.unlocked_brawlers:
            Player.selected_pins.update({f"{id}": 0})
            Player.selected_skins.update({f"{id}": 0})
            Player.selected_sp.update({f"{id}": 0})
            Player.brawler_newtags.update({f"{id}": 0})
            Player.selected_gadgets.update({f"{id}": 0})
        
        for x in Player.unlocked_brawlers:
            Player.brawlers_trophies.update({f'{x}': 0})
        
        for x in Player.unlocked_brawlers:
            Player.brawlers_high_trophies.update({f'{x}': 0})
        
        for x in Player.unlocked_brawlers:
            Player.brawlers_level.update({f'{x}': 0})

        for x in Player.unlocked_brawlers:
            Player.brawlers_powerpoints.update({f'{x}': 0})        
        
        