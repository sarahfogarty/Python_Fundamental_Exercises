
# part 1 -
def draw_stars(x):
    i = 0
    for element in x:
        print "*" * x[i]
        i = i + 1


x = [2, 5, 4, 9, 3]

draw_stars(x)

#  part 2

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars2(*args):
    for i in x:
        output = ''
        if type(i) is int:
            #for i in range(i):
            output += i * "*"
        elif type(i) is str:
            first_letter = i[0].lower()
            for i in range(len(i)):
                output += first_letter
        print output


draw_stars2(x)
