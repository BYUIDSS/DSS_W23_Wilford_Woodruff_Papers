clean_text_list = []
with open('derived_data/journals.txt') as journals_file:
 text = journals_file.read()
a1 = text
a2 = a1.replace('[[','').replace(']]','').replace('[figure','').replace(']','')
clean_text_list.append(a2)
print(clean_text_list)