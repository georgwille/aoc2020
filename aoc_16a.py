fin = open('input_16.txt')

all = fin.readlines()
fin.close()
ntickets = all[25:]

fields = {
'departure location': [49,258,268,960],
'departure station': [37,117,128,968],
'departure platform': [31,70,78,974],
'departure track': [26,234,247,952],
'departure date': [49,625,635,969],
'departure time': [26,777,799,974],
'arrival location': [49,735,757,971],
'arrival station': [28,381,399,970],
'arrival platform': [49,77,95,957],
'arrival track': [29,467,477,950],
'class': [40,218,234,967],
'duration': [45,900,911,970],
'price': [42,442,452,966],
'route': [45,104,112,953],
'row': [49,877,884,957],
'seat': [40,168,184,953],
'train': [43,913,920,949],
'type': [43,292,315,955],
'wagon': [48,547,558,954],
'zone': [40,929,935,954],
}


def is_in_any_field(number):
    # print(number)
    for field in fields:
        check = fields[field]
        if check[0]<=number<=check[1] or check[2]<=number<=check[3]:
            return True
    return False

errorsum = 0

for ticket in ntickets:
    numbers = ticket.strip().split(',')
    for number in numbers:
        if not is_in_any_field(int(number)):
            errorsum += int(number)

print("Error sum:", errorsum)