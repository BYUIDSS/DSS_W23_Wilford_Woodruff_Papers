import matplotlib.pyplot as plt
clean_text_list = []
with open('derived_data/journals.txt') as journals_file:
 text = journals_file.read()
a1 = text
x = text.count("Brigham Young Jr")
print(f"{x}")
#d#ef cleaning_data(text):
# #a2 = text.replace('[[','').replace(']]','').replace('[figure','').replace(']','')
# #return a2

# x-coordinates of left sides of bars 
left = [1, 2,]
  
# heights of bars
height = [9000, 34000,]
  
# labels for bars
tick_label = ['places', 'persons']
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.5, color = ['red', 'green'])
  
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('Persons x places')
  
# function to show the plot
plt.show()
