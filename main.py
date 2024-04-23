import os

# !!!!!!!!!! 로컬로 테스트 할 땐 아래 코드 주석을 해제해야함 !!!!!!!!!!
# from dotenv import load_dotenv
# load_dotenv()

# 환경 변수가 올바르게 로드되었는지 확인
api_key = os.getenv('OPENAI_API_KEY')

# if api_key is None:
#     print("API key is not loaded. Check your .env file and variable name.")
# else:
#     print("API key loaded successfully.")

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(openai_api_key=api_key)

output_parser = StrOutputParser()

# Chat mode를 사용하기 위해서는 ChatPromptTemplate 라이브러리를 사용해야함.
prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 세계 최고의 시인이야 주제를 주면 너는 시를 작성해줘야해"),
    ("user", "{input}")
])

chain = prompt | llm | output_parser

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = chain.invoke({"input": content + "에 대한 시를 써줘"})
        st.write(result)