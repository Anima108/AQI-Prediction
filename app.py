#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


import pickle


# In[3]:


import numpy as np


# In[4]:


app = Flask(__name__,template_folder='.')


# In[5]:


model=pickle.load(open('model_svm','rb'))


# In[6]:


@app.route('/',methods=['GET'])
def main():
        return render_template("AQI.html")

# In[ ]:

# In[7]:

@app.route('/', methods=['POST'])
def predict():
    #print(request.form)
    if request.method=='POST':

        final=[]

        final.append(float(request.form['pm2']))
        final.append(float(request.form['pm10']))
        final.append(float(request.form['no']))
        final.append(float(request.form['no2']))
        final.append(float(request.form['nox']))
        final.append(float(request.form['nh3']))
        final.append(float(request.form['co']))
        final.append(float(request.form['so2']))
        final.append(float(request.form['o3']))
        final.append(float(request.form['benzene']))
        final.append(float(request.form['toluene']))
        final.append(float(request.form['xylene']))
        
        
        final=np.array(final)
        
        #print(features)
        #print(final)
        
        arr=final.reshape(1, -1)

        prediction=model.predict(arr)
        
        #output='{0:.{1}f}'.format(prediction[0][1], 2)
    
    return render_template("AQI.html",pred = prediction)


# In[ ]:


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




