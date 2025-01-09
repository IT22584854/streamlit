import streamlit as st

st.title("Stream Demo MCN")

st.header("This is Header")

st.subheader("sub- Header")

if st.checkbox("select"):
    st.success("pit thmi")
else:
    st.warning("select some")

state = st.radio("what is fav color", ("RED", "GREEN", "YELLO"))

if st.button("button"):
    st.selectbox("what do you do", ["st", "navi"])

st.sidebar.header("Heading of sidebar")
st.sidebar.color_picker("Heading of sidebar")