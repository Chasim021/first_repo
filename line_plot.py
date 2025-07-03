import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import seaborn as sns
import matplotlib.pyplot as plt
# sns.set_theme(style="ticks" , color_codes=True)
phol=sns.load_dataset("iris") 
sns.lineplot(x='species' , y='petal_width' , data=phol)
plt.show()
print(phol)
