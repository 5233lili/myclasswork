import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv("student_data.csv")

model = joblib.load("score_predictor.pkl")

st.set_page_config(
    page_title="学生成绩分析与预测系统", page_icon="🗊", layout="wide",)

with st.sidebar:
    st.title('导航菜单')
    page = st.radio(
        "选择页面",
        ("项目介绍", "专业数据分析", "成绩预测")
    )

if page == "项目介绍":
    st.title("👩‍🎓学生成绩分析与预测系统")

  
    st.header('📝项目概述')
    st.text('本项目是一个基于streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。')
    st.subheader('主要特点')
    st.markdown('◼️**📊数据可视化：多维度展示学生学业数据**')
    st.markdown('◼️**🎯专业分析：按专业分类的详细统计分析**')
    st.markdown('◼️**🎲智能预测：基于机器学习模型的成绩预测**')
    st.markdown('◼️**💡学习建议：根据预测结果提供个性化反馈**')
   

    st.header('🚀项目目标')
    c1,c2,c3 =st.columns(3)
    with c1:
        st.subheader('🎯目标一')

        st.text('分析影响因素')
        st.text('◼️识别关键学习指标')
        st.text('◼️探索成绩相关因素')
        st.text('◼️提供数据支持决策')

    with c2:
        st.subheader('🛠目标二')

        st.text('可视化展示')
        st.text('◼️专业对比分析')
        st.text('◼️性别差异研究')
        st.text('◼️学习模式识别')

    with c3:
        st.subheader('🔮目标三')

        st.text('成绩预测')
        st.text('◼️机器学习模型')
        st.text('◼️个性化预测')
        st.text('◼️及时干预预警')

    st.subheader('🕹技术架构')

    a1,a2,a3,a4 =st.columns(4)

    with a1:
        st.text('前端架构')
        st.code('streamlit')
    with a2:
        st.text('数据处理')
        python_code1='''pandas
numpy
                     '''
        st.code(python_code1, language=None)    
    with a3:
        st.text('可视化')
        python_code2='''plotly
matplotlib
               '''
        st.code(python_code2, language=None) 
    with a4:
        st.text('机器学习')
        st.code('scikit-learn')

elif page == "专业数据分析":
    st.title("📊专业数据分析")
    st.subheader('性别比例统计表')

    df = pd.read_csv('student_data.csv', encoding='utf-8')
    col1, col2 = st.columns(2)
    with col1:
        # 按专业和性别分组统计人数
        grouped_data = df.groupby(['专业', '性别'])['学号'].count().reset_index(name='人数')
        # 计算每个专业的总人数
        total_by_major = grouped_data.groupby('专业')['人数'].transform('sum')
        # 计算男女比例（保留两位小数）
        grouped_data['男女比例(%)'] = (grouped_data['人数'] / total_by_major * 100).round(2)
        # 将数据转换为透视表格式，便于展示
        pivot_data = grouped_data.pivot(index='专业', columns='性别', values='男女比例(%)')
        # 使用 st.bar_chart 展示柱状图
        st.bar_chart(pivot_data)

    with col2:
        # 展示各专业男女比例表格
        st.write('各专业男女比例：')
        st.dataframe(pivot_data)   

    st.title('各专业平均期末考试分数')
    col1, col2 = st.columns(2)
    with col1:
        # 按专业分组计算平均期末考试分数，并保留两位小数
        grouped_data = df.groupby('专业')['期末考试分数'].mean().round(2).reset_index()
        # 将数据框设置为以"专业"为索引，方便绘制柱状图
        bar_chart_data = grouped_data.set_index('专业')
        # 使用 st.bar_chart 展示柱状图
        st.bar_chart(bar_chart_data)

    with col2:
        # 将表格横向展示并在 Streamlit 中显示
        st.write('各专业平均期末考试分数：')
        st.dataframe(grouped_data.set_index('专业').T)
    st.subheader('3.各专业出勤率分析')
    f1, f2 = st.columns([2,1])
    with f1:
         attendance_fig = px.density_heatmap(df, x="专业", y="上课出勤率",
                                           title="各专业出勤率分布",
                                           labels={"专业": "专业", "上课出勤率": "出勤率"})
         st.plotly_chart(attendance_fig, use_container_width=True)
    with f2:
        attendance_rank = df.groupby("专业")["上课出勤率"].mean().reset_index().sort_values("上课出勤率", ascending=False)
        attendance_rank["排名"] = attendance_rank["上课出勤率"].rank(ascending=False).astype(int)
        st.subheader("出勤率排名")
        st.dataframe(attendance_rank[["排名", "专业", "上课出勤率"]], use_container_width=True)


    st.markdown('***')
    st.subheader('4.大数据管理专业专项分析')
    bd_major = df[df["专业"] == "大数据管理"]
    # 关键指标卡片
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("平均出勤率", f"{bd_major['上课出勤率'].mean():.1%}")
    with col2:
        st.metric("期中成绩", f"{bd_major['期中考试分数'].mean():.1f}分")
    with col3:
        st.metric("期末成绩", f"{bd_major['期末考试分数'].mean():.1f}分")
    with col4:
        st.metric("平均学习时长", f"{bd_major['每周学习时长（小时）'].mean():.1f}小时")
    # 图表
    col1, col2 = st.columns(2)
    with col1:
        bd_score_fig = px.histogram(bd_major, x="期末考试分数", title="大数据管理专业期末成绩分布")
        st.plotly_chart(bd_score_fig, use_container_width=True)
    with col2:
        bd_hours_fig = px.box(bd_major, y="每周学习时长（小时）", title="大数据管理专业学习时长分布")
        st.plotly_chart(bd_hours_fig, use_container_width=True)        

else:
   st.title("⛳️ 期末成绩预测系统")
   st.markdown("通过输入学生的学习特征，系统将基于机器学习模型预测期末成绩并提供个性化建议")
   st.markdown("---")

   with st.form("predict_form", clear_on_submit=False):
       st.subheader("📓 学生学习信息录入")
       col1, col2 = st.columns(2)
       with col1:
            student_id = st.text_input("学号", placeholder="例如：2023001001")
            gender = st.selectbox("性别", ["男", "女"])
            major = st.selectbox("专业", df["专业"].unique())
            study_hours = st.slider(
                "每周学习时长（小时）",
                min_value=0.0, max_value=50.0, step=0.5, value=15.0,
                help="学生平均每周投入学习的时长"
                )
            with col2:
                attendance = st.slider(
                    "上课出勤率",
                    min_value=0.0, max_value=1.0, step=0.01, value=0.8,
                    help="实际出勤课时/应出勤课时"
                    )
                mid_score = st.slider(
                    "期中考试分数",
                    min_value=0.0, max_value=100.0, step=1.0, value=70.0
                    )
                homework_rate = st.slider(
                    "作业完成率",
                    min_value=0.0, max_value=1.0, step=0.01, value=0.9,
                    help="已完成作业数/总作业数"
                    )
            submit_btn = st.form_submit_button("🔍 预测期末成绩", type="primary")
            if submit_btn and student_id:
                X = [[study_hours, attendance, mid_score, homework_rate]]
                pred_score = model.predict(X)[0]
                pred_score = max(0, min(100, round(pred_score, 1))) 
                st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
                st.subheader(f"🧑‍🎓 学号 {student_id} 的预测结果")
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown(f'<div class="result-highlight">{pred_score} 分</div>', unsafe_allow_html=True)
                with col2:
                    st.progress(pred_score / 100) 
                    if pred_score >= 90:
                        st.success("💯 成绩等级：优秀")
                        st.image("6.png", width=200)
                    elif pred_score >= 80:
                        st.success("🤩 成绩等级：良好")
                        st.image("7.png",width=200)
                    elif pred_score >= 60:
                        st.info("🈴 成绩等级：合格")
                        st.image("5.png", width=200)
                    else:
                        st.warning("☹️ 成绩等级：待提高")
                        st.image("4.png", width=200)
                    st.markdown('<div class="advice-box">', unsafe_allow_html=True)
                    st.subheader("💡 学习建议")
                if attendance < 0.7:
                    st.markdown("- 建议提高出勤率，课堂互动对平时成绩影响显著")
                if homework_rate < 0.8:
                    st.markdown("- 需加强作业完成质量，作业是巩固和复习知识的关键")
                if study_hours < 10:
                    st.markdown("- 建议增加每周学习时长，保证足够的知识消化时间")
                if pred_score < 60:
                    st.markdown("- 可针对性复习期中考试薄弱环节，及时寻求老师帮助")
                else:
                    st.markdown("- 保持当前学习状态，建议定期总结知识体系，查漏补缺")
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

            elif submit_btn:
                pass





