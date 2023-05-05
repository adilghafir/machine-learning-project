import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))
st.sidebar.write("MASTER DSEF")
st.sidebar.write("Prepared by: ADIL GHAFIR")
st.sidebar.write("Supervised by: MR TALI")
def main():
    st.title("House Price Prediction App ")
    st.write("Enter the number of rooms and distance to employment centers to predict the price of the house:")

    rooms = st.number_input("Number of rooms per dwelling:", value=1)
    distance = st.number_input("Distance to employment centers (in km):", value=1)

    if st.button("Predict"):
        prediction = model.predict([[rooms, distance]])
        output = round(prediction[0], 2)
        st.write(f'A house with {rooms} rooms per dwelling and located {distance} km to employment centers has a value of ${output}K')

if __name__ == '__main__':
    main()
