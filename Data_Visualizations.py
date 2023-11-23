#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib as plt
import seaborn as sns


# In[31]:


# Load the Iris dataset directly from Seaborn
iris_data = sns.load_dataset("iris")

# Create distributional plots for each trait

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

sns.histplot(data=iris_data, x='sepal_length', hue='species', palette= 'Set1', bins=20, ax=axs[0, 0])
axs[0, 0].set_title('Sepal Length Distribution by Species')

sns.histplot(data=iris_data, x='sepal_width', hue='species', palette = 'flare', bins=20, ax=axs[0, 1])
axs[0, 1].set_title('Sepal Width Distribution by Species')

sns.histplot(data=iris_data, x='petal_length', hue='species', palette = 'RdPu', bins=20, ax=axs[1, 0])
axs[1, 0].set_title('Petal Length Distribution by Species')

sns.histplot(data=iris_data, x='petal_width', hue='species', palette = 'inferno', bins=20, ax=axs[1, 1])
axs[1, 1].set_title('Petal Width Distribution by Species')

plt.tight_layout()
plt.show()


# In[33]:


#Bar plot based on each species
plt.figure(figsize=(10, 6))
sns.barplot(data=iris_data, x='species', y=iris_data.index, palette='PuBu')
plt.title('Species Distribution')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()


# In[48]:


#Scatter plot between traits based on each species
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
fig1 = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris_data, palette='Set1')
fig1.set_title('Scatter Plot of Sepal Length vs Sepal Width')

plt.subplot(1, 2, 2)
fig2 = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=iris_data, palette='Set2')
fig2.set_title('Scatter Plot of Petal Length vs Petal Width')

plt.tight_layout()
plt.show()


# Based on my visualization, the versicolor and virginica are more closely related than the setosa. Looking at the scatter plot between petal length and petal width, you can see that the versicolor and virginica have strong correlation. Their values also align more with each other while the setosa values is further from the versicolor and virginica.

# In[49]:


import pandas as pd


# In[51]:


data = pd.read_csv('/Users/gabi_reese/Downloads/Exercise_Data.csv')


# In[58]:


num_data = data.drop(labels = ['id','diet', 'kind'], axis = 1)
num_data = (num_data - num_data.min()) / (num_data.max() - num_data.min())
sns.heatmap(num_data)


# In[82]:


time = ['1 min', '15 min', '30 min']
for time in time:
# Categorical plot of pulse values by diet and exercise for each time duration
    plt.figure(figsize=(12, 6))
    fig1 = sns.barplot(x = 'diet', y = data[time], hue ='kind', data = data, palette = 'Spectral')
    fig1.set_title(f'Distributions of Pulse Values by Diet and Exercise Type ({time})')
    plt.xlabel('Diet Type')
    plt.ylabel(f'Pulse ({time})')
    plt.legend(title='Exercise Type')
    plt.tight_layout()
    plt.show()


# Based on my visualizations, the pulse rate of students is affected depending on the exercise of students and what diet they are participating in. For example, from my bar plots, when students exercised by running on a no fat diet their pulse rate was higher than the walkinging and resting at 15 min and 30 min. When students exercised by running on a low fat diet, their pulse  was higher than walking and running at 15 min and 30 min. 
