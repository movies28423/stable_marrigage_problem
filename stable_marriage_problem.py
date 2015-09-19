def stabalize_pairs(upper_dict, lower_dict):
    open_upper = list(upper_dict.keys())
    open_lower = list(lower_dict.keys())
    pairs = {}
    while len(open_upper) > 0:
        new_upper = open_upper.pop()
        best_lower = upper_dict[new_upper][0]
        if (best_lower in pairs.keys()) == False:
            pairs.update({best_lower:(new_upper, best_lower)})
        elif lower_dict[best_lower].index(pairs[best_lower][0]) > lower_dict[best_lower].index(new_upper):
            open_upper.append(pairs[best_lower][0])
            pairs[best_lower] = (new_upper, best_lower)
        else:
           upper_dict[new_upper] = upper_dict[new_upper][1:]
           open_upper.append(new_upper)
    return pairs

upper_list = ["A, b, d, g, h, c, j, a, f, i, e",
			  "B, f, b, i, g, a, j, h, e, c, d",
			  "C, b, i, j, g, h, d, e, f, c, a",
			  "D, f, a, e, i, c, j, b, g, d, h",
		  	  "E, f, d, a, e, i, b, c, g, j, h",
		  	  "F, d, f, a, c, j, e, i, b, g, h",
		      "G, e, g, c, b, f, d, a, i, j, h",
		      "H, f, i, b, c, e, a, h, g, d, j",
			  "I, i, a, j, f, c, e, b, g, h, d",
			  "J, h, f, c, e, b, a, j, g, d, i"]


lower_list = ["a, J, C, E, I, B, F, D, G, A, H",
		      "b, I, H, J, C, D, A, E, B, G, F",
		  	  "c, C, B, I, F, H, A, D, J, G, E",
		  	  "d, F, G, J, D, C, E, I, H, B, A",
			  "e, D, G, J, C, A, H, I, E, B, F",
			  "f, E, H, C, J, B, F, D, A, G, I",
			  "g, J, F, G, E, I, A, H, B, D, C",
			  "h, E, C, B, H, I, A, G, D, F, J",
			  "i, J, A, F, G, E, D, H, B, I, C",
			  "j, E, A, B, C, J, I, G, D, H, F"]

upper_dict = {}
lower_dict = {}

for x in upper_list:
    key = x[0]
    value = x[1:].split()
    value = [y[0] for y in value if y[0].isalpha()]
    upper_dict.update({key:value})

for x in lower_list:
    key = x[0]
    value = x[1:].split()
    value = [y[0] for y in value if y[0].isalpha()]
    lower_dict.update({key:value})

pairs_dict = stabalize_pairs(upper_dict, lower_dict)

for value in pairs_dict.values():
    print(value[0] + ":" + value[1])
