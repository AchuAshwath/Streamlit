import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris FLower Prediction App
This app predicts Iris flower type
""")

# side bar to get input values
st.sidebar.header("User Input Parameters")


def user_input_features():
    sepal_length = st.sidebar.slider("sepal_length", 4.3, 7.9, 5.3)
    sepal_width = st.sidebar.slider("sepal_width", 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider("petal_length", 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider("petal_width", 0.1, 2.5, 0.2)
    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

# displaying the input
st.subheader("User Input Parameters")
st.write(df)

# loading the Iris data set
iris = datasets.load_iris()
x = iris.data
y = iris.target

# using sklearn's randomforstclasifier to predict the species
clf = RandomForestClassifier()
clf.fit(x, y)

prediction = clf.predict(df)
prediction_prob = clf.predict_proba(df)

st.subheader("Class labels and their corresponding index number")
st.write(iris.target_names)

# displaying the prediction
st.subheader("Prediction")
st.write(iris.target_names[prediction])

# displaying the prediction probability
st.write("Prediction Probability")
st.write(prediction_prob)
