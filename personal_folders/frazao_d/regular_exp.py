# %%
import re 
with open('DSS_S22_Wilford_Woodruff_Papers/journals.txt') as journals_file:
    text = journals_file.read()
pattern = r"\[\[.+|.+]\]"
x = re.findall(pattern,text)

print(x)

# %%
