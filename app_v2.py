from api_llm import gpt_call
from api_repli import repli_call
from fetch_image import fetch_photo
import streamlit as st 


# Look into the Streamlit Tutorials for indepth knowledge
if 'btn_pressed' not in st.session_state:
    st.session_state['btn_pressed'] = False


def get_src_original_url(query):
    reponse = fetch_photo(query)
    if(reponse[0] == 0):
        return reponse[1]
    else:
        st.write(reponse[1])

    return None

st.set_page_config(layout="wide")

def main():
    st.title("Article Generator App using Llama 2")
    options = ['LLAMA2','GPT2']
    page = st.radio('Select the model : ',options)
    btn = st.button("Submit")
    user_inp_context = user_input = ''
    
    if btn:
        st.session_state['btn_pressed'] = True
    if  st.session_state['btn_pressed']:
        user_input  = st.text_input("Please enter the idea/topic for the article you want to generate!")
        image_input = user_input
        different_topic = st.checkbox("Are the image and Article topic Different?")
        
        # Only if the Topic you want the image on about is different from the Article topic
        if different_topic:
            image_input = st.text_input("Please enter the topic for the image you want to fetch!")
            
        if (page == 'GPT2'):
            user_inp_context = st.text_input("Please enter the context for the article you want to generate!",
                                                placeholder='Recommended for better Results')
    
    if len(user_input) > 0 and len(image_input) > 0:
        # if (page == 'GPT2') and (len(user_inp_context) == 0):
        #     st.warning("The output may not be as expected")

        col1, col2= st.columns([1,2])

        with col1:
            st.subheader("Generated Content by ChatGPT 2")
            st.write("Topic of the article is: " + user_input)
            st.write("Image of the article is: " + image_input)

            result = ""
            if(page == "GPT2"):
                result = gpt_call(user_inp_context)
            else:
                result = repli_call(user_input)

            if len(result) > 0:
                st.info("Your article has been been generated successfully!")
                st.write(result)
            else:
                st.error("Your article couldn't be generated!")

        with col2:
            st.subheader("Fetched Image")
            image_url = get_src_original_url(image_input)
            st.image(image_url)




if __name__ == "__main__":
    main()