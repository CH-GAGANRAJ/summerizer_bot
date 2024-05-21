
from transformers import pipeline
import streamlit as st
summerizer=pipeline('summarization',model="Falconsai/text_summarization")
st.header('SUMMERIZER BOT')
with st.chat_message('assistant'):
      st.write('Hi Iam Your personal summerizer')

text=str(st.chat_input('GIVE THE SUMMERY'))
            #submit=st.form_submit_button('Submit')

task=text
op=summerizer(task,max_length=100,min_length=10,do_sample=False)
st.write('YOUR SUMMARY')
with st.chat_message('user'):
      st.write(text)
with st.chat_message('assistant'):
      for i in op[0]['summary_text'].split('.'):
            st.write('*',i)







