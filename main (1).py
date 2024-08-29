name = "Georgia" #variable storing a string
age = "3.5" # storing a decimal or an integer
hair_color = "brown" #make sure to use quotations on a string

print(name) #should print out Georgia

def hair_color_function(): #define a function called hair color
  if hair_color == "yellow":
    print("You've got yellow")
  else:
    print("You don't have yellow hair")
    
hair_color_function()

   
#now concatenate the name and the age and print it out 
sentencemerge = name + " " + "is" + " " + age
print(sentencemerge)

