#Mudasir haq,1834539
import csv #  this moduale is for reading the csv files
import datetime # for sorting by date
item_List  = {} # dict with the info
rows = 0 # this variable will let you go through all the rows
var = 0 #used in the for loop 
ids = [] # list with all the id names
dates = []
class items: #class for the items
	def __init__(self):
		item_id = []
		brand  = [] 
		type = [] 
		price = [] 
		date = []
		dam = []	
def  fullinventory(): #function for the first csv file
	
	with open('PriceList.csv') as id:
		csv_reader = csv.reader(id,delimiter=',')
		
		for row in csv_reader:
			ids.insert(1,(row[0]))#add the id from every row
			
			
			
		 
		ids.sort() #sort the id list
		cnt = 0 #iterator
		items_n = len(ids)	#number of items
		fullinventoryclss = items() #create a class for the items
		fullinventoryclss.item_id = [] #create a list for the id
		fullinventoryclss.brand = [] #create a list for the brand
		fullinventoryclss.type = [] #create a list for the type
		fullinventoryclss.price = [] #create a list for the price
		fullinventoryclss.date = [] #create a list for the date
		fullinventoryclss.dam = [] #create a list for the damage

		with open('PriceList.csv') as price: #open the csv file
			csv_reader = csv.reader(price,delimiter=',') #read the csv file
			for row in csv_reader: 
				while cnt < items_n: #while the iterator is less than the number of items
					if ids[cnt] != row[0]: #if the id is not equal to the id in the row
						cnt = cnt+ 1 #increment the iterator
					else: #if the id is equal to the id in the row
						item_List[cnt] = {cnt:{"price":row[1],"id":row[0]},} 	#add the id and price to the dictionary
						break #break the loop
				cnt = 0 #reset the iterator
			cnt = 0 #reset the iterator
		with open('ServiceDatesList.csv') as datescsv: #open the csv file
				csv_reader = csv.reader(datescsv,delimiter=',') #read the csv file
				for row in csv_reader: #for every row in the csv file
					while cnt<items_n: #while the iterator is less than the number of items
						if row[0] != ids[cnt]: #if the id is not equal to the id in the row
							cnt = cnt + 1 #increment the iterator
						else: #if the id is equal to the id in the row
							item_List[cnt][cnt]["date"] = row[1] #add the date to the dictionary
							
							break #break the loop
					cnt = 0 #reset the iterator
				cnt = 0
		with open('ManufacturerList.csv') as brandcsv: #open the csv file
			csv_reader = csv.reader(brandcsv,delimiter=',') #read the csv file
			for row in csv_reader:
				while cnt<=items_n:
					if row[0] != ids[cnt]:
						cnt = cnt + 1
					else:
						item_List[cnt][cnt]["brand"] = row[1]
						item_List[cnt][cnt]["type"] = row[2]
						if(row[3] == 'damaged'):
							item_List[cnt][cnt]["dam"] = True
						else:
							item_List[cnt][cnt]["dam"] = False
						break
				cnt = 0
			cnt = 0
		while cnt < items_n: #while the iterator is less than the number of items
			fullinventoryclss.item_id.insert(1,item_List[cnt][cnt]["id"]) #add the id to the list
			fullinventoryclss.brand.insert(1,item_List[cnt][cnt]["brand"]) #add the brand to the list
			fullinventoryclss.type.insert(1,item_List[cnt][cnt]["type"]) #add the type to the list
			fullinventoryclss.price.insert(1,item_List[cnt][cnt]["price"]) #add the price to the list
			fullinventoryclss.date.insert(1,item_List[cnt][cnt]["date"]) #add the date to the list
			fullinventoryclss.dam.insert(1,item_List[cnt][cnt]["dam"]) #add the damage to the list

			cnt = cnt + 1 #increment the iterator
		cnt = 0 #reset the iterator
		brands = [fullinventoryclss.brand] #create a list for the brand
		brands.sort() #sort the list
		
		
		#ite = 0 
		#print(fullinventoryclss.item_id)
		#print(fullinventoryclss.brand)
		#print(brands)
		#for iter in brands:
			#cnt = 0
			
			#while cnt <= items_n:
				
				#if item_List[cnt][cnt]["brand"] != iter:
					#cnt = cnt + 1
					#break
					
					
				#else:
					
					#fullinventoryclss.item_id[ite] = item_List[cnt][cnt]["id"]
					#	fullinventoryclss.brand[ite] = item_List[cnt][cnt]["brand"]
					#fullinventoryclss.type[ite] = item_List[cnt][cnt]["type"]
					#fullinventoryclss.price[ite] = item_List[cnt][cnt]["price"]
					#fullinventoryclss.date[ite] = item_List[cnt][cnt]["date"]
					#fullinventoryclss.dam[ite] = item_List[cnt][cnt]["dam"]
					#print("else")
					#cnt = 0
					#break
					
					
					
				
    	
		print(fullinventoryclss.item_id)
		print(fullinventoryclss.brand)
		print(fullinventoryclss.type)
		print(fullinventoryclss.price)
		print(fullinventoryclss.date)
		print(fullinventoryclss.dam)
		print(fullinventoryclss.brand)
		#write full inventory to a csv file
		cnt = 0
		with open('FullInventory.csv', mode='w') as fullinv:
			csv_writer = csv.writer(fullinv,delimiter=',') #write the csv file
			while cnt < items_n: #while the iterator is less than the number of items
				csv_writer.writerow([fullinventoryclss.item_id[cnt],fullinventoryclss.brand[cnt],fullinventoryclss.type[cnt],fullinventoryclss.price[cnt],fullinventoryclss.date[cnt],fullinventoryclss.dam[cnt]]) #write the row to the csv file
				cnt = cnt + 1
			
			

		
			
	

		
				

							


		
		
		
			



					  
					
					
						
					
					
					
					

						



			





			
fullinventory()


		


		
			







		
		
		







