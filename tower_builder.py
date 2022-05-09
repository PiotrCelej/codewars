

def tower_builder(n_floors) :
    if n_floors <=0 : return []

    #count number of stars on each floor
    stars = [1]
    for i in range(n_floors-1) :
        stars.append(stars[i]+2)

    #max length of a floor is in the last element
    max_stars = stars[len(stars)-1]
    
    result = []
    for i in range(n_floors) :
        spaces = int((max_stars-stars[i])/2)
        row_spaces = ''.join(' ' for j in range(spaces))
        row_stars = ''.join('*' for k in range(stars[i]))
        row = row_spaces+row_stars+row_spaces
        result.append(row)

    return result

    
print(tower_builder(3))