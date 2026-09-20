import streamlit as st
#
# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")


# message = st.chat_message("assistant")
# message.write("Hello human")
# message.bar_chart(np.random.randn(30, 4))
# message.info("Hello human")
# message.button('a')

st.title('传智平台')
st.divider()
name = st.text_input("请输入用户名")
pwd = st.text_input("请输入密码", type="password")
h = st.number_input("请输入身高", min_value=0, max_value=100)
w = st.number_input("请输入体重", min_value=0, max_value=100)
a = st.number_input("请输入年龄", min_value=0, max_value=100)
r = st.date_input('日期')
x = st.selectbox('性别', ["男","女"])
result = st.button('确认')
if result:
    st.write('录入成功')
    with open('users.txt', 'a') as f:
        f.write(f"{name}\n,{pwd}\n,{h}\n,{w}\n,{a}\n,{r}\n,{x}\n")
    # print(result, name)