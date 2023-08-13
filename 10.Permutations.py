def generatePermutations(arr):
    if len(arr)==0:
        return [[]]
    all_permutations=[] 
    for i in range(len(arr)):
        first_el=arr[i]
        rem_el=arr[:i]+arr[i+1:]
        sub_permutations=generatePermutations(rem_el)
        for perm in sub_permutations:
            all_permutations.append([first_el]+perm)
    return all_permutations 

# def generate_permutations(arr):
    if len(arr) == 0:
        return [[]]

    all_permutations = []
    for i in range(len(arr)):
        first_elem = arr[i]
        remaining_elems = arr[:i] + arr[i+1:]

        sub_permutations = generate_permutations(remaining_elems)
        for perm in sub_permutations:
            all_permutations.append([first_elem] + perm)

    return all_permutations






letters=[1,2]
output=generatePermutations(letters)
print(output)