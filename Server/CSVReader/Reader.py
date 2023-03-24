#from Logic.Assets
import csv
path = 'Logic/Assets/csv_logic/'

class CSVReader:
    def __init__(self) -> None:
        pass

    def readCSV(self, filename, isEncodeUTF = False) -> None:
        self.rowData = []
        self.lineCount = 0
        if(isEncodeUTF):
            with open(filename, encoding='utf-8') as csvFile:
                self.csvReader = csv.reader(csvFile, delimiter=',')
                for row in self.csvReader:
                    if self.lineCount == 0 or self.lineCount == 1:
                        self.lineCount += 1
                    else:
                        self.rowData.append(row)
                        self.lineCount += 1
            return self.rowData
        else:
            with open(filename) as csvFile:
                self.csvReader = csv.reader(csvFile, delimiter=',')
                for row in self.csvReader:
                    if self.lineCount == 0 or self.lineCount == 1:
                        self.lineCount += 1
                    else:
                        self.rowData.append(row)
                        self.lineCount += 1
            return self.rowData   


    def readCharacters(self):
        global path
        brawlers = []
        reader = CSVReader()
        charsData = reader.readCSV(f'{path}/characters.csv')

        for row in charsData:
            if row[20] == 'Hero' and row[2].lower() != 'true' and row[1].lower() != 'true':
                brawlers.append(charsData.index(row))

        return brawlers

    def readSkins(self):
        global path
        skins = []
        reader = CSVReader()
        skinData = reader.readCSV(f'{path}/skins.csv')
        #skinConfData = reader.readCSV(f'{path}/skin_confs.csv')
        for row in skinData:
            if 'Default' not in row[0]:
                skins.append(skinData.index(row))
        
        return skins


    def readSkinPrices(self, skinID):
        global path
        skinCurrencyInfo = {}
        reader = CSVReader()
        skinsData = reader.readCSV(f"{path}/skins.csv")
        for row in skinsData:
            if skinsData.index(row) == skinID:
                if row[7]:
                    skincost = row[7]
                    skincurrency = 3
                elif row[8]:
                    skincost = row[8]
                    skincurrency = 0
                elif row[9]:
                    skincost = row[9]
                    skincurrency = 1
                else:
                    skincost = 0
                    skincurrency = 0
                
                skincurrency = {
                    f"{skinID}":{
                        "Cost": skincost,
                        "Currency": skincurrency 
                    }
                }

                return skincurrency


    def readCardID(self, brawlerID):
        global path
        reader = CSVReader()
        charsData = reader.readCSV(f'{path}/characters.csv')
        cardsData = reader.readCSV(f'{path}/cards.csv')

        for row in charsData:
            if charsData.index(row) == brawlerID:
                name = row[0]
                for row in cardsData:
                    if row[6].lower() == '0' and row[3] == name:
                        return cardsData.index(row)

    def readAllSkinsForBrawler(self, brawlerID):
        global path
        skinsID = []
        reader = CSVReader()
        charsData = reader.readCSV(f"{path}/characters.csv")
        skinsData = reader.readCSV(f"{path}/skins.csv")
        skinConfsData = reader.readCSV(f'{path}/skin_confs.csv')
        for row in charsData:
            if charsData.index(row) == brawlerID:
                brawlerName = row[0]
                for row in skinConfsData:
                    if row[1] == brawlerName:
                        skin_name = row[0]
                        if not "Default" in skin_name:
                            for row in skinsData:
                                if row[0] == skin_name:
                                    skinsID.append(skinsData.index(row))
        return skinsID
    
    def readAllMaps(self):
        global path
        all_maps = {}
        reader = CSVReader()
        maps_data = reader.readCSV(f"{path}/locations.csv", True)

        for row in maps_data:
            if not row[1]:
                map = {
                    f"{str(row[0])}": maps_data.index(row)
                }
                all_maps.update(map)
        
        return all_maps
    
    def readGemGrabMaps(self) -> list:
        global path
        maps = []
        reader = CSVReader()
        maps_data = reader.readCSV(f"{path}/locations.csv", True)

        for row in maps_data:
            if not row[1]:
                if "Gemgrab" in row[0]:
                    maps.append(maps_data.index(row))

        return maps

    def readShowdownMaps(self) -> list:
        global path
        maps = []
        reader = CSVReader()
        maps_data = reader.readCSV(f"{path}/locations.csv", True)

        for row in maps_data:
            if not row[1]:
                if "Survival" in row[0] and "Team" not in row[0]:
                    maps.append(maps_data.index(row))

        return maps
    
    def readBrawlBallMaps(self) -> list:
        global path
        maps = []
        reader = CSVReader()
        maps_data = reader.readCSV(f"{path}/locations.csv", True)

        for row in maps_data:
            if not row[1]:
                if "Ball" in row[0]:
                    maps.append(maps_data.index(row))

        return maps    

    def readSiegeMaps(self) -> list:
        global path
        maps = []
        reader = CSVReader()
        maps_data = reader.readCSV(f"{path}/locations.csv", True)

        for row in maps_data:
            if not row[1]:
                if "Siege" in row[0]:
                    maps.append(maps_data.index(row))

        return maps    

    def readHeistMaps(self) -> list:
        global path
        maps = []
        reader = CSVReader()
        maps_data = reader.readCSV(f"{path}/locations.csv", True)

        for row in maps_data:
            if not row[1]:
                if "Heist" in row[0]:
                    maps.append(maps_data.index(row))

        return maps 

    def readBountyMaps(self) -> list:
        global path
        maps = []
        reader = CSVReader()
        maps_data = reader.readCSV(f"{path}/locations.csv", True)

        for row in maps_data:
            if not row[1]:
                if "Wanted" in row[0]:
                    maps.append(maps_data.index(row))

        return maps 


    def readGadgets(self):
        pass

    def readThumbnails(self):
        pass

    def readNameColors(self):
        pass