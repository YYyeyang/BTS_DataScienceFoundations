
# coding: utf-8

# In[2]:

traffic_data={"2013":[2144,343,455,1223,111,6644,765],
              "2014":[4324,654,7543,321,566,777,4334],
              "2015":[5454,432,666,4333,765,432,876],
              "2016":[4324,565,333,777,888,444,555],
              "2017":[333,444,555,666,777,888,999]}

mini=min(traffic_data["2016"])
print(mini)


if mini > 200:
    print("data", mini,"is stored")

else:
    print("nothing is stored")


# In[3]:

"store {0}".format(mini)


# In[ ]:



