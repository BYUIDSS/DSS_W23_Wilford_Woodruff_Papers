import pandas as pd
import re


test_text = '''23d I met in the Legislative Council. A short speech was 
made By [[Lorenzo Snow|Lorenzo Snow]] various subjects talked over then 
A subscription List was presented to the council to see how 
many each person would sustain in the Armey now to be fitted 
up for next summers campaign. I signed 2 person which 
I have to Furnish with 3 Animals clothing, bedding, Arms, amunit[ion] 
food, &c &c. After transacting the business of the day we adjourned 
untill the 4th day of January. I have been troubled for 
several days with severe pain in one of my Eye teeth. I had taken
cold & it had setled in my Jaw & tooth and it was swoolen & 
much inflamed. I called upon a Dentist and had it pulled 
as soon as He pulled it my Mouth filled with Blood. He gave 
me a cup of cold water to rens my mouth. I spit out the 
Blood & filled my mouth with cold water it struck my 
brain numb like a stroak of the Palsey for a few seconds the 
then the numness left me and at each beat of the pulse a 
[FIGURE] A Pain went through my Brain like an Arrow 
or a thunder bolt for the term of two hours untill it appeared 
as though my head would burst. This pain continued in my 
head untill I covered my head with hot potatoe poultice & got 
into a high state of perspiration. I never before heard of an instance 
of this kind. I reason upon it thus that it being an Eye tooth 
& taking cold water into my mouth before the goum had closed
the water chilled the nerve runing from the tooth through the Eye 
to the Brain and the cold Blood was instantly carried to the 
Brain which created a concussion which was both excruciating 
and dangerous had the water been warm instead of cold no
such effect would have been produced. Let surgeon & Dentist observe 
this rule when pulling Eye teeth use warm water instead of cold'''

pattern = r"[A-Z]\w+\s\d+,\s\d+\s~[A-Z]\w+"
patter_nouns = r"[["

print(re.findall(pattern, test_text))