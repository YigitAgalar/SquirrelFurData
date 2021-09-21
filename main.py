import collections

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = data["Primary Fur Color"].to_list()
gray = []
cinnamon = []
black = []

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])



fur_dict = collections.defaultdict()
fur_dict["Fur Color"]=["gray", "cinnamon", "black"]
fur_dict["Count"] =  [gray, cinnamon, black]

fur_dict["Fur Color"].append("pembe")
fur_dict["Count"].append(8)
data_dict = pandas.DataFrame(fur_dict)
data_dict.to_csv("fur_data.csv")



