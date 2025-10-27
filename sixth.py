import streamlit as st

st.set_page_config(page_title="个人简历生成器", page_icon="🈸", layout="wide")


c1,c2 =st.columns([1,2])
with c1:
    st.subheader('个人信息表单')
    name = st.text_input('姓名', autocomplete='name')

    career = st.text_input('职位', autocomplete='name')

    phone = st.text_input('电话', autocomplete='name')

    email = st.text_input('邮箱', autocomplete='name')
    dob = st.date_input("出生日期", value=None)
from datetime import datetime, timedelta    
  
gender = st.radio(
        '你的性别',['男', '女'],
        horizontal=True,
        label_visibility='hidden')

st.text('学历')
degrees = st.selectbox(
    '选择学历',
    ['高中', '专科', '本科','硕士','博士',],
    label_visibility='collapsed'
)

st.text('身份')
identity = st.selectbox(
    '选择身份',
    ['法师', '游走', '战士','打野','射手',],
    label_visibility='collapsed'
)

introduce = "北方草原的狼旗诸部因环境严苛常南下侵扰中原，中原诸侯以和亲等方式换取和平，王昭君作为和亲公主被送往凛冬之海献祭给神明"\
            "后来，中原强国违背盟,，趁狼旗诸部举行祭典时发动袭击，史称“血色婚礼”。将军们还觊觎冰川中的宝物，结果引发暴风雪和雪崩"\
            "王昭君则在幸存狼旗人的簇拥下成为了他们的公主。"

st.text_area(label='背景故事: ', value=introduce,
            height=200, max_chars=200)

skill = "被动技能“冰封之心”让王昭君脱战后获得寒冰护盾，护盾破裂或普攻可对敌人施加冰冷效果。" \
            "一技能“凋零冰晶”可对指定区域敌人造成法术伤害并施加冰冷效果，同时获得目标视野" \
            "二技能“禁锢寒霜”能冰冻范围内敌人，对冰冻敌人还会额外造成伤害。" \
            "大招“凛冬已至”可召唤暴风雪，对范围内敌人持续造成伤害与冰冷效果，召唤时会刷新寒冰护盾。"
st.text_area(label='技能介绍：', value=skill,
            height=200, max_chars=200)

photo=st.file_uploader('上传个人照片')
if photo is not None:
    bytes_data=photo.getvalue()

with c2:
    st.subheader('简历实时预览')
    a1,a2 = st.columns([1, 2])
    with a1:
        if photo:
            st.image(photo,width=300)
        st.write('',name)
        st.write('职位：',career)
        st.write('电话：',phone)
        st.write('邮箱：',email)
        st.write('出生日期：',dob)
            
    with a2:
        st.write('学历：',degrees)
        st.write('身份：',identity)
        st.write('性别：',gender)
        st.title('个人简介')
        st.write('',introduce)

        st.title('技能介绍')
        st.write('',skill)


