import pandas as pd
import re

url = "https://github.com/BYUIDSS/DSS_S22_Wilford_Woodruff_Papers/blob/master/raw_data/wwp.csv?raw=true"
wwp = pd.read_csv(url, encoding = 'unicode-escape')

test_text = " December 17, 2020 ~Monday: Today sucked, it was very cold."

pattern = r"[A-Z]\w+\s\d+,\s\d+\s~[A-Z]\w+"

print(re.findall(pattern, test_text))