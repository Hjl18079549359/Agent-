
# app.py
import sys
import os
import time

# 把项目根目录 E:\code\python 加入模块搜索路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))




import streamlit as st
from Agent.agent.agent.react_agent import ReactAgent

#标题
st.title("智扫通机器人智能客服")
st.divider()

if "agent" not in st.session_state:
    st.session_state["agent"]=ReactAgent()

if "messages" not in st.session_state:
    st.session_state["messages"]=[]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

# 用户输入提示词
prompt=st.chat_input()

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["messages"].append({"role":"user","content":prompt})
    response_messages=[]
    with st.spinner("智能客服思考中..."):
        res_stream=st.session_state["agent"].execute_stream(query=prompt)

        def capture(generator,cache_list):
            for item in generator:
                cache_list.append(item)
                for char in item:
                    time.sleep(0.01)
                    yield char



        st.chat_message("assistant").write_stream(capture(res_stream,response_messages))
        st.session_state["messages"].append({"role":"assistant","content":response_messages[-1]})
        st.rerun()
