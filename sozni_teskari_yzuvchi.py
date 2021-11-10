"""
NOT COMPLETED
"""

text = input('Matn: ')
text_list = list(text[::-1])

# print(text_list)
index, index2 = None, None

print(text_list)
def a_apostrophe():
    if "'" in text_list:
        index = text_list.index("'")
        index2 = index + 1
        text_list[index], text_list[index2] = text_list[index2], text_list[index]

def the_apostrophe():
    i = 0
    while i <= len(text_list):
        if text_list[i] == "'":
            index = text_list.index(text_list[i])
            index2 = index+1
            # print(text_list[index], text_list[index2])
            text_list[index], text_list[index2] = text_list[index2], text_list[index]
            print(text_list)
        i+=1

if text_list.count("'") == 1:
    a_apostrophe()
elif text_list.count("'") > 1:
    the_apostrophe()

text = ''
for char in text_list:
    text+=char
print(text)