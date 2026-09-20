# 打开
# open(路径, 模式，文件编码)
# name: 路径。相对路径/绝对路径 r'xx\xxx\xxxx' 加r代表/分隔符，没有其他特殊含义
# mode：模式。
#   r和rb: 文件必须存在；
#   w和wb：写数据到文件，如果文件不存在先创建再写入，存在即直接使用
#   a和ab：追加写数据到文件，如果文件不存在先创建再写入，存在即直接使用
# 文件编码
#   utf8: 万国码 通用最常用
#    gbk：主要针对中文的国际标准扩展

f = open('test.txt', 'w')
# f = open('/Users/Admin/Desktop/LLM_Learn/python_project/python04/10_try_except_else_finally完整格式.py', 'r')
print(f) # <_io.TextIOWrapper name='test.txt' mode='w' encoding='UTF-8'>
