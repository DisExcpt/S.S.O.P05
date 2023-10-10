from archives import *
test = folders()

root = test.selectRoot()
# print(root)
test.selectElements(root)
archivos = test.getArchives()
print(archivos)

