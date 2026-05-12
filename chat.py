from llm import get_ai_response
import streamlit as st


from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="소득세 챗봇", page_icon="🤖")
st.title("🤖 소득세 챗봇")
st.caption("소득세에 대한 질문이 있으신가요? 챗봇에게 물어보세요!")

# 앱 처음 실행할 때 딱 한 번만 실행됨
if 'message_list' not in st.session_state:
    st.session_state['message_list'] = []

# message_list에 있는 메시지들을 화면에 출력
for message in st.session_state.message_list:
    with st.chat_message(message["role"]): # 유저
        st.write(message["content"])


if user_question := st.chat_input(placeholder = "소득세에 대해 궁금한 점을 입력해주세요."):
    with st.chat_message("user"):   # 👤 말풍선 열기
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("AI가 답변을 생각하는 중..."):

        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):   
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})
