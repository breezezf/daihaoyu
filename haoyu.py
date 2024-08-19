import streamlit as st
from PIL import Image
import base64
import time
import wordcloud

page=st.sidebar.radio('慈云图书馆',['中国四大名著及外国名著','阅读小能手','图片小帮手','查看书籍','留言区'])
def ciyun(str):
    font="anna.ttf"
    w=wordcloud.WordCloud(width=600,height=400,font_path=font,max_words=50).generate(str)
    w.to_file("ciyun.png")
    img=Image.open("ciyun.png")
    return img
def page1():    
    st.subheader('中国四大名著')
    pol1,pol2=st.columns([2,3])
    with pol1:
        m=":pink[浮生着甚苦奔忙，盛席华宴终散场。]"
        st.write(m)
        st.image("红楼梦.png")
    with pol2:
        n=":red[覆载群生仰至仁，发明万物皆成善。]"
        st.write(n)
        st.image("西游记.png")
    pol3,pol4=st.columns([2,3])
    with pol3:
        l=":blue[滚滚长江东逝水，浪花淘尽英雄。]"
        st.write(l)
        st.image("三国演义.png")
    with pol4:
        k=":green[虚名薄利不关愁，裁冰及剪雪，谈笑看吴钩。]"
        st.write(k)
        st.image("水浒传.png")
    st.write("-------------------")
    st.subheader("外国名著")
    mol1,mol2=st.columns([2,3])
    with mol1:
        st.image("鲁滨逊漂流记.png")
    with mol2:
        st.image("骑鹅旅行记.jpg")   
    st.video('四大名著.mp4')
    
def page2():
    st.subheader('请你检测一下自己对书籍的了解吧！')
    st.write('《西游记》的作者是谁？')
    col1,col2=st.columns([2,3])
    with col1:
        cb1 = st.checkbox('曹雪芹')
    with col2:
        cb2 = st.checkbox('施耐庵')
    col3,col4=st.columns([2,3])
    with col3:
        cb3 = st.checkbox('吴承恩')
    with col4:
        cb4 = st.checkbox('罗贯中')
    if st.button('提交答案'):
        if cb1 == False and cb2 == False and cb3 == True and cb4 == False:
            st.write('回答正确')
        else:
            st.write('回答错误')
    st.write('----------------------')
    st.write('《鲁滨逊漂流记》中，鲁滨逊在孤岛上生活了几年？')
    sd1,sd2=st.columns([2,3])
    with sd1:
        er1 = st.checkbox('28年')
    with sd2:
        er2 = st.checkbox('27年')
    sd3,sd4=st.columns([2,3])
    with sd3:
        er3 = st.checkbox('29年')
    with sd4:
        er4 = st.checkbox('31年')
    if st.button('确认答案'):
        if er1 == True and er2 == False and er3 == False and er4 == False:
            st.write('回答正确')
        else:
            st.write('回答错误')
    st.write('----------------------')
    st.write('《骆驼祥子》中，祥子的职业是什么？')
    dc1,dc2=st.columns([2,3])
    with dc1:
        ear1 = st.checkbox('车夫')
    with dc2:
        ear2 = st.checkbox('鞋匠')
    dc3,dc4=st.columns([2,3])
    with dc3:
        ear3 = st.checkbox('裁缝')
    with dc4:
        ear4 = st.checkbox('环卫工人')
    if st.button('确定答案'):
        if ear1 == True and ear2 == False and ear3 == False and ear4 == False:
            st.write('回答正确')
        else:
            st.write('回答错误')
            
def page3():
    st.subheader(":sunglasses:处理图片,文章:sunglasses:")
    uploaded_file=st.file_uploader("请上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4=st.tabs(["原图","一","二","三"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:    
            st.image(img_change(img,1,0,2))
        with tab4:
            st.image(img_change(img,2,1,0))
    uploaded_font=st.file_uploader("请上传你喜欢的txt文件")
    if uploaded_font is not None:
        str_data=uploaded_font.read().decode("utf-8")
        st.image(ciyun(str_data))
    else:
        pass
        
def page4():
    st.subheader('查找书籍')
    with open('words_space.txt','r',encoding='utf-8')as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    word=st.text_input('请输入要查看的书籍')
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        st.write('查看次数：',times_dict[n])    
    with open('check_out_times.txt','w',encoding='utf-8')as f:
        message=''
        for k,v in times_dict.items():
            message+=str(k)+'#'+str(v)+'\n'
        message=message[:-1]
        f.write(message)
    if word=='西游记':
        u=":red[恭喜你找到隐藏彩蛋！\(^o^)/~]"
        st.write(u)
        st.snow()
        st.balloons()
    st.link_button('鸠摩搜书', 'https://www.jiumodiary.com/')
    st.write('除了鸠摩搜书之外，还有更多的阅读app哦！')
    go = st.selectbox('书籍是人类进步的阶梯！！！', ['中国国家图书馆', '微信读书'])
    if go == '中国国家图书馆':
        st.link_button('点击进入', 'http://www.nlc.cn/')
    elif go == '微信读书':
        st.link_button('点击加载', 'https://weread.qq.com/')

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

bar_bg('天空1.jpg')
page_bg('天空.jpg')

def page5():
    st.subheader('留言区')
    with open('leave_messages.txt','r',encoding='utf-8')as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    for i in messages_list:
        if i[1]=='编程猫':
            with st.chat_message('🦑'):
                st.write(i[1],':',i[2])
        elif i[1]=='代号<・)))><<':
            with st.chat_message('🐡'):
                st.write(i[1],':',i[2])         
    name=st.selectbox('称呼',['代号<・)))><<','编程猫'])
    new_message=st.text_input('分享一下自己的阅读心得吧！')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])      
        with open('leave_messages.txt','w',encoding='utf-8')as f:
            message=''
            for i in messages_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]
            f.write(message)
    
def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()

    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
    
if page=='中国四大名著及外国名著':
    page1()
elif page=='阅读小能手':
    page2()
elif page=='图片小帮手':
    page3()
elif page=='查看书籍':
    page4()
elif page=='留言区':
    page5()
