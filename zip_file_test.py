import zipfile
zf = zipfile.ZipFile('hello.zip',mode='w')
try:
    zf.write('company.csv')
    zf.write('CSV.csv')

finally:
    zf.close()
    print('zip file is ready')