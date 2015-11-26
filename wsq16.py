cars_data = open("93cars.dat.txt")
count = 0
tot_price = 0
tot_city = 0
tot_high = 0

for line in cars_data:
    if(count % 2 == 0):
        sin_price = float(line[42:46])
        tot_price = tot_price + sin_price
        sin_city = float(line[52:54])
        tot_city = tot_city + sin_city
        sin_high = float(line[55:57])
        tot_high = tot_high + sin_high
    count = count + 1
    x = count/2
    midrange_price = tot_price/x
    mileage_city = tot_city/x
    mileage_highway = tot_high/x

print("The average gas mileage in city is",mileage_city)
print("The average gas mileage on highway is",mileage_highway)
print("The average midrange price is",midrange_price)
