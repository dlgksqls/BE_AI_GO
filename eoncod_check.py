import chardet
import pandas as pd

rawdata = open(r"C:\Users\horai\Desktop\BE_AI_GO\api\202309_xlsx.xlsx", "rb").read()
result = chardet.detect(rawdata)
char_enc = result["encoding"]

print(char_enc)
