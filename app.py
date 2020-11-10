#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


import pickle


# In[3]:


import numpy as np


# In[4]:


app = Flask(__name__)


# In[5]:


model=pickle.load(open('model_svm','rb'))


# In[6]:


@app.route('/',methods=['GET'])
def hello_world():
    if flask.request.method == 'GET':
        return render_template('AQI.html')

# In[ ]:

# In[7]:

@app.route('/predict', methods=['POST'])

def predict():
    #print(request.form)
    int_features=[str(x) for x in request.form.values()]
    req_model=int_features[12]

    for x in range (11):
        final[x]=float(int_features[x])
    #final=np.array(features)
    #print(features)
    #print(final)
    
    arr=final.reshape(1, -1)

    prediction=model.predict(arr)
    
    output='{0:.{1}f}'.format(prediction[0][1], 2)
    
    return render_template('AQI.html',pred = 'Pedicted AQI - {}'.format(output))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




