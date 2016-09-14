import csv

def run():
	with open('C:/Users/Peter/Websites/CUAPB/police_archive/CSV/tcc4j_full.csv', 'rb') as f:
		with open('C:/Users/Peter/Websites/CUAPB/police_archive/CSV/riseup_output.txt', 'r+') as g:
			for row in csv.reader(f):
				g.write(row[28])
				g.write(' ')
				g.write(row[0])				
				g.write('\n')
		