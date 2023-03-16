import colour
import json
from pprint import pprint
import numpy as np
from applymakeup import MakeupApplier


class MakeupPaletteGenerator:
    foundationColors = None
    concealerColors = None
    lipstickColors = None
    makeup_applier = MakeupApplier()

    def __init__(self):

        with open('json/foundation_shades.json') as json_file:
            data = json.load(json_file)
            self.foundationColors = data
        with open('json/concealer_shades.json') as json_file:
            data = json.load(json_file)
            self.concealerColors = data
        with open('json/lipstick_shades.json') as json_file:
            data = json.load(json_file)
            self.lipstickColors = data

    def HEXToRGB(self, hex):
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    def RGBToHEX(self, rgb):
        red = int(rgb[0])
        green = int(rgb[1])
        blue = int(rgb[2])
        hex_string = "{:02x}{:02x}{:02x}".format(red, green, blue)
        return hex_string

    def applyLipstick(self, lipstickHex="", lipstickCode=""):
        if lipstickHex:
            self.makeup_applier.applyLipstick(
                color=lipstickHex, imgpath="uploads/image.png", product=lipstickCode)

    def applyFoundation(self, foundationHex="", foundationCode=""):
        if foundationHex:
            self.makeup_applier.applyFoundation(
                color=foundationHex, imgpath="uploads/image.png", product=foundationCode)

    def getFoundationColor(self, suggestionNumber=3, skinColor=None):

        foundationSuggestion = []
        for foundationColor in self.foundationColors:
            self.applyFoundation(
                foundationHex=foundationColor["shadeHex"], foundationCode=foundationColor["shadeCode"])
            foundationSuggestion.append({"colorDetails": foundationColor,
                                         "distance": colour.delta_E(skinColor, self.HEXToRGB(foundationColor["shadeHex"]))})

        foundationSuggestion = sorted(
            foundationSuggestion, key=lambda d: d['distance'])

        return foundationSuggestion[0:suggestionNumber]

    def getConcealerColor(self, foundationColor, suggestionNumber=3, skinUndertone="Neutral", matchUndertone=False):
        foundationColorHEX = foundationColor["colorDetails"]["shadeHex"]
        foundationColorRGB = self.HEXToRGB(foundationColorHEX)

        # choosing the concealer based on the skin undertone
        skintoneConcealerSuggestion = []
        for concealerColor in self.concealerColors:
            concealerColor["distance"] = colour.delta_E(
                foundationColorRGB, self.HEXToRGB(concealerColor["concealerHex"]))
            if matchUndertone:
                if concealerColor["concealerUndertone"] == skinUndertone:
                    skintoneConcealerSuggestion.append(concealerColor)
            else:
                skintoneConcealerSuggestion.append(concealerColor)

        skintoneConcealerSuggestion = sorted(
            skintoneConcealerSuggestion, key=lambda d: d['distance'])

        darkConcealerSuggestion = []
        lightConcealerSuggestion = []
        # choosing the concealer a darker and lighter shade of the concealer
        warmShades = []
        coolShades = []
        neutralShades = []
        for concealerColor in self.concealerColors:
            if concealerColor["concealerUndertone"] == "Warm":
                warmShades.append(concealerColor)
            elif concealerColor["concealerUndertone"] == "Cool":
                coolShades.append(concealerColor)
            else:
                neutralShades.append(concealerColor)

        # sort shades based on concealer code
        warmShades = sorted(warmShades, key=lambda d: d['concealerCode'])
        coolShades = sorted(coolShades, key=lambda d: d['concealerCode'])
        neutralShades = sorted(neutralShades, key=lambda d: d['concealerCode'])

        for suggestedConcealer in skintoneConcealerSuggestion:
            if suggestedConcealer["concealerUndertone"] == "Warm":
                dark = self.getNeighbours(
                    warmShades, suggestedConcealer["concealerCode"])["dark"]
                light = self.getNeighbours(
                    warmShades, suggestedConcealer["concealerCode"])["light"]
            elif suggestedConcealer["concealerUndertone"] == "Cool":
                dark = self.getNeighbours(
                    coolShades, suggestedConcealer["concealerCode"])["dark"]
                light = self.getNeighbours(
                    coolShades, suggestedConcealer["concealerCode"])["light"]
            else:
                dark = self.getNeighbours(
                    neutralShades, suggestedConcealer["concealerCode"])["dark"]
                light = self.getNeighbours(
                    neutralShades, suggestedConcealer["concealerCode"])["light"]
            darkConcealerSuggestion.append(dark)
            lightConcealerSuggestion.append(light)

        return {"skinColor": skintoneConcealerSuggestion[0:suggestionNumber],
                "darkColor": darkConcealerSuggestion[0:suggestionNumber],
                "lightColor": lightConcealerSuggestion[0:suggestionNumber]}

    def getNeighbours(self, lst, id_val):
        lstid = [d['concealerCode'] for d in lst]
        index = lstid.index(id_val)
        if index == 0:
            return {"dark": lst[1], "light": None}
        elif index == len(lst) - 1:
            return {"light": lst[-2], "dark": None}
        else:
            return {"dark": lst[index + 1], "light": lst[index - 1]}

    def getLipstickColor(self, suggestionNumber=3, skinUndertone=None, foundationColor=None, matchUndertone=False):
        foundationColorHEX = foundationColor["colorDetails"]["shadeHex"]
        foundationColorRGB = self.HEXToRGB(foundationColorHEX)
        lipstickSuggestion = []
        for lipstickColor in self.lipstickColors:
            # pprint(lipstickColor)
            lipstickColor["distance"] = colour.delta_E(
                self.HEXToRGB(lipstickColor["lipstickHex"]), foundationColorRGB)
            if matchUndertone:
                if lipstickColor["lipstickUndertone"] == skinUndertone:
                    self.applyLipstick(
                        lipstickHex=lipstickColor["lipstickHex"], lipstickCode=lipstickColor["lipstickCode"])
                    lipstickSuggestion.append(lipstickColor)
            else:
                self.applyLipstick(
                    lipstickCode=lipstickColor["lipstickCode"], lipstickHex=lipstickColor["lipstickHex"])
                lipstickSuggestion.append(lipstickColor)
        mauveShades = []
        pinkShades = []
        redShades = []
        coralShades = []
        nudeShades = []
        for lipstickColor in lipstickSuggestion:
            if lipstickColor["lipstickType"] == "Mauve":
                mauveShades.append(lipstickColor)
            elif lipstickColor["lipstickType"] == "Pink":
                pinkShades.append(lipstickColor)
            elif lipstickColor["lipstickType"] == "Red":
                redShades.append(lipstickColor)
            elif lipstickColor["lipstickType"] == "Coral":
                coralShades.append(lipstickColor)
            else:
                nudeShades.append(lipstickColor)

        mauveShades = sorted(mauveShades, key=lambda d: d['distance'])
        pinkShades = sorted(pinkShades, key=lambda d: d['distance'])
        redShades = sorted(redShades, key=lambda d: d['distance'])
        coralShades = sorted(coralShades, key=lambda d: d['distance'])
        nudeShades = sorted(nudeShades, key=lambda d: d['distance'])

        return {"mauve": mauveShades[0:suggestionNumber], "pink": pinkShades[0:suggestionNumber],
                "red": redShades[0:suggestionNumber], "coral": coralShades[0:suggestionNumber],
                "nude": nudeShades[0:suggestionNumber]}


# conealearMatchesUndertone is a boolean value that determines if the concealer
# should match the skin undertone so if the skin undertone is warm,
# the concealer should be warm as well

# suggestionNumber is the number of suggestions that should be returned for each category of consealer and foundation


    def getMakeupColorPalette(self, dominantColor, suggestionNumber=3, concealorMatchesUndertone=True, lipstickMatchesUndertone=True):
        skinColorRGB = tuple(dominantColor[0]['color'])
        foundation = self.getFoundationColor(
            suggestionNumber, skinColorRGB)

        selectedFoundation = foundation[0]
        skinUndertone = selectedFoundation["colorDetails"]["shadeUndertone"]

        selectedConcealer = self.getConcealerColor(
            selectedFoundation, skinUndertone=skinUndertone, matchUndertone=concealorMatchesUndertone, suggestionNumber=suggestionNumber)
        selectedLipstick = self.getLipstickColor(
            skinUndertone=skinUndertone, matchUndertone=lipstickMatchesUndertone, foundationColor=selectedFoundation, suggestionNumber=suggestionNumber)

        return {"suggestedFoundation": foundation, "suggestedConcealer": selectedConcealer,
                "skinColorHex": self.RGBToHEX(skinColorRGB),
                "skinUndertone": skinUndertone,
                "suggestedLipstick": selectedLipstick}
