import time
from gtts import gTTS
import speech_recognition as sr
import os
import streamlit as st


st.title("SELAMAT DATANG DAN UCAPKAN PERINTAH ")
st.write("\t\t\tKLIK TOMBOL DAN UCAPKAN PERINTAH ")
engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ""

Klik_masuk= st.button('KLIK LALU UCAPKAN PERINTAH UNTUK MENGHIDUKAN ATAU MEMATIKAN ELEKTRONIK ANDA')
if Klik_masuk:
    with mic as source:
        st.warning("silahkan berbIcara", icon="⚠️")
        rekaman = engine.listen(source)
        with st.spinner('Sedang si proses...'):
            time.sleep(5)
        st.info('SELESAI..!')

    try:
        hasil =engine.recognize_google(rekaman,language='id-ID')
        st.error(hasil)
        if(hasil == "turn on lamp" or hasil == "Turn on lamp"):
            st.success(" lampu telah di hidupkan ")
            
        if(hasil == "Turn off lamp" or hasil == "turn off lamp"):
            st.success(" lampu telah di di matikan ")
            
        if(hasil == "Turn on AC" or hasil == "turn on AC"):
            st.success(" ac telah di hidupkan ")
            
        if(hasil == "Turn off AC" or hasil == "turn off AC"):
            st.success(" ac telah di matikan ")
            
        if(hasil == "Turn on printer" or hasil == "turn on printer"):
            st.success(" printer telah dinyalakan ")
        
        if(hasil == "Turn off printer" or hasil == "turn off printer"):
            st.success(" printer telah di matikan ")
            
        if(hasil == "turn on TV" or hasil == "Turn on TV"):
            st.success(" tv berhasil di nyalakan ")
            
        if(hasil == "turn off TV" or hasil == "Turn off TV" or hasil == "turn off tv"):
            st.success(" tv berhasil di matikan ")
                
    except engine.UnknowValueEror:
        st.error("maaf tidak di ketahui, mohon ulangi")
    except Exception as e:
        e = RuntimeError('This is an exception of type RuntimeError')
        st.exception(e)
