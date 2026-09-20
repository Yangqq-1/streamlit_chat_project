# python中的ollama模块连接本地ollama模型

import ollama
# 连接本地ollama软件
client = ollama.Client('127.0.0.1:11434')
def get_stream_data(message):
    # 选择模型及角色
    res = client.chat(
        model = "qwen3:14b",
        messages = message[-20:],
        think = False,
        stream = False
    )
    # print(res.message.content)
    return res.message.content

if __name__ == "__main__":
    msg = '执行中...'
    print(msg)
    get_stream_data([
        {
            "role": "user",
            "content": "讲个笑话",
        }
    ])
    msg = ''
    print('执行结束')

