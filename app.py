import streamlit as st

st.text("trfugy io")

def somma(l1:float,l2:float):
    a=l1+l2
    return a
def main():
    st.text("Ciao")
    num1=st.slider("inserisci lato1 rettangolo",0,100,2)
    num2=st.slider("inserisci lato1 rettangolo",0,100,3)
    r=somma(num1,num2)

    st.write("la somma è", r)

if __name__=="__main__":
    main()