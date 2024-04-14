# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pickle
import numpy as np
 # Load the Random Forest Classifier model

filename = 'diabetes-prediction-rfc-model.pkl'

classifier = pickle.load(open(filename, 'rb'))
 
def predict(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age):

    data = np.array([[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]])

    prediction = classifier.predict(data)

    return prediction
 
def main():

    st.title('Diabetes Prediction')
 
    pregnancies = st.slider('Pregnancies', 0, 20, 1)

    glucose = st.slider('Glucose', 0, 200, 100)

    bloodpressure = st.slider('Blood Pressure', 0, 150, 70)

    skinthickness = st.slider('Skin Thickness', 0, 100, 20)

    insulin = st.slider('Insulin', 0, 900, 100)

    bmi = st.slider('BMI', 0.0, 70.0, 25.0)

    dpf = st.slider('Diabetes Pedigree Function', 0.0, 3.0, 1.0)

    age = st.slider('Age', 0, 100, 30)
 
    if st.button('Predict'):

        prediction = predict(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age)

        if prediction == 1:

            st.write('The person is likely to have diabetes.')

        else:

            st.write("The person is unlikely to have diabetes.")
 
if __name__ == '__main__':

    main()
