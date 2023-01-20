import json
import streamlit as st
import pandas as pd
import requests
from PIL import Image
from streamlit_lottie import st_lottie
import webbrowser

# The code below is for the layout of the page
st.set_page_config(  # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
    page_title='Venkata_Bhargavi_Sikhakolli',  # String or None. Strings get appended with "• Streamlit".
    page_icon= None,  # String, anything supported by st.image, or None.
)
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# st.set_page_config(page_title="My Tabs", page_icon=":guardsman:", layout="wide")

tab_styles = """
.stTab {
    font-size: 36px;
}
"""
# st.set_page_config(page_title="My Tabs", page_icon=":guardsman:", layout="wide") #css=tab_styles,unsafe_allow_html=True)

# home, work_ex, pro, blog, skills, about, contact = st.tabs(["Home", "Work Experience", "Project", "Blog", "Skills", "About", "Contact"])
home,work_ex, pro, Blog,skills,about,contact = st.tabs(["🏠 Home","👩‍💻 Work Experience", "⚙ ️Project", "✍️ Blog","🤹🏽 Skills","🧑 About","📞 Contact"]   )
# below code works when clicked home
with home:
    col1, col2 = st.columns([1, 1])
    # col1  in home
    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("<h1 style='font-size: 60px; text-align: center'>Hi, I'm Bhargavi</h1>", unsafe_allow_html=True)
        st.markdown("")
        st.markdown(
            "<p style='font-size: 20px; text-align: center'>This portfolio is a collection of my work and achievements, showcasing my <span style='color: orange;'>skills</span> and abilities in my field of expertise. Here you will find a variety of <span style='color: orange;'>projects</span>, case studies, and other examples of my <span style='color: orange;'>work</span>. I hope you find it informative and I would be glad to discuss any of the works presented here. Thank you!</p>",unsafe_allow_html=True)
        # res_button = st.button("SEE MY RESUME")
    def open_link(url):
        webbrowser.open_new_tab(url)
    res_col,link_col = st.columns([1,8]) #columns for buttons
    with res_col:
        res_url = "https://drive.google.com/file/d/1YthW-l6dMbe7YmnFPKhNIWiixroTNdaA/view?usp=sharing"
        res_button = st.button("SEE MY RESUME")
        if res_button:
            open_link(res_url)
    with link_col:
        linkedin_url = "https://www.linkedin.com/in/bhargavi-sikhakolli-9ab281117/"
        linkedin_button = st.button("LINKEDIN")
        if linkedin_button:
            open_link(linkedin_url)

    # col 2 in home
    with col2:
        st.markdown("")
        st.markdown("")
        lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_rdkbjlef.json")
        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            height="450px",
            width=None,
            key=None,
        )


with work_ex:
    # st.markdown('Streamlit is **_really_ cool**.')
    # st.markdown("This text is: red[colored red], and this is **:blue[colored] ** and bold.")
    # st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
    st.subheader("Work Experience")
    st.markdown("<p style='font-size: 20px'>Below is my work experience, including full-time positions and internships, where I had the opportunity to learn about the latest AI products, technologies, and advancements in various research fields.</p>", unsafe_allow_html=True)
   # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
#     data = {"Company":['<font size="6">BUDDI AI a Claritrics Company</font>,', '<font size="6">BUDDI AI a Claritrics Company</font>', '<font size="6">Continental Automotive India Pvt Ltd</font>',
#              '<font size="6">ConfirmTKT</font>',],
#             "Job Title":['<font size="6">Research Engineer</font>', '<font size="6">Intern</font>', '<font size="6">Research Intern in AIR Labs</font>',
#              '<font size="6">Android Developer Intern</font>'],
#             "Description": ["""<font size="6">– Researched on extracting named entities i.e NER from Electronic Health Records leveraging BILSTM and CRF models resulting in a 30% reduction in medical coding costs.
# – Devised a more advanced ensemble model for Named Entity Recognition in conversational medical text, using BioBert as a reference model and incorporating contextual information, resulted in a 40% increase in precision compared to previously trained generic models
# – Guided a team of 3 in a research project comparing BERT-based algorithms and provided knowledge transfer sessions</font>""", '<font size="6">30</font>', '<font size="6">Chicago</font>',
#              '<font size="6">Engineer</font>'],
#             "Certificates": ['<font size="6">Mike</font>', '<font size="6">28</font>', '<font size="6">Houston</font>',
#              '<font size="6">Data Analyst</font>']
#     }

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")


    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.image("Utils/Images/buddi.png")

    with col2:
        st.image("Utils/Images/conti.png")

    with col3:
        st.image("Utils/Images/confirmtkt.png")

        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
    data = {"Company": ["BUDDI AI - a Claritrics Company",
                        'BUDDI AI - a Claritrics Company',
                        'Continental Automotive India Pvt Ltd',
                        "ConfirmTKT", ],
            "Job Title": ['Research Engineer', 'Intern',
                          'Research Intern in AIR Labs',
                          'Android Developer Intern'],
            "Description": ["""– Researched on extracting named entities i.e NER from Electronic Health Records leveraging BILSTM and CRF models resulting in a 30% reduction in medical coding costs.
    – Devised a more advanced ensemble model for Named Entity Recognition in conversational medical text, using BioBert as a reference model and incorporating contextual information, resulted in a 40% increase in precision compared to previously trained generic models
    – Guided a team of 3 in a research project comparing BERT-based algorithms and provided knowledge transfer sessions""",
                            """– Developed an interactive command-line tool for conducting statistical analysis on numerical data using Scala and SMILE (Statistical Machine Intelligence and Learning Engine) package. 
– Tool allows users to select specific features for analysis and perform a variety of operations, such as mean, median and standard deviation""", """– Synthetic Voice Emotion Generation – A data generator to generate voice of multiple emotions other than input voice, it is intended to completely reduce manual efforts in collecting data from individuals
– The generator is trained on a CycleGAN model using voice data of different emotions and generates synthetic data  that can be consumed by computer vision researchers in model training. The model’s generated voices are ~75% in comparison to human voices
– Created a UI in python to execute image processing operations and displays processed histograms and translated images in widgets""",
                            """– Created a user-friendly interface for a recharge module by utilizing API calls and seamlessly integrating with a payment portal.
– Leveraged XML in Android Studio to design and develop the interface for the recharge module.
– Utilized Java programming language to execute API calls, integrate with the payment portal, and implement shared preferences"""],

            }

    df = pd.DataFrame(data)

    certi =  [
                     "[Experience Certificate](https://drive.google.com/file/d/1f-DeitZtOxD3Xp8a9-q0fVTx8GJIuKqP/view",
                     "[Internship Certificate](https://drive.google.com/file/d/1wkhYExQQ4j4CFlyMwBvJyaoEHfP5scUX/view?usp=sharing",
                     "[Internship Certificate](https://drive.google.com/file/d/1TuW2FPYaa5Tv3NX4_zueALg2xAQYLy-3/view?usp=sharing",
                     "[Internship Certificate](https://drive.google.com/file/d/1E1HDQwe7_M4Y-N0OmDRLxrhq_VmBb4jh/view?usp=sharing"
                     ]
    df["Certificates"] = certi
    # st.write(df,format='markdown', unsafe_allow_html=True)
    # st.write(df.style.format({'Certificates': '<a href="{}">{}</a>'}))

    # df.at[1, 'Certificates'] = f"[Experience Letter](https://drive.google.com/file/d/1f-DeitZtOxD3Xp8a9-q0fVTx8GJIuKqP/view)"

    # for i in range(len(df)):
    #     df.loc[i,"Certificates"] = certi[i]
    # # st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)


    def make_clickable(link):
        # target _blank to open new window
        # extract clickable text to display for your link
        text = link.split(']')[0].replace("[","")
        return f'<a target="_blank" href="{link}">{text}</a>'


    # link is the column with hyperlinks
    df['Certificates'] = df['Certificates'].apply(make_clickable)

    df = df.to_html(escape=False,index=False)

    st.write(df,f'<style>table {{background-color: white;border: 4px solid orange}}</style>', unsafe_allow_html=True)


with pro:
 col1, col2 = st.columns([1, 1])
 with col1:
     st.markdown("")
     st.markdown("")
     lottie_pro = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_glp2wakj.json")
     st_lottie(
         lottie_pro,
         speed=1,
         reverse=False,
         loop=True,
         height="450px",
         width=None,
         key=None,
     )
 with col2:
     st.markdown("")
     st.markdown("")
     st.subheader("What I DO!")
     st.markdown(
         "<p style='font-size: 20px'>Explore and develop <span style='color: green;'>Machine learning</span> and <span style='color: green;'>Data Science</span> projects, I develop <span style='color: green;'>JAVA applications</span> too.</p>",
         unsafe_allow_html=True)
     st.markdown(
         "<p style='font-size: 20px'>Aiming to explore every Data Engineering and Data Pipeline Tool.</p>",
         unsafe_allow_html=True)


