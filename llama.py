import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import CTransformers

# Ctransformers
llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

output_parser = StrOutputParser()

# Chat mode를 사용하기 위해서는 ChatPromptTemplate 라이브러리를 사용해야함.
prompt = ChatPromptTemplate.from_messages([
    # open ai의 경우 한글 지원이 잘되어있어서 한글로 가능하지만
    # llama의 2버전의 경우 한글 지원이 잘 안되어있음 그래서 영문으로 해야됨
    ("system", "You are the best poet in the world. Give me a topic and you have to write a poem."),
    ("user", "{input}")
])

chain = prompt | llm | output_parser

st.title('인공지능 시인')

content = st.text_input('시의 주제를 영어로 제시해주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = chain.invoke({"input": "Write a poem about" + content})
        st.write(result)