import streamlit as st
import pandas as pd

with st.sidebar:
    Pages = st.radio(
        "Choose an option",
        ("Form", "CSV Uploader","Image Gallery")
    )
if Pages == "Form":
    st.title("User Informaion Form")
    with st.form("Informaion_Form"):
        name = st.text_input("Enter your Name:")
        age = st.number_input("Enter your Age:",0,120,step=1)
        text = st.text_area("Your FeedBack:")
        agree = st.checkbox('I accept the terms and conditions')
        Gender = st.radio('Gender',["Female","Male","Other"])
        work = st.slider("How many days do you work per week?", min_value=0, max_value=7, value=5)

        submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"Thank you for your submitting, {name}!")
        st.write("Age : ",age)
        st.write("FeedBack : ", text)
        st.write("Gender : ", Gender)
        st.write("Days active per week: ",work)
        if agree:
            st.write("You have accepted the terms and conditions")
        else :
            st.write("Please accept the terms and conditions")

elif Pages == "CSV Uploader":
    st.title("CSV Uploader & Intractive Table")
    File = st.file_uploader("Upload CSV",type =["csv"])
    if File is not None:
        df = pd.read_csv(File)
        df_view = df.copy()
        st.title("Data Table")
        query = st.text_input("Search")
        if query:
            mask = df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)
            df_view = df_view[mask]

            if df_view.empty:
                st.warning("No Result")
        sort_col = st.selectbox("Sort by Column",df_view.columns)
        df_view = df_view.sort_values(sort_col)
        total_rows = len(df)
        if total_rows > 0:
            default_rows = min(20, total_rows)
            show_n = st.slider("Select Page", min_value=1, max_value=min(total_rows,100), value=default_rows)
            st.data_editor(df_view.head(show_n), use_container_width=True)
        else:
            st.data_editor(df_view, use_container_width=True)
    else:
        st.info("Please Choose CSV File")

elif Pages == "Image Gallery":
    st.title("Image Gallery With Batch Upload")
    Image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"],accept_multiple_files=True)
    if Image is not None:
        st.title("Gallery")
        st.image(Image,)



