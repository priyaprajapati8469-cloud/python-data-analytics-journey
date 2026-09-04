import matplotlib.pyplot as plt
#scatterplot syntax-plt.scatter(x,y,color="color name",marker="marker style",label="label name")
#scatter plot is used to find correlation between two variables (comparison)
hours_study=[1,2,3,4,5,6,7,8,9]
exam_score=[39,45,50,64,79,85,86,90,95]
plt.scatter(hours_study,exam_score,color="green",marker="+",label="student result data based on hours of study")
plt.xlabel("hours study")
plt.ylabel("exam scores")
plt.title("relationship btw study time and exam score")
plt.legend()
plt.grid(True)
plt.show()

plt.scatter([1,2,3],[45,56,92],color='blue',label='class A')   #group1
plt.scatter([1,2,3],[45,50,52],color='orange',label='class B')   #group2
plt.xlabel("hours study")
plt.ylabel("exam scores")
plt.title("comparison of two classes")
plt.legend()
plt.grid(True)
plt.show()

# subplots and layout adjustments
#subplot syntax-plt.subplot(nrows,ncolumns,index)
x=[1,2,3,4]
y=[10,20,15,25]
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("line chart")

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("bar chart")

# # plt.light_layout()
plt.show()

# x=[1,2,3,4]
# y=[10,20,15,25]
# syntax-fig,ax=plt.subplots(nrows,ncolumns,figsize=(width,height))
fig,ax=plt.subplots(1,2,figsize=(10,5))
x=[1,2,3,4]
y=[10,20,15,25]
ax[0].plot(x,y)
ax[0].set_title("line plot")


ax[1].bar(x,y,color="green")
ax[1].set_title("bar chart")
fig.suptitle("this is line graph and bar chart")

plt.tight_layout()
plt.show()


#save figures syntax-savefig()





