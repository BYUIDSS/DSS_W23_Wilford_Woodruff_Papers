import re

test_text = '''19th Sunday I was quite poorly & did not attend meeting Lorenzo 
D Young spok followed by [[Heber Chase Kimball|H. C. Kimball]] Wm Brace [[Stephen H. Godard|Steph [Godard]]] & George 
Godard & [[William Carter|Wm Carter]], & in the Afternoon [[Henry Harriman|H Harriman]] & President 
[[Brigham Young|B Young]] follow by many missionaries
in Texas & the Twelve in London. The statistical account 
of the financial affairs of the Church was read. In the afternoon 
[[Daniel Hanmer Wells|D. H. Wells]] & [[Heber Chase Kimball|H. C. Kimball]] spoke, followed by Preside,t [[Brigham Young|B. Young]] 
who delivered a vary interesting account upon practical economy 
I attended the 70 meeting in the evening at the 70 Hall & had a 
full House & a good time. I spoke a short time to them I followed 
[[Joseph Young|Joseph Young]]. [[Orson Hyde|O Hyde]] attended the High Priest meeting President 
B. Young spoke to them'''

with open('derived_data\journals.txt') as journals_file:
    text = journals_file.read()

def get_nouns(text):
    pattern = r"\[\[.+?\|"
    clean_nouns = []
    captured = re.findall(pattern, text)
    for noun in captured:
        clean_noun = noun.strip("[|")
        clean_nouns.append(clean_noun)  
    
    return clean_nouns


print(get_nouns(text))

