import streamlit as st
import chat_api

st.title("智能聊天机器人")
st.divider()
prompt = st.chat_input('开启你的探索')
if 'message_array' not in st.session_state:
    st.session_state.message_array = []
# 先渲染历史
for message in st.session_state.message_array:
    st.chat_message(message['role']).write(message['content'])

if prompt is not None:
    st.chat_message('user').write(prompt) # 渲染user气泡
    st.session_state.message_array.append({'role': 'user', 'content': prompt})
    with st.spinner("思考中......"):
        res_data = chat_api.get_stream_data(st.session_state.message_array)
    st.chat_message('assistant').write(res_data) # 渲染响应气泡
    # print(res_data)
    # written = st.write_stream(res_data)
    st.session_state.message_array.append({'role': 'assistant', 'content': res_data})