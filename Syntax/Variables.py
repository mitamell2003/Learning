# X = 13
# Y = "Gioi"
# print(X)
# print(Y)
# X = 5
# X = "NĂM"
# print(X)
# X = str(3)
# Y = int(3)
# Z = float(3)
# print(X)
# print(Y)
# print(Z)
# X = 5
# Y = 'hello'
# Z = 3.5
# print(type(X))
# print(type(Y))
# print(type(Z))
# X, Y, Z = "Chó", "Mèo", "Chuột"
# print(X)
# print(Y)
# print(Z)
# Trái_Cây = ["Cam", "Mận", "Xoài"]
# X, Y, Z = Trái_Cây
# print(X)
# print(Y)
# print(Z)
# X, Y, Z = 'Tên', 'Tui', 'là'
# print(X + Y + Z)
# print(X, Y, Z)
# X, Y, Z = 'Tuổi', 15, 10
# print(X, Y, Z)
# X = 'Tiên'
# def tentien():
#     print('Tên là ' + X)
# tentien()    
# X = 'Cat'
# def animal():
#     X = 'Động vật ăn thịt'
#     print('Mèo là ' + X)
# animal()
# print(X + ' is an animal')
# X = 'Apple'
# def name():
#     global X
#     X = 'Banana'
# name()
# print('Chuối' + X)
# import pandas as pd
# a = [1, 2, 3]
# myvar = pd.Series(a)
# print(myvar)
# import pandas as pd
# a = [1, 2, 3]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)
# import pandas as pd
# calo = {"day 1": 1200, "day 2": 1300, "day 3": 1200}
# myvar = pd.Series(calo)
# print(myvar)
# import pandas as pd
# calo = {"day 1": 1200, "day 2": 1300, "day 3": 1200}
# myvar = pd.Series(calo, index = ["day 1", "day 2"])
# print(myvar)
# import pandas as pd
# data = {
# "calo": [1200,  1300,  1200],
# "duration": [50, 49, 45] 
# }
# myvar = pd.DataFrame(data)
# print(myvar)
# import pandas as pd
# data = {
# "calo": [1200,  1300,  1200],
# "duration": [50, 49, 45] 
# }
# df = pd.DataFrame(data)
# print(df.loc[0])
# import pandas as pd
# data = {
# "calo": [1200,  1300,  1200],
# "duration": [50, 49, 45] 
# }
# df = pd.DataFrame(data)
# print(df.loc[[0, 1]])
# import pandas as pd
# data = {
# "calo": [1200,  1300,  1200],
# "duration": [50, 49, 45] 
# }
# df = pd.DataFrame(data, index = ["day 1", "day 2", "day 3"])
# print(df)
import pandas as pd
data = {
"calo": [1200,  1300,  1200],
"duration": [50, 49, 45] 
}
df = pd.DataFrame(data, index = ["day 1", "day 2", "day 3"])
print(df.loc["day 1"])
