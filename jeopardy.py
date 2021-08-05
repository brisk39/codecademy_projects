#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[26]:


jeopardy_data = pd.read_csv("jeopardy.csv")


# In[168]:


# look at the first 10 rows of the data
jeopardy_data.head(10)


# In[28]:


# look at the column names and find some formatting issues
jeopardy_data.columns


# In[31]:


# rename the volumns in a proper format
jeopardy_data = jeopardy_data.rename(columns = {" Air Date": "Air Date", " Round": "Round", " Category": "Category", " Value": "Value", " Question": "Question", " Answer": "Answer"})


# In[32]:


# look at questions
jeopardy_data["Question"]


# In[62]:


# to return rows of the question that has certain words in a list
# list expression: word in x for word in words will provide a list of boolean values
# all(True...) is True otherwise false
# the returned result here is dataframe not series
def filter(words):
    return jeopardy_data.loc[jeopardy_data["Question"].apply(lambda x: all(word in x for word in words))]


# In[63]:


filter(["King", "England"])


# In[66]:


# to return rows of the questions that has the word with variances(all letters lower case, all capital letters, or a combination of lower and upper cases)
def intermediate_filter(words):
    return jeopardy_data.loc[jeopardy_data["Question"].apply(lambda x: all(word.lower() in x.lower() for word in words))]


# In[67]:


# call the function
# Finding: There are so noises in this function, e.g. row 6337, Viking
intermediate_filter(["KIng", "ENGLAND"])


# In[107]:


# to refine last function: capitalize the first letter to exclude words like vking
def advanced_filter(words):
    return jeopardy_data.loc[jeopardy_data["Question"].apply(lambda x: all((word.lower()).capitalize() in x for word in words))]


# In[108]:


# to find the exact match of England and King
advanced_filter(["ENGLAND", "KIng"])


# In[124]:


# aggregate statistics
# change value to float into a new column: value_float
jeopardy_data["Value_float"] = jeopardy_data.Value.apply(lambda x: float(x[1:].replace(",","")) if x != "None" else 0)
print(jeopardy_data["Value_float"])


# In[127]:


# function returns the count of the unique answers to all of the questions in a dataset
def unique_count(word):
    question = jeopardy_data.loc[jeopardy_data["Question"].apply(lambda x: word.lower() in x.lower())]
    return question.Answer.nunique()
    


# In[128]:


# There are 812 uniques answers to the questions which have a word England in them.
# Finding: The result of the figure wont tell us anything special here, so we may modify the format of the output.
# A summary like a table may suffice our needs.
unique_count("England")


# In[166]:


# modified function to show an output of a table
# inplace = True: modifies existing dataframe
def unique_counts(word):
    question = jeopardy_data.loc[jeopardy_data["Question"].apply(lambda x: word.lower() in x.lower())]
    summary = question.groupby("Answer").Question.count().reset_index()
    summary.rename(columns = {"Question" : "Answer_Count"}, inplace = True)
    summary.sort_values(by = "Answer_Count", ascending = False)
    return summary


# In[167]:


unique_counts("England")


# In[ ]:




