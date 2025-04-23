set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print(set1 & set2)
print(set1.intersection(set2))

text1 = "my name is junil"
text2 = "my name is junlee"

textList1 = text1.split(" ")
textList2 = text2.split(" ")
print(textList1)
print(textList2)

textSet1 = set(textList1)
textSet2 = set(textList2)
print(textSet1)
print(textSet2)

print(textSet1 & textSet2)
print((textSet1 | textSet2) - (textSet1 & textSet2))    # {'junlee', 'junil'}

