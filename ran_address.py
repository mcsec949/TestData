import random
import sys

def read_file(fName):

    nList = []

    try:
        f = open(fName,'r')
    except:
        print('error opening ',fName)
        sys.exit()
    names = f.readlines()
    names = [x.strip() for x in names]  #remove whitespace 

    for x in names:
        nList.append(x)

    f.close()
    return nList

def genRanAddr():
    # Generates a random address.
    streets = read_file("streetNames.txt")
    cities = read_file("cityNames.txt")
    zips = read_file("zipcodes.txt")
    stateList = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

    streetNum = str(random.randint(1,1500))
    street = random.choice(streets)
    city = random.choice(cities)
    tlstate = random.choice(stateList)
    zip = random.choice(zips)

    fullAddr = streetNum + ' ' + street + ', ' + city + ', ' + tlstate + " " + zip 
 

    return fullAddr


def main():
    form = 'd'
    m = 15
    fname = 'fullAddress.txt'
    adrfile = open(fname,'a') 

    if len(sys.argv) > 1:
        try:
            m = int(sys.argv[1])
        except:
            print("argument must be an integer\n")
            print("using default of 5\n")

    print(genRanAddr())
    


    for _ in range(m):
        addr = (genRanAddr())
        print(addr)
        adrfile.write(addr + '\n')
    
    adrfile.close()


if __name__ == '__main__':
	main()
