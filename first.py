import streamlit as st


st.title("学生小林—档案🗎")
st.header("基础信息")
st.markdown('''姓名：小林👧
            
        年级：高一3班
            
        学号：20250312
            
        兴趣特长：校园播音员、硬笔书法、乒乓球女队队员''')


st.header("学业能力矩阵📊")
#定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="语文", value="95%", delta="-1%")
c2.metric(label="数学", value="95%", delta="+2%")
c3.metric(label="英语", value=None, delta="0",delta_color="off")


st.markdown("任务日志")
st.markdown('''
| 日期 | 任务 | 进度 | 难度 |
| :-: | :-: | :-: | :-: |   
| 2025/9/30 | 写作文     | ✅完成|⭐⭐⭐ |
| 2025/10/30| 写数学卷子 | ✅完成| ⭐⭐   |
| 2025/11/30| 打乒乓球   | ✅完成| ⭐⭐   |''')

st.header("🍎最新代码成果")

str ='''
def matrix_breach():
    while True:
       if detect_vulmerability():
          exploit()
          return "ACCESS GRANTED"
else:
    stealth_evade()
'''

st.code(str,language=None)
st.caption('这是Python代码')
st.code(str,language="python", line_numbers=True)


