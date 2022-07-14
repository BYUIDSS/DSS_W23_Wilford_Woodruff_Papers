import matplotlib.pyplot as plt
import re
clean_text_list = []
with open('derived_data/journals.txt') as journals_file:
 text = journals_file.read()
a1 = text
x = text.count("Brigham Young Jr")
#print(f"{x}")

def main():
        PLACE_INDEX = 0
        PEOPLE_INDEX = 1
        g_n = get_nouns(text)
        x = g_n[PLACE_INDEX]
        y = g_n[PEOPLE_INDEX]
        # x-coordinates of left sides of bars 
        left = [1, 2,]
        
        # heights of bars
        height = [x, y,]
        
        # labels for bars
        tick_label = ['places', 'persons']
        
        # plotting a bar chart
        plt.bar(left, height, tick_label = tick_label,
                width = 0.5, color = ['brown', 'purple'])
        
        # naming the x-axis
        plt.xlabel('x - axis')
        # naming the y-axis
        plt.ylabel('y - axis')
        # plot title
        plt.title('Places x Persons')
        
        # function to show the plot
        plt.show()
#d#ef cleaning_data(text):
# #a2 = text.replace('[[','').replace(']]','').replace('[figure','').replace(']','')
# #return a2
def get_nouns(text):
    # Pattern to grab nouns formatted as "[[NOUN ...|"
    pattern = r"\[\[.+?\|"
    # People and place lists initialized
    clean_places = []
    clean_people = []
    # The nouns are captured from given text.
    captured = re.findall(pattern, text)

    # The nouns are cleaned of brackets and 
    for noun in captured:
        clean_noun = noun.strip("[|")
        if "," in clean_noun:
            if ", b." in clean_noun:
                clean_people.append(clean_noun)
            else:
                clean_places.append(clean_noun)
        else:
            clean_people.append(clean_noun)
    
    return [len(clean_people), len(clean_places)]
main()