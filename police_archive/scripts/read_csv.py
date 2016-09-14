import csv
from police_archive.models import Officer, Incident, Details


def run():
	with open('C:/Users/Peter/Websites/CUAPB/police_archive/scripts/cuapb_html.csv', 'rb') as f:
		with open('C:/Users/Peter/Websites/CUAPB/police_archive/scripts/complaints.csv', 'r+') as g:

			

	#Defining a function to find all instances of a substring
			def findall(sub, string):
			    # """
			    # >>> text = "Allowed Hello Hollow"
			    # >>> tuple(findall('ll', text))
			    # (1, 10, 16)
			    # """
			    index = 0 - len(sub)
			    try:
			        while True:
			            index = string.index(sub, index + len(sub))
			            yield index
			    except ValueError:
	        		pass


			CRA_dict={}
			id_count=1903
			for row in csv.reader(f):
				post_content=row[0]


				cra_index= post_content.find("Civilian Review Authority")
				ia_index=post_content.find("Internal Affairs")
				opcr_index = post_content.find("Police Conduct Review")
				


				if opcr_index<>-1:
					office_section=post_content[opcr_index:]
				

					data_list=[]

					tr_tuple=tuple(findall('<tr>',office_section))
					endtr_tuple=tuple(findall('</tr>',office_section))



					if (len(tr_tuple)==len(endtr_tuple) and tr_tuple <> ()):
						tr_count=1
						while (tr_count<len(tr_tuple)):

							tr_start = tr_tuple[tr_count]
							tr_end = endtr_tuple[tr_count]
							tr_section = office_section[tr_start:tr_end]


							td_tuple=tuple(findall('<td>', tr_section))
							endtd_tuple=tuple(findall('</td>', tr_section))



							
							data_list.append([])
							td_count=0
							while(td_count)<len(td_tuple):
								
								td_start = td_tuple[td_count]
								td_end = endtd_tuple[td_count]
							
								
								
								td_section = tr_section[td_start:td_end]
								data = td_section
								cleaned_data= data.replace('\r\n\t\t\t\t','').replace('\r\n\t\t\t','').replace('<td>','').replace('&nbsp;','')
								
								data_list[tr_count-1].append(cleaned_data)

								
								td_count=td_count+1

							tr_count=tr_count+1
																														
					


					o=Officer.objects.get(id=id_count)
					print o
					print id_count

					for list in data_list:

						if len(list)==4:
							print list
							i=Incident.objects.create(case_number=list[0], office='OPCR')							
							Details.objects.create(officer=o,incident=i, allegation=list[1], finding=list[2], action=list[3])
					id_count=id_count+1
					print data_list


				
				
				

			


				
			#endfor
