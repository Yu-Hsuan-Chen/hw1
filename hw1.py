# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================
# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106030029.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================
# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

target_id = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
result = []
for id in target_id:
   target_data = list(filter(lambda item: item['station_id'] == id, data))
   target_data = list(filter(lambda item: item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000', target_data))
   sum = 0.0
   if bool(target_data):
      for x in target_data:
         sum += float(x['HUMD'])*1000
      sum /= 1000
   else:
      sum = 'None'
   result.append([id, sum])

# Retrive ten data points from the beginning.
# target_data = data[:10]
#=======================================
# Part. 4
#=======================================
# Print result
print(result)
#========================================