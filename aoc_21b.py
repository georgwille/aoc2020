fin = open('input_21.txt')

food = [] # tuple of sets of ingredients and allegens

foods_with_allergen = {} # list of food indices for each allergen
foods_with_ingredient = {} # list of food indices for each ingredient


for ln,line in enumerate(fin):
    allergens = line[line.index('(contains ')+10:line.index(')')].split(', ')
    ingredients = line[:line.index('(')-1].split(' ')
    food.append((set(ingredients),set(allergens)))
    for allergen in allergens:
        try:
            foods_with_allergen[allergen].append(ln)
        except KeyError:
            foods_with_allergen[allergen] = [ln]
    for ingredient in ingredients:
        try:
            foods_with_ingredient[ingredient].append(ln)
        except KeyError:
            foods_with_ingredient[ingredient] = [ln]

fin.close()

#print(food)
#print(foods_with_ingredient)
#print(foods_with_allergen)

# filtering allergen candidates

allergen_could_be = {}

for allergen in foods_with_allergen:
    foods = foods_with_allergen[allergen]
    print(allergen,'in',foods)
    common_ingr = set(food[foods[0]][0])
    for entry in foods[1:]:
        common_ingr = common_ingr.intersection(food[entry][0])
    # print(allergen,common_ingr)
    allergen_could_be[allergen] = common_ingr

print(allergen_could_be)

# removing ambiguities

finished = False

while not finished:
    finished = True
    for allergen in allergen_could_be:
        candidates = allergen_could_be[allergen]
        if len(candidates) == 1:
            for allergen_check in allergen_could_be:
                if allergen_check == allergen:
                    continue
                else:
                    allergen_could_be[allergen_check] = allergen_could_be[allergen_check].difference(candidates)
        else:
            finished = False

print(allergen_could_be)

evil_ingr = set()

for entry in allergen_could_be:
    evil_ingr = evil_ingr.union(allergen_could_be[entry])

print(evil_ingr)

goodcount = 0

for entry in food:
    for ingr in entry[0]:
        if ingr not in evil_ingr:
            goodcount += 1

print("Occurences of good stuff:",goodcount)

evillist = []

for entry in allergen_could_be:
    evillist.append([entry,list(allergen_could_be[entry])[0]])

evillist.sort(key=lambda entry: entry[0])
print("Canonical evil stuff:",[entry[1] for entry in evillist])
