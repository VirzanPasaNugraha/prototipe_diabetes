"""
Global Theme
"""

import streamlit as st


def apply_theme():

    st.markdown(
        """
<style>

/* ==========================
   GLOBAL
========================== */

.stApp{
    background:linear-gradient(135deg,#F8FAFC,#EEF2FF);
}

.block-container{
    max-width:1200px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* ==========================
   TYPOGRAPHY
========================== */

h1,h2,h3{
    color:#0F172A;
    font-weight:700;
}

p,label{
    color:#475569;
}

/* ==========================
   SIDEBAR
========================== */

[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:1px solid #E2E8F0;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3{
    color:#0F172A;
}

/* ==========================
   BUTTON
========================== */

.stButton button{
    width:100%;
    border:none;
    border-radius:12px;
    background:#2563EB;
    color:white;
    font-weight:600;
    padding:0.65rem 1rem;
    transition:0.25s;
}

.stButton button:hover{
    background:#1D4ED8;
}

/* ==========================
   INPUT
========================== */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"]{
    border-radius:10px;
}

/* ==========================
   CARD
========================== */

.custom-card{
    background:white;
    border-radius:18px;
    padding:22px;
    border:1px solid #E2E8F0;
    box-shadow:0 4px 15px rgba(0,0,0,.05);
    margin-bottom:18px;
}

/* ==========================
   METRIC
========================== */

.metric-value{
    font-size:32px;
    font-weight:700;
    color:#2563EB;
}

.metric-title{
    color:#64748B;
    font-size:14px;
}

/* ==========================
   SUCCESS
========================== */

.success-box{
    background:#ECFDF5;
    border-left:5px solid #22C55E;
    padding:15px;
    border-radius:10px;
}

/* ==========================
   WARNING
========================== */

.warning-box{
    background:#FFFBEB;
    border-left:5px solid #F59E0B;
    padding:15px;
    border-radius:10px;
}

/* ==========================
   ERROR
========================== */

.error-box{
    background:#FEF2F2;
    border-left:5px solid #EF4444;
    padding:15px;
    border-radius:10px;
}

/* ==========================
   DATAFRAME
========================== */

[data-testid="stDataFrame"]{
    border-radius:12px;
    overflow:hidden;
}

/* ==========================
   IMAGE
========================== */

.stImage img{
    border-radius:12px;
}

/* ==========================
   HR
========================== */

hr{
    border:none;
    border-top:1px solid #E2E8F0;
}

/* ==========================
   RESPONSIVE
========================== */

@media (max-width:768px){

.block-container{
    padding-top:1rem;
    padding-left:1rem;
    padding-right:1rem;
}

h1{
    font-size:28px;
}

}

</style>
        """,
        unsafe_allow_html=True,
    )