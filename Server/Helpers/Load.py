

class Loader:
    def init(self, Player, CSVReader):
        # Load Characters
        characters = CSVReader().readCharacters()
        Player.all_brawlers = characters

        # Character Card ID
        for x in Player.all_brawlers:
            card_id = CSVReader().readCardID(x)
            Player.brawler_cardID[x] = card_id

        # Load Skins
        skins = CSVReader().readSkins()
        Player.all_skins = skins
        
        # Load Skin Prices
        for x in Player.all_skins:
            cost = CSVReader().readSkinPrices(x)
            Player.skin_prices.update(cost)

        # Load Skins for Brawlers
        for x in Player.all_brawlers:
            list = CSVReader().readAllSkinsForBrawler(x)
            data1 = {f"{x}": list}
            Player.brawler_skins.update(data1)

        # Load Maps
        Player.maps_all = CSVReader.readAllMaps(self)

        # Load Gem Grab Maps
        Player.maps_gem = CSVReader.readGemGrabMaps(self)

        # Load Showdown Maps
        Player.maps_showdown = CSVReader.readShowdownMaps(self)

        # Load BrawlBall Maps
        Player.maps_brawlball = CSVReader.readBrawlBallMaps(self)

        # Load Siege Maps
        Player.maps_siege = CSVReader.readSiegeMaps(self)

        # Load Heist Maps
        Player.maps_heist = CSVReader.readHeistMaps(self)

        # Load Bounty Maps
        Player.maps_bounty = CSVReader.readBountyMaps(self)

        # Load Big Game Maps
        Player.maps_biggame = [119]

        print("Loaded CSV Data:")
        print(f"  {len(characters)} Brawler loaded!")
        print(f"  {len(skins)} Skin loaded!")
