import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image

# st.title('Banglore House Price Prediction App')

# # Header Image
# image = Image.open('house.jpg')
# st.image(image, use_column_width='auto')

# X = pd.read_csv("data.csv", index_col='Unnamed: 0')

# location_data = ['1st Block Jayanagar', '1st Phase JP Nagar', '2nd Phase Judicial Layout',
#                  '2nd Stage Nagarbhavi', '5th Block Hbr Layout',
#                  '5th Phase JP Nagar', '6th Phase JP Nagar', '7th Phase JP Nagar', '8th Phase JP Nagar',
#                  '9th Phase JP Nagar', 'AECS Layout', 'Abbigere', 'Akshaya Nagar', 'Ambalipura',
#                  'Ambedkar Nagar', 'Amruthahalli', 'Anandapura', 'Ananth Nagar', 'Anekal', 'Anjanapura', 'Ardendale',
#                  'Arekere', 'Attibele',
#                  'BEML Layout', 'BTM 2nd Stage', 'BTM Layout', 'Babusapalaya', 'Badavala Nagar', 'Balagere',
#                  'Banashankari', 'Banashankari Stage II',
#                  'Banashankari Stage III', 'Banashankari Stage V', 'Banashankari Stage VI', 'Banaswadi',
#                  'Banjara Layout', 'Bannerghatta',
#                  'Bannerghatta Road', 'Basavangudi', 'Basaveshwara Nagar', 'Battarahalli', 'Begur', 'Begur Road',
#                  'Bellandur',
#                  'Benson Town', 'Bharathi Nagar', 'Bhoganhalli', 'Billekahalli', 'Binny Pete', 'Bisuvanahalli',
#                  'Bommanahalli',
#                  'Bommasandra', 'Bommasandra Industrial Area', 'Bommenahalli', 'Brookefield', 'Budigere',
#                  'CV Raman Nagar', 'Chamrajpet',
#                  'Chandapura', 'Channasandra', 'Chikka Tirupathi', 'Chikkabanavar', 'Chikkalasandra', 'Choodasandra',
#                  'Cooke Town', 'Cox Town',
#                  'Cunningham Road', 'Dasanapura', 'Dasarahalli', 'Devanahalli', 'Devarachikkanahalli', 'Dodda Nekkundi',
#                  'Doddaballapur', 'Doddakallasandra', 'Doddathoguru',
#                  'Domlur', 'Dommasandra', 'EPIP Zone', 'Electronic City', 'Electronic City Phase II',
#                  'Electronics City Phase 1', 'Frazer Town', 'GM Palaya',
#                  'Garudachar Palya', 'Giri Nagar', 'Gollarapalya Hosahalli', 'Gottigere', 'Green Glen Layout',
#                  'Gubbalala', 'Gunjur',
#                  'HAL 2nd Stage', 'HBR Layout', 'HRBR Layout', 'HSR Layout', 'Haralur Road', 'Harlur', 'Hebbal',
#                  'Hebbal Kempapura',
#                  'Hegde Nagar', 'Hennur', 'Hennur Road', 'Hoodi', 'Horamavu Agara', 'Horamavu Banaswadi', 'Hormavu',
#                  'Hosa Road', 'Hosakerehalli', 'Hoskote', 'Hosur Road',
#                  'Hulimavu', 'ISRO Layout', 'ITPL', 'Iblur Village', 'Indira Nagar', 'JP Nagar', 'Jakkur',
#                  'Jalahalli', 'Jalahalli East', 'Jigani', 'Judicial Layout', 'KR Puram', 'Kadubeesanahalli', 'Kadugodi',
#                  'Kaggadasapura', 'Kaggalipura', 'Kaikondrahalli', 'Kalena Agrahara', 'Kalyan nagar', 'Kambipura',
#                  'Kammanahalli', 'Kammasandra', 'Kanakapura', 'Kanakpura Road', 'Kannamangala', 'Karuna Nagar',
#                  'Kasavanhalli', 'Kasturi Nagar', 'Kathriguppe', 'Kaval Byrasandra', 'Kenchenahalli', 'Kengeri',
#                  'Kengeri Satellite Town', 'Kereguddadahalli', 'Kodichikkanahalli', 'Kodigehaali', 'Kodigehalli',
#                  'Kodihalli', 'Kogilu', 'Konanakunte', 'Koramangala', 'Kothannur', 'Kothanur', 'Kudlu', 'Kudlu Gate',
#                  'Kumaraswami Layout', 'Kundalahalli',
#                  'LB Shastri Nagar', 'Laggere', 'Lakshminarayana Pura', 'Lingadheeranahalli', 'Magadi Road',
#                  'Mahadevpura', 'Mahalakshmi Layout', 'Mallasandra',
#                  'Malleshpalya', 'Malleshwaram', 'Marathahalli', 'Margondanahalli', 'Marsur', 'Mico Layout',
#                  'Munnekollal', 'Murugeshpalya', 'Mysore Road', 'NGR Layout', 'NRI Layout', 'Nagarbhavi', 'Nagasandra',
#                  'Nagavara',
#                  'Nagavarapalya', 'Narayanapura', 'Neeladri Nagar', 'Nehru Nagar', 'OMBR Layout', 'Old Airport Road',
#                  'Old Madras Road', 'Padmanabhanagar', 'Pai Layout', 'Panathur', 'Parappana Agrahara',
#                  'Pattandur Agrahara', 'Poorna Pragna Layout',
#                  'Prithvi Layout', 'R.T. Nagar', 'Rachenahalli', 'Raja Rajeshwari Nagar', 'Rajaji Nagar', 'Rajiv Nagar',
#                  'Ramagondanahalli', 'Ramamurthy Nagar', 'Rayasandra', 'Sahakara Nagar', 'Sanjay nagar',
#                  'Sarakki Nagar', 'Sarjapur', 'Sarjapur  Road', 'Sarjapura - Attibele Road', 'Sector 2 HSR Layout',
#                  'Sector 7 HSR Layout', 'Seegehalli', 'Shampura', 'Shivaji Nagar', 'Singasandra',
#                  'Somasundara Palya', 'Sompura', 'Sonnenahalli', 'Subramanyapura', 'Sultan Palaya', 'TC Palaya',
#                  'Talaghattapura', 'Thanisandra', 'Thigalarapalya', 'Thubarahalli', 'Thyagaraja Nagar', 'Tindlu',
#                  'Tumkur Road', 'Ulsoor', 'Uttarahalli', 'Varthur', 'Varthur Road', 'Vasanthapura', 'Vidyaranyapura',
#                  'Vijayanagar', 'Vishveshwarya Layout', 'Vishwapriya Layout', 'Vittasandra', 'Whitefield',
#                  'Yelachenahalli', 'Yelahanka',
#                  'Yelahanka New Town', 'Yelenahalli', 'Yeshwanthpur']

# loaded_model = pickle.load(open('Banglore_house_price_prediction.sav', 'rb'))


# location = st.selectbox('Select the Location', location_data)
# sqft = st.slider('Total Area in sqft', 1000, 5000, 1800)
# bath = st.slider('Number of Bathrooms', 1, 10, 2)
# bhk = st.slider('Number of Bedrooms', 1, 12, 3)
# data = {'location': location,
#            'sqft': sqft,
#            'bath': bath,
#            'bhk': bhk}
# features = pd.DataFrame(data, index=[0])


# # st.subheader('User Input parameters')
# # st.write(features)

# def predict_price(location, sqft, bath, bhk):
#     loc_index = np.where(X.columns == location)[0][0]

#     x = np.zeros(len(X.columns))
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk
#     if loc_index >= 0:
#         x[loc_index] = 1

#     prediction = loaded_model.predict([x])[0]
#     return prediction


# my_preds = predict_price(location,sqft,bath,bhk)
# st.header("Expected Price:")
# st.subheader(f" {round(my_preds, 4)} ")
# st.divider()
# st.divider()
import requests

r1 = requests.get('https://0419-45-252-78-212.ngrok-free.app/success/himalayara raj ')

print(r1.text)
