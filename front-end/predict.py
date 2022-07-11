import torch
import streamlit as st
from typing import Tuple


@st.cache
def load_model(pretrained: str = "face_paint_512_v2") -> Tuple:
    model = torch.hub.load(
        "bryandlee/animegan2-pytorch:main", "generator", pretrained=pretrained
    )
    face2paint = torch.hub.load(
        "bryandlee/animegan2-pytorch:main", "face2paint", size=512
    )
    return model, face2paint
