import streamlit as st
from PIL import Image
import datetime as dt

st.set_page_config(page_title = "🎅 Secret Santa 🎅")

date_string = "3 January, 2021"
new_day = dt.datetime.strptime(date_string, "%d %B, %Y")
if new_day < dt.datetime.now():
    with st.beta_expander("It's been 3 days, click to see the answer! Or just continue with the puzzle :)"):
        st.write("__username__: `sveyn`")
        st.write("__password__: `hy@mJy52C@46B*`")

params = st.experimental_get_query_params()

if params:
    if 'book' in params['answer']:
        st.title("Wow you made it! Hi!!!")
        text = st.text_input("What is your name")
        if text:
            if "sveyn" in text.lower():
                new_answer = st.text_input("'Earth' in Greek")
                if new_answer:
                    if new_answer.lower() == 'geo':
                        newest = st.text_input("CATCH me if you can!")
                        if newest:
                            if 'cach' in newest.lower():
                                put = st.text_input("Put them together and you get ...")
                                if put:
                                    if "geocach" in put.lower():
                                        caught = st.button("Catch me here")
                                        if caught:
                                            st.image('bitwarden.png')
                                            st.balloons()
                                    else:
                                        st.error("You know what to do...")
                                        st.stop()
                            else:
                                st.error("Try again")
                                st.stop()
                    else:
                        st.error("Try again")
                        st.stop()
            else:
                st.warning(f"GIT out of here'{text.upper()}'")
                st.stop()

    if 'bitwarden' in params['answer']:
        st.title("Hi.")
        text = st.text_input("What is your name")
        if text:
            if "sveyn" in text.lower():
                st.write("## Congratulations on your brand NEW THING!!")
                col1, col2 = st.beta_columns([1,2])
                with col1:
                    st.image('kyle.png',use_column_width=True)
                with col2:
                    st.image('mexcity.png',use_column_width=True)
                st.balloons()
                mex = st.text_input("fave to be?")
                if mex:
                    if "yes" in mex.lower():
                        st.write("Amazing")
                        st.image("password2.png")
            else:
                st.warning("GIT GIT GIT!")
    elif "lastpass" in params['answer'].lower():
        st.error("lol")
else:
    st.info("No params? Gitoutta here...")