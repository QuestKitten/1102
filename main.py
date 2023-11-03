#read the numbers
#sort the numbers
#missing numnbers
#write numbers in sorted_numbers

f = open("three_digit_numbers.txt")
sample = f.read()
cols = sample.split()
num_list = []
for col in cols:
    num = int(col)
    num_list.append(num)

start = min(num_list)

#open txt file for sorted numbers
sorted_num = open('sorted_numbers.txt', 'w')

for count in range(start, max(num_list)):
    #print(count)
    if count in num_list:
        sorted_num.write(f"{count}\n")
#close the file
sorted_num.close()


#open the txt file for missing numbers
missing_num = open('missing_numbers.txt', 'w')

for count in range(start, max(num_list)):
    if count not in num_list:
        print(f"{count} is missing")
        missing_num.write(f"{count}\n")
#close missing_num file
missing_num.close()
        



























