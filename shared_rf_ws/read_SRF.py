import re
import xlwt 
import sys
from xlwt import Workbook
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')
side = []
for h in range(1,6):
	with open(sys.argv[1]+"/layer"+str(h)+"/timeloop-mapper.stats.txt","r") as fi: 
		num = []
		i =-1
		j = 0
		w = 0
		k = 0
		p = 0
		s = 0
		m = 0
		g = 0
		r = 0
		q = 0
		l =0
		temp = 0
		for ln in fi:
			if ln.startswith("=== mac ==="):j = 1;w=1;
			
			if(w == 1 and ln.startswith("        Energy (total)")):
				side.append("mac");
				temp = re.findall(r"[-+]?\d*\.\d+|\d+", ln);num.append(temp);
				w = 0;

			if ln.startswith("=== output_activation_reg ==="):j = 1;p=1;
			
			if(p == 1 and ln.startswith("        Energy (total)")):
				side.append("out reg");
				temp = re.findall(r"[-+]?\d*\.\d+|\d+", ln);num.append(temp);
				p = 0;
			if ln.startswith("=== input_activation_reg ==="):j = 1;s=1;
			
			if(s == 1 and ln.startswith("        Energy (total)")):
				side.append("input reg");
				temp = re.findall(r"[-+]?\d*\.\d+|\d+", ln);num.append(temp);
				s = 0;
			if ln.startswith("=== weight_reg ==="):j = 1;m=1;
			
			if(m == 1 and ln.startswith("        Energy (total)")):
				side.append("wei reg");
				temp = re.findall(r"[-+]?\d*\.\d+|\d+", ln);num.append(temp);
				m = 0;
			if ln.startswith("=== pe_spad ==="):j = 1;l=1;
			if(l == 1 and ln.startswith("        Energy (total)")):
				side.append("pespad");
				temp = re.findall(r"[-+]?\d*\.\d+|\d+", ln);num.append(temp);
				l = 0;
			if ln.startswith("=== shared_glb ==="):j = 1;g=1;side.append("shared_glb");temp = 0

			if(g == 1 and ln.startswith("        Energy (total)")):
				k = k+1;
				
				if(k == 1):temp = float(re.findall(r"[-+]?\d*\.\d+|\d+", ln)[0]);print(temp)
				if(k == 2):temp = temp + float(re.findall(r"[-+]?\d*\.\d+|\d+", ln)[0]);print(temp)
				if(k == 3):temp = temp + float(re.findall(r"[-+]?\d*\.\d+|\d+", ln)[0]);num.append(temp);print(temp)
				
			if ln.startswith("=== DRAM ==="):j = 1;r=1;side.append("DRAM");temp = 0
			if(r == 1 and ln.startswith("        Energy (total)")):
				q = q+1;
				
				if(q == 1):temp = float(re.findall(r"[-+]?\d*\.\d+|\d+", ln)[0]);
				if(q == 2):temp = temp + float(re.findall(r"[-+]?\d*\.\d+|\d+", ln)[0]);
				if(q == 3):temp = temp + float(re.findall(r"[-+]?\d*\.\d+|\d+", ln)[0]);num.append(temp);
				


		i=-1;j=0;w=0;k=0;q=0;r=0;g=0


	for i in range(len(num)):
		sheet1.write(i+1, h, num[i]) 
				
for i in range(0,7):
	sheet1.write(i+1, 0, side[i])
wb.save("file_{}_shared_ws.xls".format(str(sys.argv[1])))
