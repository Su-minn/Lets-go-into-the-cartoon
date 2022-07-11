import io
import time
from PIL import Image
import streamlit as st
from predict import load_model
from confirm_button_hack import cache_on_button_press


# SETTING PAGE CONFIG TO CENTER MODE
st.set_page_config(
    page_title="Leggo Cartoon!",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

root_password = "cartoon"


def visualize_image(uploaded_file):
    model, face2paint = load_model()

    if uploaded_file:
        image_bytes = uploaded_file.getvalue()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        st.image(image, width=500, caption="만화 속으로 들어갈 사진입니다 !")
        converted_img = face2paint(model, image)
        placeholder = st.empty()
        with placeholder:
            for i in range(1, 6):
                space = "\u00A0" * 3
                st.write("")
                st.write("만화 속으로 이동 중입니다" + f"{space}🐕{space}" * i)
                time.sleep(0.3)

        st.image(converted_img, caption="만화 속으로 들어간 사진입니다 !")
        st.balloons()


def main():
    st.write("")
    st.subheader("만화 속으로 들어갈 사진을 넣어주세요!")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    visualize_image(uploaded_file)


@cache_on_button_press("만화 속으로 떠날 준비가 되셨다면 클릭해주세요 🤸‍♂️")
def authenticate(password: str) -> bool:
    return password == root_password


st.title("Lets go into the cartoon ! 😎\n  by Jussuit")
password = st.text_input("🔐  PASSWORD 를 입력해주세요", type="password")

if authenticate(password):
    st.success("🐥 환영합니다 🐥" + "\u00A0" * 5 + "함께 만화 속으로 떠나볼까요?")
    main()
else:
    st.error("비밀번호를 다시 확인해주세요 💦")
