
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 5
plt.style.use('fivethirtyeight')


# In[3]:


df = pd.read_csv('911 calls- Mongomery county/911.csv')
df = df[df['zip'] > 10000]


# In[4]:


# lat: Latitude
# lng: Longitude
# desc: Description of Emergency
# zip: ZIP Code
# title: Title of Emergency
# time: StampDate and time of the call
# twp: Town
# addr: Address


# In[5]:


print (df.head())


# # Aspects to explore
# 1. How are emergencies ranked by frequency?<br>
#     1.1. What are the top few most frequent emergencies in each type? <br>
#     1.2. Subcategories by count.
#     
# 2. Location based exploration <br>
#     2.1. Do specific emergencies happen at specific places more than the others?
#         - a. Plot emergency categories by 1. town,
#                                           2. zip,
#                                           3. Latitude, longitude
#         - b. Under categories, plot each sub category by 1. town,
#                                                          2. zip,
#                                                          3. Latitude, longitude.
#         
# 3. Time based exploration<br>
#     3.1. Is there a specific time window when an emergency occurs?
#         - a. By time of day
#             - Plot emergency categories
#                 - Plot emergency subcategories
#         - b. By month
#             - Plot emergency categories
#                 - Plot emergency subcategories
#                 
# 4. Geo-temporal exploration<br>
#     4.1. Do emergencies show any pattern?
#         - a. At a given time, which place needs most attention? What type of attention is it?

# In[6]:


df.columns = ['latitude','longitude','description','zip','type','time','town','address','if_emergency']


# In[7]:


df.dtypes


# In[8]:


df['time'] = pd.to_datetime(df['time'])
print (df['time'].max())
print (df['time'].min())
print (df['time'].max() - df['time'].min())


# In[9]:


df.count()


# In[10]:


df.head()


# ## 1. General Exploration (1/4)

# ### 1.1. Ranking emergency categories by frequency

# In[11]:


df2= df.groupby('type')


# In[12]:


grouped = df.groupby('type').agg({'type':'count'}).sort_values('type')[::-1][:30]/len(df)*100


# In[13]:


grouped


# In[14]:


xi = grouped.values[:,0]
yi = grouped.index
plt.subplots(figsize=(20,15))
sns.barplot(x=xi,y=yi,color='r')


sns.set(style="whitegrid")
sns.set_color_codes("muted")
sns.set(font_scale=2)   
sns.despine(left=True, bottom=True)

sns.set(font_scale=2)
plt.xlim=(0,25)
plt.ylabel("Emergency")
plt.xlabel("Percentage of all 911 calls")
plt.title('30 most common reasons behind 911 calls')
plt.show()


# In[15]:


## Categorizing data by emergency type
df_title_cat = pd.DataFrame(df.type.str.split(':',1).tolist(),columns = ['emergency_type','emergency_subtype'])
df_cat = df.copy()
del df_cat['type']
df_cat.insert(4,'emergency_type',df_title_cat['emergency_type'].values)
df_cat.insert(5,'emergency_subtype',df_title_cat['emergency_subtype'].values)


# In[16]:


df_cat.head()


# In[17]:


grouped_by_type = df_cat.groupby('emergency_type').agg(
    {'emergency_type':'count'}).sort_values('emergency_type')[::-1][:10]/len(df_cat)*100


# In[18]:


plt.style.use('fivethirtyeight')

grouped = grouped_by_type
yi = grouped.values[:,0]
xi = grouped.index
plt.subplots(figsize=(3,7))
plt.style.use('fivethirtyeight')

sns.barplot(x=xi,y=yi,color='b')


sns.set(style="whitegrid")
sns.set_color_codes("muted")
sns.set(font_scale=2)   
sns.despine(left=True, bottom=True)

sns.set(font_scale=1)
plt.xlim=(0,100)
plt.xlabel("")
plt.ylabel('Percentage of Total Number of Calls')
plt.show()
# plt.title('All 911 calls Grouped by Emergency Types')


# In[19]:


grouped_by_emstype = df_cat[df_cat['emergency_type']=='EMS'].groupby('emergency_subtype').agg({
    'emergency_type':'count'}).sort_values('emergency_type')[::-1][:10]/len(df_cat)*100


# In[20]:


grouped = grouped_by_emstype
plt.style.use('fivethirtyeight')

xi = grouped.values[:,0]/sum(grouped.values[:,0])*100
yi = grouped.index
plt.subplots(figsize=(20,7))
sns.barplot(x=xi,y=yi,color='r')


sns.set(style="whitegrid")
sns.set_color_codes("muted")
sns.set(font_scale=2)   
sns.despine(left=True, bottom=True)

sns.set(font_scale=1.5)
plt.xlim=(0,100)
plt.ylabel("")
plt.xlabel("Percentage of All EMS Calls")
plt.title('EMS Calls Grouped by Emergency Sub-type')
plt.show()


# In[21]:


grouped_by_traffictype = df_cat[df_cat['emergency_type']=='Traffic'].groupby('emergency_subtype').agg({
    'emergency_type':'count'}).sort_values('emergency_type')[::-1][:10]/len(df_cat)*100


# In[22]:


grouped = grouped_by_traffictype
plt.style.use('fivethirtyeight')

xi = grouped.values[:,0]/sum(grouped.values[:,0])*100
yi = grouped.index
plt.subplots(figsize=(20,7))
sns.barplot(x=xi,y=yi,color='r')

sns.set(style="whitegrid")
sns.set_color_codes("muted")
sns.set(font_scale=2)   
sns.despine(left=True, bottom=True)

sns.set(font_scale=1.5)
plt.xlim=(0,100)
plt.ylabel("")
plt.xlabel("Percentage of All Traffic calls")
plt.title('Traffic Calls Grouped by Emergency Sub-type')
plt.show()


# In[23]:


grouped_by_firetype = df_cat[df_cat['emergency_type']=='Fire'].groupby('emergency_subtype').agg({
    'emergency_type':'count'}).sort_values('emergency_type')[::-1][:10]/len(df_cat)*100


# In[24]:


grouped = grouped_by_firetype
plt.style.use('fivethirtyeight')

xi = grouped.values[:,0]/sum(grouped.values[:,0])*100
yi = grouped.index
plt.subplots(figsize=(20,7))
sns.barplot(x=xi,y=yi,color='r')

sns.set(style="whitegrid")
sns.set_color_codes("muted")
sns.set(font_scale=2)   
sns.despine(left=True, bottom=True)

sns.set(font_scale=1.5)
plt.xlim=(0,100)
plt.ylabel("")
plt.xlabel("Percentage of All Fire calls")
plt.title('Fire Calls Grouped by Emergency Sub-type')
plt.show()


# ## 2. Location-based Exploration

# ### 2.1. Emergency categories by town

# In[25]:


count_by_town = df_cat[df_cat['emergency_type'] == 'EMS'].groupby('town').agg({'town':'count'}).sort_values('town')[::-1][:20]


# In[26]:


grouped = count_by_town
plt.style.use('fivethirtyeight')

xi = grouped.values[:,0]/1000
yi = grouped.index
plt.subplots(figsize=(20,7))
sns.barplot(x=xi,y=yi,color='r')

sns.set(style="whitegrid")
sns.set_color_codes("muted")
sns.set(font_scale=2)   
sns.despine(left=True, bottom=True)

sns.set(font_scale=1.5)
plt.xlim=(0,100)
plt.ylabel("")
plt.xlabel("1000 Calls")
plt.title('EMS Calls Grouped by Town')
plt.show()


# In[27]:


count_by_zip = df_cat[df_cat['emergency_type'] == 'EMS'].groupby('zip').agg({'zip':'count'}).sort_values('zip')[::-1].iloc[:20]
count_by_zip.columns = ['count']


# In[28]:


grouped = count_by_zip
plt.style.use('fivethirtyeight')

yi = count_by_zip['count']
xi = count_by_zip.index
plt.subplots(figsize=(20,7))
sns.barplot(x=xi,y=yi,color='r')

sns.set(style="whitegrid")
sns.set_color_codes("muted")
sns.set(font_scale=2)   
sns.despine(left=True, bottom=True)

sns.set(font_scale=1.5)
plt.xlim=(0,100)
plt.ylabel("1000 Calls")
plt.title('EMS Calls Grouped by zip')
plt.show()


# In[29]:


count_by_zip = df_cat.groupby('zip').agg({'zip':'count'}).sort_values('zip')[::-1]
count_by_zip['cumsum_percent'] = count_by_zip.cumsum()/len(df)*100
count_by_zip.columns = ['count','cumsum_percent']


# In[30]:


count_by_zip[count_by_zip['cumsum_percent']<81].count()/len(count_by_zip)
# 80% of all EMS calls originated only from about 25% of zip codes
# 99% of all EMS calls originated only from about 45% of zip codes


# In[31]:


plt.style.use('fivethirtyeight')

plt.plot(range(len(count_by_zip)),count_by_zip['cumsum_percent'])
plt.xlabel('Number of Zip Codes')
plt.ylabel('Percent of all EMS Calls')
plt.axhline(y = 80,xmin = 0,xmax =0.22,color = 'r')
plt.axvline(x = 26,ymax = 0.75,color='r')

plt.show()


# In[32]:


print (str(len(df_cat['zip'].unique()))+' unique zip codes.')
print (str(len(df_cat['town'].unique()))+ ' unique towns.')


# ## Plot all calls on map

# <img src ="images/calls_by_zip.png">

# ## Plot EMS calls on map

# In[33]:


only_EMS_view = df_cat[df_cat['emergency_type']=='EMS']


# In[34]:


only_EMS_view.to_csv('segregated_data.csv')


# In[35]:


only_EMS_view


# In[36]:


df_cat['zip'].unique()


# In[37]:


us_pop = pd.read_csv('us-population-by-zip-code/population_by_zip_2010.csv')


# In[38]:


us_pop.head()


# In[39]:


us_pop_by_zip = us_pop[us_pop['zipcode'].isin(df_cat['zip'].unique())].groupby('zipcode').agg({'population':'sum'})


# In[40]:


result = pd.concat([us_pop_by_zip, count_by_zip], axis=1, sort=False)


# In[41]:


result.dropna(inplace=True)


# In[42]:


result.sort_values('population').corr()
# As seen, population and EMS calls are very poorly correlated


# ## 3. Analyze EMS Calls according to time

# In[43]:


plt.style.use('fivethirtyeight')
sns.distplot(df_cat[df_cat['emergency_type'] == 'EMS']['time'].dt.hour,bins=24)
plt.ylabel('Inverse of calls per hour')
plt.xlabel('Time of Day')

plt.show()


# In[44]:


plt.style.use('fivethirtyeight')
sns.distplot(df_cat[df_cat['emergency_type'] == 'EMS']['time'].dt.hour[df_cat['time'].dt.month==6],bins=24,label='June')
sns.distplot(df_cat[df_cat['emergency_type'] == 'EMS']['time'].dt.hour[df_cat['time'].dt.month==12],bins=24,label='December')
plt.ylabel('Inverse of calls per hour')
plt.xlabel('Time of Day')

plt.legend()
plt.show()


# In[45]:


plt.style.use('fivethirtyeight')
sns.distplot(df_cat[df_cat['emergency_subtype'] == ' RESPIRATORY EMERGENCY']['time'].dt.hour[df_cat['time'].dt.month==6],bins=24,label='June')
sns.distplot(df_cat[df_cat['emergency_subtype'] == ' RESPIRATORY EMERGENCY']['time'].dt.hour[df_cat['time'].dt.month==12],bins=24,label='December')
plt.ylabel('Inverse of calls per hour')
plt.xlabel('Time of Day')

plt.legend()
plt.show()


# In[46]:


df_cat['date'] = df_cat['time'].dt.date
df_cat.head()


# In[47]:


daily_count = df_cat[df_cat['zip']==19401.0].groupby('date').agg({'if_emergency':'count'}).sort_values('date')
daily_count.head()#['year'] = 


# In[48]:


daily_count.describe()


# In[49]:


plt.style.use('fivethirtyeight')
sns.distplot(daily_count,label='Distribution of daily emergencies in 19401')
plt.xlabel('Number of calls')
plt.legend()
plt.show()


# In[50]:


plt.style.use('seaborn')
daily_count.plot()

