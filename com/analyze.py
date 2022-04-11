import pandas as pd

df = pd.read_json("./products1.json")

writer = pd.ExcelWriter("products1.xlsx")
df.to_excel(writer, "sheet1")
writer.save()


print(df.count())
