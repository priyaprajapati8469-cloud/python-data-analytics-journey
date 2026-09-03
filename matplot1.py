import matplotlib.pyplot as plt
#matplotlib-main package
#pyplot-module that provide redimate functions(kind of redimate paintbrush set)
#plt-standard name

x=[1,2,3,4]
y=[10,20,15,25]

 #plot-function, that is a reusable tool that perform specific task
plt.plot(x,y)   #plt.plot(horizontal value ,vertical value)
plt.show()

x=['mon','tue','wed','thu','fri','sat']
y=[12,10,4,8,11,20]
plt.plot(x,y)
plt.title("this is cake sales data")
plt.xlabel("days of week")
plt.ylabel("no of cake sold")
plt.show()

#plt.plot(x,y,color='color name',linestyle='line_style',linewidth=value,marker='marker symbol',label='label name')
months=[1,2,3,4]
sales=[1000,1500,1200,4000]

plt.plot(months,sales,color='blue',linestyle='-.',linewidth=2,marker='o',label='2025 sales data')
plt.xlabel("no of months")
plt.ylabel("amount of sales")
# plt.title( "monthly  data  analysis")
plt.legend(loc="upper left",fontsize=10)     #upper left -top left corner    lower right-bottom right corner
plt.grid(color="green",linestyle=":",linewidth=1)
plt.xlim(1,5000)
plt.ylim(0,)
plt.xticks([1,2,3,4],['m1','m2','m3','m4'])
plt.show()

#Bar Chart
# synatx=plt.bar(x,height,'color name',width=value,label='label name')
product=['A','B','C','D']
sales=[1200,800,1000,1100]
plt.barh(product,sales,color='olive',label='sales 2025')     #barh-displar bar horizontally     barv-display bar vertically
plt.xlabel("product")
plt.ylabel("sales")
plt.title("product sales comparison")
plt.legend()
plt.show()

#Pie Chart
#synatx-plt.pie(values,labels=label_list,colors=color_list,autopct='%1.1f%%')
region=['north','south','east','west']
revenue=[3000,4000,1500,1000]
plt.pie(revenue,labels=region,autopct='%1.1f%%',colors=['gold','skyblue','lightgreen','coral'])
plt.title("revenue contribution by region")
plt.show()

#histogram
#synatx-plt.hist(data,bins=numbers_of_bins,color="colorname",edgecolor='black')
scores=[45,55,78,90,78,57,45,64,75,88,90,92,83,68,77,88,45,32,54,67,53,56,89,36,70]
plt.hist(scores,bins=5,color='pink',edgecolor='red')
plt.xlabel("score range")
plt.ylabel("nimbers of students")
plt.title('score distribution of students')
plt.legend()
plt.show()
