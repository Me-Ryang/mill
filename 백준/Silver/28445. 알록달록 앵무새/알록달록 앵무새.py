male_b, male_t = input().split()
female_b, female_t = input().split()

color = set([male_b, male_t, female_b, female_t])
color = list(color)
color.sort()

for r in color:
    for c in color:
        print(r, c)