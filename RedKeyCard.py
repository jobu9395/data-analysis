#Assumptions:
# -You are able to hit the room during the raid and make it out of the raid with all of the loot from that room
# -Does not account for hitting multiple rooms.
# - Assumes you are making an average haul outside of the room of 400,000 roubles
# - Assumes you are hitting the analyzed room every time you enter Labs, not necessarily others


class KeyCardBreakEven:
    def __init__(self, Color, SurvivalRate, RunCount, AverageInRoomHaul, FleaMarket, KeyCardCost, KitCost):
        self.Color = Color
        self.SurvivalRate = SurvivalRate
        self.RunCount = RunCount
        self.AverageInRoomHaul = AverageInRoomHaul
        self.FleaMarket = FleaMarket
        self.KeyCardCost = KeyCardCost
        self.KitCost = KitCost


    def isKeyCardWorthIt(self):
        AverageHaul = 400_000
        TotalHaul = AverageHaul + self.AverageInRoomHaul
        revenue = (self.SurvivalRate * self.RunCount * TotalHaul)
        cost = (self.KeyCardCost * self.RunCount) + (self.KitCost * (1 - self.SurvivalRate) * self.RunCount)
        Profit = revenue - cost
        print(f"This model follows the following assumptions: Survival Rate: {self.SurvivalRate}, Run Count: {self.RunCount}, Lab Key Card Cost: {self.FleaMarket}, Average haul of loot outside of this room: " + str(
                AverageHaul) + ".")
        if Profit > self.FleaMarket:
            print(f"Your revenue would be " + str(revenue) + " roubles, which is more than the key cost of " + str(self.FleaMarket) + " roubles.")
            print(f"Your net profit would be " + str(Profit - self.FleaMarket) + " roubles")
            print(f"The {self.Color} key card is worth it!\n")

        else:
            print(f"Your revenue would only be " + str(revenue) + " roubles, which is less than the key cost of " + str(self.FleaMarket) + " roubles.")
            print(f"Your net profit would be " + str(Profit - self.FleaMarket) + " roubles")
            print(f"The {self.Color} key card is not worth it.  Buy a sweet kit instead!\n")


SurvivalRate = 0.5
RunCount = 150
LabKeyCard = 155_000
KitCost = 100000

# optmized parameters
# SurvivalRate = 0.65
# RunCount = 5000
# LabKeyCard = 155_000
# KitCost = 570_000

RedKeyCard = KeyCardBreakEven('Red', SurvivalRate, RunCount, 400_000, 28_900_000, LabKeyCard, KitCost)
RedKeyCard.isKeyCardWorthIt()

BlueKeyCard = KeyCardBreakEven('Blue', SurvivalRate, RunCount, 150_000, 5_000_000, LabKeyCard, KitCost)
BlueKeyCard.isKeyCardWorthIt()

VioletKeyCard = KeyCardBreakEven('Violet', SurvivalRate, RunCount, 150_000, 7_900_000, LabKeyCard, KitCost)
VioletKeyCard.isKeyCardWorthIt()

GreenKeyCard = KeyCardBreakEven('Green', SurvivalRate, RunCount, 200_000, 1_500_000, LabKeyCard, KitCost)
GreenKeyCard.isKeyCardWorthIt()

BlackKeyCard = KeyCardBreakEven('Black', SurvivalRate, RunCount, 75_000, 500_000, LabKeyCard, KitCost)
BlackKeyCard.isKeyCardWorthIt()





