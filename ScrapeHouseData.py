from bs4 import BeautifulSoup
import pandas as pd
plotsDetail = []
for i in range(1,7):
    with open(f"PlotPage{i}.htm",'r',encoding='utf-8') as dataFile:
        soup = BeautifulSoup(dataFile,"html.parser")
        # print(soup.find_all("div",class_="MuiBox-root mui-style-zf9afz"))
        plotDetailBoxes = soup.find_all("div",class_="MuiBox-root mui-style-zf9afz")
        # print(len(plotDetailBox))
        for plotBox in plotDetailBoxes:
            plotsDetail.append(plotBox)
# print(len(plotsDetail))            
# print(plotsDetail)
plotLocations = []
plotAreas = []
plotPrices = []
for plot in plotsDetail:
    location = plot.find("h5",class_="MuiTypography-root MuiTypography-subtitle2New mui-style-3bzwbl")
    plotLocations.append(location.text)
    area = plot.find("div",class_="MuiTypography-root MuiTypography-body2New mui-style-1548769")
    plotAreas.append(area.text)
    price = plot.find("div",class_="MuiTypography-root MuiTypography-h4New mui-style-gz23my")
    plotPrices.append(price.text)
    # print(price.text)
    # print(area.text)
    # print(area.text)
# print(plotLocations)
# print(len(plotLocations))
# print(plotAreas)    
# print(len(plotAreas))
# print(plotPrices)
# print(len(plotPrices))
plotsData = pd.DataFrame({
    "Total Area of Plot":plotAreas,
    "Total Price of Plot":plotPrices,
    "Location Of Plot":plotLocations
})
print(plotsData)
print(plotsData.describe())
plotsData.to_csv("ResidentialPlotsInMultan.csv",index=False)