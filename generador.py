'''
    @author: Adrian Zayas Viveros
    @version: 1.0.0
    @date: 07/05/24 [MM:DD:YY]
'''

import qrcode
import pandas as pd
import os

# Define the file path
filePath = './csvs/Catalog_v2.csv'

# Extract only the file name without the path or extension.
fileName = os.path.splitext(os.path.basename(filePath))[0]
# extension = os.path.splitext(os.path.basename(filePath))[1]


# reate the path where the generated QR codes will be saved. The immediate
# containing folder will be named after the document from which the data 
# is being extracted.
folderQR = f'img/{fileName}'

# Create the folder at the path defined in the variable folderQR.
if not os.path.exists(folderQR):
    os.makedirs(folderQR)

# # Read the CSV file using pandas.
data = pd.read_csv(filePath, encoding='utf-8')
columns = data.columns

for i in range(len(data)):
    text = ''
    print(f'Record: {i}')
    for j in range(len(columns)):
        text += columns[j] + ': ' + str(data.iloc[i,j]) + '\n'
    print(text)
    img = qrcode.make(text)
    img.save(f"{folderQR}/Qr{i}.png")
    text=''
    print('--------------------------------------------')

print("Number of records: " , len(data))
print("Number of columns: " , len(columns))

# text= f'Este programa te permite generar códigos QR \nDescarga este proyecto desde https://github.com/AdrianZayas/QRGenerator.git'
# text= f'This program allows you to generate QR codes \nDownload this project from https://github.com/AdrianZayas/QRGenerator.git'
# img = qrcode.make(text)
# img.save(f"img/Bienvenido.png")
# img.save(f"img/Welcome.png")