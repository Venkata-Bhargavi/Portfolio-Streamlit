import json
import streamlit as st
import pandas as pd
import requests
from st_functions import st_button,load_css
from PIL import Image
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
import subprocess
import webbrowser
# The code below is for the layout of the page
st.set_page_config(  # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
    page_title='Venkata_Bhargavi_Sikhakolli',  # String or None. Strings get appended with "• Streamlit".
    page_icon= None,  # String, anything supported by st.image, or None.
)
load_css()
res_url = "https://drive.google.com/file/d/1YthW-l6dMbe7YmnFPKhNIWiixroTNdaA/view?usp=sharing"
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
def open_link(url):
    webbrowser.open_new_tab(url)
# st.set_page_config(page_title="My Tabs", page_icon=":guardsman:", layout="wide")

tab_styles = """
.stTab {
    font-size: 36px;
}
"""
# st.set_page_config(page_title="My Tabs", page_icon=":guardsman:", layout="wide") #css=tab_styles,unsafe_allow_html=True)

# home, work_ex, pro, blog, skills, about, contact = st.tabs(["Home", "Work Experience", "Project", "Blog", "Skills", "About", "Contact"])
home,work_ex, pro, Blog,about = st.tabs(["🏠 **Home**","👩‍💻 **Work Experience**", "⚙ ️**Project**", "✍️ **Blog**","🧑 **About**"]   )
# below code works when clicked home
with home:
    buddi_col1, buddi_col2 = st.columns([1, 1])
    # col1  in home
    with buddi_col1:
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

    res_col,dummy_col = st.columns([1.2,8]) #columns for buttons
    with res_col:
        def open_link(url):
            # webbrowser.open_new_tab(url)
            subprocess.run(["open", url])
        res_url = "https://drive.google.com/file/d/1YthW-l6dMbe7YmnFPKhNIWiixroTNdaA/view?usp=sharing"
        st_button('newsletter','https://drive.google.com/file/d/1YthW-l6dMbe7YmnFPKhNIWiixroTNdaA/view?usp=sharing','RESUME',17)
        #
        # st.markdown(f"""<a href={res_url}><button style="background-color:GreenYellow;">Stackoverflow</button></a>
        # """,unsafe_allow_html=True)
        # st.markdown(f"[SEE MY RESUME 📋]({res_url})", unsafe_allow_html=True)
        # res_button = st.button("SEE MY RESUME ")
        # if res_button:
        #     # embed streamlit docs in a streamlit app
        #     # webbrowser.open("https://drive.google.com/file/d/1YthW-l6dMbe7YmnFPKhNIWiixroTNdaA/view?usp=sharing")
        #     open_link(res_url)
    link_col,dummy_col2 = st.columns([1.2,8])
    with link_col:
        linkedin_url = "https://www.linkedin.com/in/bhargavi-sikhakolli-9ab281117/"
        # linkedin_button = st.button("LINKEDIN  📋")
        # if linkedin_button:
        #     open_link(linkedin_url)
        # st.markdown(f"[LinkedIn 📋]({linkedin_url})", unsafe_allow_html=True)
        st_button('linkedin', f'{linkedin_url}','LinkedIn', 17)

    # col 2 in home
    with buddi_col2:
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


    buddi_col1, buddi_col2 = st.columns([1, 1])

    with buddi_col1:
        st.image("Utils/Images/buddi.png")
    with buddi_col2:
        st.markdown("**Company** :  BUDDI AI - a Claritrics Company")
        st.markdown("**Job Title** :  Research Engineer")
        st.markdown("**Duration** : 08-2020 to 06-2022 **(2 years)**")
        st.markdown("**Certificate** :  [Click Here](https://drive.google.com/file/d/1f-DeitZtOxD3Xp8a9-q0fVTx8GJIuKqP/view?usp=share_link)")
        with st.expander("**Read More**"):
            st.write("- Researched on extracting named entities i.e NER from Electronic Health Records leveraging BILSTM and CRF models resulting in a 30% reduction in medical coding costs")
            st.write("- Devised a more advanced ensemble model for Named Entity Recognition in conversational medical text, using BioBert as a reference model and incorporating contextual information, resulted in a 40% increase in precision compared to previously trained generic models")
            st.write("- Guided a team of 3 in a research project comparing BERT-based algorithms and provided knowledge transfer sessions")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    buddi2_col1, buddi2_col2 = st.columns([1, 1])
    with buddi2_col1:
        st.image("Utils/Images/buddi.png")
    with buddi2_col2:
        st.markdown("**Company** :  BUDDI AI - a Claritrics Company")
        st.markdown("**Job Title** :  Intern")
        st.markdown("**Duration** : 06-2020 to 08-2020 **(2 months)**")
        st.markdown("**Certificate** :  [Click Here](https://drive.google.com/file/d/1wkhYExQQ4j4CFlyMwBvJyaoEHfP5scUX/view?usp=sharing)")
        with st.expander("**Read More**"):
            st.write("- Developed an interactive command-line tool for conducting statistical analysis on numerical data using Scala and SMILE (Statistical Machine Intelligence and Learning Engine) package")
            st.write("- Tool allows users to select specific features for analysis and perform a variety of operations, such as mean, median and standard deviation")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    conti_col1, conti_col2 = st.columns([1, 1])
    with conti_col1:
        st.image("Utils/Images/conti.png")
    with conti_col2:
        st.markdown("**Company** :  Continental Automotive India Pvt Ltd")
        st.markdown("**Job Title** :  Research Intern in Artificial Intelligence and Robotics Labs")
        st.markdown("**Duration** : 08-2019 to 04-2020 **(10 months)**")
        st.markdown("**Certificate** :  [Click Here](https://drive.google.com/file/d/1TuW2FPYaa5Tv3NX4_zueALg2xAQYLy-3/view?usp=sharing)")
        with st.expander("**Read More**"):
            st.write("- Synthetic Voice Emotion Generation – A data generator to generate voice of multiple emotions other than input voice, it is intended to completely reduce manual efforts in collecting data from individuals")
            st.write("- The generator is trained on a CycleGAN model using voice data of different emotions and generates synthetic data that can be consumed by computer vision researchers in model training. The model’s generated voices are ~75% in comparison to human voices")
            st.write("- Created a UI in python to execute image processing operations and displays processed histograms and translated images in widgets")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    confirm_col1,confirm_col2 = st.columns([1,1])
    with confirm_col1:
        st.image("Utils/Images/confirmtkt.png")
    with confirm_col2:
        st.markdown("**Company** :  ConfirmTKT")
        st.markdown("**Job Title** :  Android Developer Intern")
        st.markdown("**Duration** : 05-2019 to 06-2019 **(1 month)**")
        st.markdown("**Certificate** :  [Click Here](https://drive.google.com/file/d/1E1HDQwe7_M4Y-N0OmDRLxrhq_VmBb4jh/view?usp=sharing)")
        with st.expander("Read More"):
            st.write("- Created a user-friendly interface for a recharge module by utilizing API calls and seamlessly integrating with a payment portal")
            st.write("- Leveraged XML in Android Studio to design and develop the interface for the recharge module")
            st.write("- Utilized Java programming language to execute API calls, integrate with the payment portal, and implement shared preferences")


# Project tab
with pro:
    buddi_col1, buddi_col2 = st.columns([1, 1])
    with buddi_col1:
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
    with buddi_col2:
     st.markdown("")
     st.markdown("")
     st.subheader("What I DO!")
     st.markdown(
         "<p style='font-size: 20px'>Explore and develop <span style='color: green;'>Machine learning</span> and <span style='color: green;'>Data Science</span> projects, I develop <span style='color: green;'>JAVA applications</span> too.</p>",
         unsafe_allow_html=True)
     st.markdown(
         "<p style='font-size: 20px'>Aiming to explore every Data Engineering and Data Pipeline Tools.</p>",
         unsafe_allow_html=True)
     st.image("Utils/Images/tools.drawio.png")
     st.markdown("**<p style='font-size: 40px'><span style='color: purple;'>PROJECTS</span></p>**",unsafe_allow_html=True)
     st.markdown("")
     st.markdown("")
    pro_col1_1,pro_col1_2 = st.columns([1,1])
    with pro_col1_1:
        heart_url = "https://heartdiseasejkkn.streamlit.app/"
        st.subheader("**Heart Disease Prediction** 💚")
        st.markdown("Category : **<span style='color: orange;'>Machine Learning</span>**",unsafe_allow_html=True)
        st.image("Utils/Images/Screen Shot 2023-01-10 at 4.26.27 PM.png")
        st.markdown("Heart diseases are complex and challenging to predict using machine intelligence and predictions are expected to be highly accurate. Knowing their heart condition in just few clicks can help in alerting patients about their health. Here is an app built using data science techniques and machine learning algorithm that can help you know about your heart health.")
        # res_button = st.button("**Heart Disease Prediction APP**")
        # if res_button:
        #     open_link(heart_url)
        st_button('', f'{heart_url}',
               'Heart Disease Prediction App', 17)
    with pro_col1_2:
        vim_url = "https://github.com/Venkata-Bhargavi/AED_Final_Project"
        st.subheader("**Vaccine Inventory Management** 💉")
        st.markdown("Category : **<span style='color: orange;'>JAVA Application Development</span>**", unsafe_allow_html=True)
        st.image("Utils/Images/Screen Shot 2023-01-10 at 4.24.46 PM.png")
        st.markdown("A vaccine management system which combinely manages distribution, inventory and monitoring of vaccine supply. This applications provides the traceability and security of the vaccines and its recipients.")
        st.markdown("")
        # res_button = st.button("**Github 🚑**")
        # if res_button:
        #     open_link(vim_url)
        st_button('', f'{vim_url}',
               'Github 🚑', 17)
    line_col, dummy= st.columns([0.9,0.001])
    with line_col:
        st.write("----------------------------------------------------------------")
    pro_col2_1, pro_col2_2, pro_col2_3 = st.columns([1, 1, 1])
    with pro_col2_1:
        st.markdown("")
        st.markdown("")
        st.subheader("**Machine Predictive Maintenance** 🏭")
        st.markdown("")
        st.markdown("")
        st.markdown("Category : **<span style='color: orange;'>Machine learning</span>**", unsafe_allow_html=True)
        st.markdown("A Machine Learning model with 98% accuracy in identifying potential machine failures in an industry")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        # res_button = st.button("**Colab 📔**")
        mpm_colab_rul = "https://colab.research.google.com/drive/1qX2yBbnwrMkc7Ag0dmAnYmJ_UBkK7ca7?usp=sharing"
        # if res_button:
        #     open_link(mpm_colab_rul)
        st_button('', f'{mpm_colab_rul}',
                       'Colab 📔', 17)
    with pro_col2_2:
        st.markdown("")
        st.markdown("")
        st.subheader("**Statistical Analysis Command Line Tool** 📈")
        st.markdown("Category : **<span style='color: orange;'>Scala Application Development</span>**", unsafe_allow_html=True)
        st.markdown("An Interactive command line tool implemented in Scala using SMILE(Statistical Machine Intelligence and Learning Engine) for conducting Statistical analysis on numerical data.")
        scala_url = "https://github.com/bhargavi31/CommandLineTool/tree/master/CommandLineTool"
        st.markdown("")
        st.markdown("")

        # git_button = st.button("**Github 📊**")
        # if git_button:
        #     open_link(scala_url)
        st_button('', f'{scala_url}',
               'Github 📊', 17)

    with pro_col2_3:
        st.markdown("")
        st.markdown("")
        st.subheader("**UI to display processed images** 🔍")
        st.markdown("")
        st.markdown("")
        st.markdown("Category : **<span style='color: orange;'>Python Application Development</span>**", unsafe_allow_html=True)
        st.markdown("An UI in python using PyQt library to execute image processing operations and displays processed histograms and translated images in widgets to help Computer Vision Engineers analyze model outputs")
        ui_url = "https://github.com/bhargavi31/UI_designer"
        st.markdown("")
        # git_button = st.button("**Github**")
        # if git_button:
        #     open_link(ui_url)
        st_button('', f'{ui_url}',
               'Github', 17)
    pro_col3_1,pro_col3_2,pro_col3_3 = st.columns([1,1,1])
    with pro_col3_1:
        st.markdown("")
        st.markdown("")
        st.subheader("**Medical Resource Management 🏥**")
        st.markdown("")
        st.markdown("")
        st.markdown("Category : **<span style='color: orange;'>Python Application Development</span>**",
                 unsafe_allow_html=True)
        st.markdown(
         "An UI in python using PyQt library to execute image processing operations and displays processed histograms and translated images in widgets to help Computer Vision Engineers analyze model outputs")
        ui_url = "https://github.com/bhargavi31/UI_designer"
        st.markdown("")
        # git_button = st.button("**Github ⚕️**")
        # if git_button:
        #     open_link(ui_url)
        st_button('', f'{ui_url}',
               'Github ⚕', 17)







with Blog:
    buddi_col1, buddi_col2 = st.columns([1, 2])
    with buddi_col1:
        st.markdown("")
        st.markdown("")
        st.subheader("Blogs")
        st.markdown("")
        st.markdown("[**Monitoring ML systems using MLOps - Medium**  🔗](https://medium.com/@bhargavi.sikhakolli31/monitoring-ml-systems-using-mlops-an-overview-e1d6eea64ae2)")
        res_url = "https://medium.com/@bhargavi.sikhakolli31/monitoring-ml-systems-using-mlops-an-overview-e1d6eea64ae2"
        res_button = st.button("""**🟡 Machine Learning operations  🟡 Model Monitoring**  🔗"""
                               " Machine Learning Operations helps in streamlining the deployment process in production." 
                                  " In addition it can be used for maintaining and monitoring the Machine Learning models.  Some of its features are focused and explained in this blog.")
        if res_button:
            open_link(res_url)

    with buddi_col2:
        lottie_pro = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_vjysv46c.json")
        st_lottie(
            lottie_pro,
            speed=1,
            reverse=False,
            loop=True,
            height="400px",
            width=None,
            key=None,
        )
    col2_1, col2_2 = st.columns([1, 2])
    with col2_1:
        st.markdown("")
        st.markdown("")
        st.subheader("Knowledge Share")
        st.markdown("")
        st.markdown(
            "[**Feature scaling in data preprocessing**  🔗](https://drive.google.com/file/d/1e49rttp_EYnMnbaXSkc4TBVGPTYwpafo/view?usp=sharing)")
        res_url = "https://drive.google.com/file/d/1e49rttp_EYnMnbaXSkc4TBVGPTYwpafo/view?usp=sharing"
        res_button = st.button("""**🟡 Feature scaling techniques  🟡 Data Science**  🔗"""
                               " Here is a presentation by me explaining feature scaling techniques to perform during Exploratory Data Analysis.")
        if res_button:
            open_link(res_url)

with about:
    st.markdown("")
    st.markdown("")
    st.header("Hi Again!")
    col1_1,col1_2 = st.columns([6,2])
    with col1_1:
        st.markdown(
            f"As a graduate student in Information Systems at Northeastern University in Boston, I bring a unique blend of academic and professional experience to my field. Prior to this, I worked as a Research Engineer at BUDDI AI. I also hold an M.Tech in Integrated Software Engineering(a five year integrated course) from Vellore Institute of Technology in India. My philosophy is centered on the belief that hard work and consistency are the keys to success, and I constantly strive to gain wisdom over just knowledge.")
        st.markdown("")
        st.markdown("**Note:** I am known among my colleagues as a fun and enjoyable person to work with.")
    with col1_2:
        st.image("Utils/Images/self.png", width=320)
    col1_1,col1_2 = st.columns([1,2])
    with col1_1:
      st.header("Contact Information")
        # st.image("Utils/Images/linkedin.png",width= 20)


    st.markdown("<p style='font-size: 20px'><span style='color: grey;'>Would you like to disscuss a project or a tech topic, or just want to say Hi? drop an email to</span> bhargavi.sikhakolli31@gmail.com <span style='color: grey;'>or</span> sikhakolli.v@northeastern.edu</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px'><span style='color: grey;'>Open to Opportunities : YES</span></p>",
                unsafe_allow_html=True)

    col2_1,col2_2 = st.columns([1,50])
    with col2_1:
        st.image("Utils/Images/linkedin.png", width=20)
    with col2_2:
        st.markdown("[LinkedIn](https://www.linkedin.com/in/bhargavi-sikhakolli-9ab281117/)")
    col3_1,col3_2 = st.columns([1,50])
    with col3_1:
        st.image("Utils/Images/medium_logo.png", width=20)
    with col3_2:
        st.markdown("[Medium](https://medium.com/@bhargavi.sikhakolli31)")

