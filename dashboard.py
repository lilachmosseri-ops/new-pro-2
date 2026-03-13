import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="דשבורד קטן לדוגמה", layout="wide")
st.title("📊 דשבורד קטן לדוגמה")
st.markdown("ברוך הבא לדשבורד לדוגמה ב-Streamlit!")

# יצירת נתונים לדוגמה
np.random.seed(42)
data = pd.DataFrame({
    'תאריך': pd.date_range('2024-01-01', periods=30),
    'מכירות': np.random.randint(50, 200, 30),
    'הוצאות': np.random.randint(20, 100, 30)
})

# סיכום מהיר
col1, col2, col3 = st.columns(3)
col1.metric("סך הכל מכירות", f"{data['מכירות'].sum():,} ₪")
col2.metric("סך הכל הוצאות", f"{data['הוצאות'].sum():,} ₪")
col3.metric("רווח נקי", f"{(data['מכירות'].sum() - data['הוצאות'].sum()):,} ₪")

# הצגת טבלה
with st.expander("הצג נתונים מפורטים"):
    st.dataframe(data)

# גרף מכירות והוצאות
st.subheader("📈 מכירות והוצאות לאורך זמן")
st.line_chart(data.set_index('תאריך')[['מכירות', 'הוצאות']])
