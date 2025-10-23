import streamlit as st

st.set_page_config(page_title='动物园', page_icon='🐨')

# 图片对象数组
images = [
    {'url': 'https://wallpapers.com/images/hd/flamingo-pictures-h9yrjvl6rdc9tva2.jpg',
     'parm': '鸟'
     },
    { 'url': 'https://www.animalspot.net/wp-content/uploads/2017/08/Penguin.jpg',
      'parm': '企鹅 '
     },
    {
      'url':    'https://images2.alphacoders.com/716/71660.jpg',
      'parm': '猫'
      }
]

# st.image()总共两个参数，url：图片地址 caption:图片的备注
if 'ind' not in st.session_state:
    st.session_state['ind'] =0

    
def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] -1) % len(images)
    st.session_state['ind'] = (st.session_state['ind'] -1) % len(images)

st.image(images[st.session_state['ind']]['url'], caption=images[st.session_state['ind']]['parm'])

#将一行分两列
c1, c2 = st.columns(2)

with c1:
    st.button('上一张', on_click=nextImg, use_container_width=True)

with c2:
  
    st.button('下一张', on_click=nextImg, use_container_width=True)

