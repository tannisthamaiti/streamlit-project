import streamlit as st
from streamlit_option_menu import option_menu
#import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
#import streamlit.components.v1 as components
import base64
from streamlit_text_rating.st_text_rater import st_text_rater



def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
        
        

col1, col2,col3= st.columns(3)
with col1:  
    if st.button('Read PDF Tutorial',key='1'):            
        show_pdf('SH R-1H1_Merged_diff.pdf')
            
           