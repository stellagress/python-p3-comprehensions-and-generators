#!/usr/bin/env python3

# def return_evens(num_list):
#     even_num=[]
#     for n in num_list:
#         if n % 2 == 0:
#             even_num.append(n)
#     return even_num


def return_evens(num_list):
    even_num=[]
    for n in num_list:
        if n % 2 == 0:
            even_num.append(n)
    return even_num
    


# def return_evens(num_list):
#     return [(n % 2 == 0) for n in num_list]





# def make_exclamation(sentence_list):
#     words = []

#     while len(words) <  len(sentence_list):
#         words.append("!")
#     return words



def make_exclamation(sentence_list):
    exclamation_point = []

    for s in sentence_list:
        exclamation_point.append(s + "!")
        
    return exclamation_point

















