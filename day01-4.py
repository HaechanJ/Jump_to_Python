#문자열 인덱싱

filename = "DF_260923_SCAN.pdf"

company = filename[0:-16]
date = filename[-15:-9]
work = filename[-8:-4]
extension = filename[-3:]

print(company)
print(date)
print(work)
print(extension)