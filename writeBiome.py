# coding: UTF-8
import csv

height = [0.1,0.1,-0.9,-1.9,-2.9,-3.0,-4.9,-5.9,-6.9,-7.9,-8.9,0,0,1,2,3,4,5,6,7,8,9]
suffix = ["n0","n0","n1","n2","n3","n4","n5","n6","n7","n8","n9","0","0","1","2","3","4","5","6","7","8","9"]
flag = [0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]

biomeID = 256
strCustomBiomes = ""

colorFile = open("color.csv", "r")
biomeFile = open("biome.txt", "r")

colorReader = csv.reader(colorFile, lineterminator="\n")

for biome in biomeFile:
	print biome.strip()
	colorRow = next(colorReader)
	for index, color in enumerate(colorRow):
		if flag[index]:
			print "height: " + str(height[index]) + ", color: " + color
			writeFile = open("target/"+biome.strip()+" "+suffix[index]+".bc","w")
			writeFile.write("BiomeExtends: "+biome.strip()+"\n")
			writeFile.write("ResourceInheritance: true\n")
			writeFile.write("ReplaceToBiomeName: "+biome.strip()+"\n")
			writeFile.write("BiomeColor: "+color+"\n")
			writeFile.write("BiomeHeight: "+str(height[index])+"\n")
			writeFile.write("SmoothRadius: 5\n")
			writeFile.close()
			strCustomBiomes += biome.strip()+" "+suffix[index]+":"+str(biomeID)+","
			biomeID += 1


colorFile.close()
biomeFile.close()

print strCustomBiomes
