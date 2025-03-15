import pandas as pd
plotsData = pd.read_csv("ResidentialPlotsInMultan.csv")
# print(plotsData["Total Area of Plot"].tolist())
areas = plotsData["Total Area of Plot"].tolist()
# 1 marla = 272.25 square feet
# 1 Kanal = 20 marlas
# 1 Kanal = 20 * 272.25 = 5445 square feet
# print(areas)
# Converting areas to square feet
areaInMarlas = []
areaInKanals = []
areaInSqfeet = []
for index,area in enumerate(areas):
    area = area.split()
    area[0] = round(float(area[0]),3)
    if area[1] == 'marla':
        areaInMarlas.append(area[0])
        areaInKanals.append(area[0]/20.0)
        areaInSqfeet.append(area[0]*272.25)
    elif area[1] == 'kanal':
        areaInKanals.append(area[0])
        areaInMarlas.append(area[0]*20.0)
        areaInSqfeet.append(area[0]*5445.0)
    elif area[1] == 'sqft':
        areaInMarlas.append(area[0]/272.25)
        areaInKanals.append(area[0]/5445.0)
        areaInSqfeet.append(area[0])
# converting price into lacs and crores
plotsPrices = plotsData["Total Price of Plot"].tolist()
# print(plotsPrices)
priceInLacs = []
priceInCrores = []
for index,price in enumerate(plotsPrices):
    price = price.split()
    price[0] = round(float(price[0]),3)
    if price[1] == 'Lac':
        priceInLacs.append(price[0])
        priceInCrores.append(round(price[0]/100,3))
    elif price[1] == 'Crore':
        priceInLacs.append(round(price[0]*100,3))
        priceInCrores.append(price[0])
# print(len(priceInLacs))
# print(len(priceInCrores))                        
# print(priceInLacs)
# print(priceInCrores)
plotsLocation = plotsData["Location Of Plot"].tolist()
plotsData = pd.DataFrame({
    "Area (Marlas)":areaInMarlas,
    "Area (Kanals)":areaInKanals,
    "Area (Sq-feet)":areaInSqfeet,
    "Price (Lacs)":priceInLacs,
    "Price (Crores)":priceInCrores,
    "Location": plotsLocation
})
print(plotsData)
plotsData.to_csv("ResidentialPlotsDataSetUpdated.csv",index=False)