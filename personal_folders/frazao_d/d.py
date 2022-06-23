clean_text_list = []
with open('derived_data/journals.txt') as journals_file:
 text = journals_file.read()
a1 = text
def cleaning_data(text):
 a2 = text.replace('[[','').replace(']]','').replace('[figure','').replace(']','')
 return a2
