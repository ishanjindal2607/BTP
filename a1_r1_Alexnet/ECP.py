import re
import xlwt 
import sys
from xlwt import Workbook
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')
side = []
for h in range(1,5):
	with open(sys.argv[1]+"/layer"+str(h)+"/timeloop-mapper.stats.txt","r") as fi: 
		num = []
		i =-1
		j = 0
		w = 0
		k = 0
		for ln in fi:
			if ln.startswith("Summary"):
				i = 0
				num.append("");num.append("STATS  " + "layer"+ str(h));
			if(i>=0 and i<5):
				i =i+1;
				if(i>2):
					side.append(ln.split()[0])
					temp = re.findall(r"[-+]?\d*\.\d+|\d+", ln)
					num.append(temp)
			if ln.startswith("=== DRAM ==="):j = 1;w=1;
			if(ln.startswith("    Cycles") and j == 1):
				num.append("DRAM  "+ "layer"+ str(h));num.append("");side.append("");
				side.append("");side.append("Cycles");
				temp = re.findall(r"[-+]?\d*\.\d+|\d+", ln);num.append(temp)
				j = 0
			if(w == 1 and ln.startswith("        Energy (total)")):
				k = k+1;
				if(k == 1):side.append("WEIGHTS ENERGY");
				if(k == 2):side.append("INPUTS ENERGY");
				if(k == 3):side.append("OUTPUTS ENERGY");
				temp = re.findall(r"[-+]?\d*\.\d+|\d+", ln);num.append(temp);
			if(w == 1 and ln.startswith("Networks")): 
				w = 0;side.append("");side.append("");
		i=-1;j=0;w=0;k=0;


	for i in range(len(num)):
		sheet1.write(i+1, h, num[i]) 
				
for i in range(0,13):
	sheet1.write(i+1, 0, side[i])
wb.save('ECP_{}.xls'.format(sys.argv[1]))
