#문자열 인덱싱

text = "DESIGNFOLDER"

print(text[0])
print(text[1])
print(text[2])

company = "DF"
date = "260923"
work = "SCAN"

filename =f"{company}_{date}_{work}.pdf"

print(filename[0])
print(filename[1])
print(filename[3])
print(filename[-1])

company = filename[0:2]
date = filename[3:9]
work = filename[10:14]
extention = filename[15:19]

print(company)
print(date)
print(work)
print(extention)