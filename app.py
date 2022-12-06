import streamlit as st
import joblib
from PIL import Image
import pickle

filename = "Completed_model.joblib"
#model = pickle.load(open('./Model/ML_Model.pkl', 'rb'))

model = joblib.load(filename)


def run():
    #img1 = Image.open('bank.png')
    #img1 = img1.resize((156,145))
    #st.image(img1,use_column_width=False)
    st.title("Flight delay prediction")

    ## DAY_OF_MONTH
    DAY_OF_MONTH = st.text_input('DAY OF MONTH')

    ## DAY_OF_WEEK
    DAY_OF_WEEK = st.text_input('DAY OF WEEK')

    ## For OP_UNIQUE_CARRIER
    gen_display = (1, 14, 12, 15, 13,  3,  0,  2,  5,  9,  4,  6, 11,  7, 16,  8, 10) #ken kharjet erreur rodhom string
    gen_options = list(range(len(gen_display)))
    OP_UNIQUE_CARRIER = st.selectbox("CARRIER",gen_options, format_func=lambda x: gen_display[x])

    ## For ORIGIN
    #mar_display = ('No','Yes')
    #mar_options = list(range(len(mar_display)))
    #mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    ORIGIN=st.text_input('ORIGIN')



    ## DEST
    #dep_display = ('No','One','Two','More than Two')
    #dep_options = list(range(len(dep_display)))
    #dep = st.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])

    DEST=st.text_input('DEST')


    ## For DEP_TIME
    #edu_display = ('Not Graduate','Graduate')
    #edu_options = list(range(len(edu_display)))
    #edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    DEP_TIME=st.text_input('DEP_TIME')



    ## For DEP_TIME_BLK
    #emp_display = ('Job','Business')
    #emp_options = list(range(len(emp_display)))
    #emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

    
    Time_blk_display = (1, 14, 12, 15, 13,  3,  0,  2,  5,  9,  4,  6, 11,  7, 16,  8, 10) #ken kharjet erreur rodhom string
    blk_options = list(range(len(Time_blk_display)))
    DEP_TIME_BLK = st.selectbox("DEP_TIME_BLK",blk_options, format_func=lambda x: blk_options[x])



    ## For ARR_TIME
    ARR_TIME=st.text_input('ARR_TIME')

    ## For DISTANCE
    DISTANCE=st.text_input('DISTANCE')

    

    if st.button("Submit"):
        
        features = [[DAY_OF_MONTH, DAY_OF_WEEK, OP_UNIQUE_CARRIER, ORIGIN, DEST,DEP_TIME, DEP_TIME_BLK, ARR_TIME, DISTANCE]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Dear traveler, welcome to Turkich&Mimi airlines. We regret to inform you that your flight will be delayed"
            )
        else:
            st.success(
                "Dear traveler, welcome to Turkich&Mimi airlines. Your flight will be in time."
            )

run()