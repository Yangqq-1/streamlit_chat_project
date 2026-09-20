import streamlit as st
import chat_api
# import ollama

# def get_data(prompt):

    # r = ollama.chat(model="qwen3:14b", messages=[{"role": "user", "content": prompt}], think=False)
# message_array = []
# st.title("智能聊天机器人")
# st.divider()
# 构建聊天窗口
# st.chat_message('assistant').write('你好，我是你的小助手')
# st.chat_message('user').write('你好')
# st.chat_message('assistant').write('有什么可以帮你的')

st.title("智能聊天机器人")
st.divider()
prompt = st.chat_input('开启你的探索')
if 'message_array' not in st.session_state:
    st.session_state.message_array = []

if prompt is not None:
    st.chat_message('user').write(prompt)
    st.session_state.message_array.append(
        {
                "role": "user",
                "content": prompt
        }
    )
    print(st.session_state.message_array, '1.message_array')
    response = chat_api.get_stream_data(st.session_state.message_array)
    print(response, '2.response')
    st.chat_message('assistant').write(response)
    st.session_state.message_array.append({"role": "assistant", "content": response})


    # if prompt is not None:
    #     st.session_state.message_array.append(
    #         {
    #             "role": "user",
    #             "content": prompt
    #         }
    #     )
    #     for item in st.session_state.message_array:
    #         if item['role'] == 'user':
    #             st.chat_message('user').write(item.content)
    #         else:
    #             st.chat_message('assistant').write(item.content)
    #     response = chat_api.get_stream_data(st.session_state.message_array)
    #     st.session_state.message_array.append({"role": "assistant", "content": response})
    #     for item in st.session_state.message_array:
    #         if item['role'] == 'user':
    #             st.chat_message('user').write(item.content)
    #         else:
    #             st.chat_message('assistant').write(item.content)
