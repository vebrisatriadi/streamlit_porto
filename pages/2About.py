# pages/2_👨‍💻_About.py
import streamlit as st

def load_css():
    """Memuat CSS kustom untuk seluruh aplikasi."""
    st.markdown("""
    <style>     
        /* Style untuk kotak metrik individual */
        .individual-metric {
            display: inline-block; /* Agar bisa diatur padding dan margin */
            background-color: #f0f2f6; /* Warna latar belakang dasar */
            color: #333; /* Warna teks */
            padding: 8px 12px; /* Padding di dalam kotak */
            margin: 4px; /* Jarak antar kotak */
            border-radius: 8px; /* Sudut melengkung */
            font-size: 1rem;
            font-weight: bold;
        }

        /* Warna latar belakang yang berbeda untuk setiap metrik */
        .metric-bg-1 { background-color: #e1f5fe; color: #0277bd; } /* Light Blue */
        .metric-bg-2 { background-color: #fffde7; color: #f9a825; } /* Light Yellow */
        .metric-bg-3 { background-color: #e8f5e9; color: #1b5e20; } /* Light Green */
        .metric-bg-4 { background-color: #f3e5f5; color: #5e35b1; } /* Light Purple */
    </style>
    """, unsafe_allow_html=True)

# --- Memuat Aset ---
load_css()

def render_about():
    """Merender konten halaman About."""
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    
    # Sisa konten halaman About
    st.write("""
    ### Executive Summary
    A seasoned Data Engineer with a proven track record of architecting and maintaining scalable data infrastructure. 
    My expertise lies in optimizing data flow, ensuring data quality, and enabling data-driven decisions across the organization. 
    I am passionate about leveraging modern technologies to solve complex data problems efficiently.
    """)

    st.markdown("### Work Experiences")
    
    with st.expander("Senior Data Engineer - Alodokter (August 2023 - November 2024)"):
        st.markdown("""
        - **Optimized Ingestion Pipeline**: Refactored a critical Python-based ingestion process from MongoDB to the Data Lake running on Cloud Function.
            - **Result**: Reduced memory consumption by **6x** (from 3 GB to 500 MB on average) and cut execution time by **50%** (from 9 minutes to 4.5 minutes).
        - **Enhanced Developer Productivity**: Improved and expanded a Jinja2-based code generator template, automating boilerplate code for new data pipelines.
            - **Result**: Decreased manual effort and accelerated development, improving team's work time efficiency by an estimated **40%**.
        - **Optimized Kubernetes Resource Utilization**: Engineered and fine-tuned container orchestration on Google Kubernetes Engine (GKE) for Airflow services. 
            - **Result**: Achieved a **~50% reduction in CPU usage** and **~30% reduction in memory footprint**, significantly improving cluster stability and cost-efficiency.
        - **Led and Mentored Data Engineering Team**: Guided junior data engineers through complex tasks, fostering team growth and enabling effective delegation. This effort improved team velocity and ensured the successful delivery of high-impact data products.
        - **Drove Cross-Functional Data Solutions**: Partnered strategically with Data Analysts, DevOps Engineers, and business stakeholders to design, develop, and deploy end-to-end data solutions that directly addressed critical business requirements.
        - **Tech Stack**: Google Cloud Platform (GCP), Cloud Functions, Google Kubernetes Engine (GKE), Apache Airflow, Pub/Sub, Jinja2, BigQuery, MongoDB, PostgreSQL, FastAPI, Looker Studio.
        """)

    with st.expander("Mentor - COMPFEST 2024 (September 2024 - October 2024)"):
        st.markdown("""
        - COMPFEST is one of the greatest IT competition in Indonesia, I was focus to mentoring Data Analytics Dash (DAD) section.
        - Mentored fnalists in the Data Analytic Dash (DAD) competition, guiding them in the development of data-driven insights and dashboard design. 
        - Focused on using Tableau for data visualization and storytelling to prepare participants for final evaluations.
        - **Tech Stack**: Tableau
        """)
    
    with st.expander("Data Engineer Mentor - Alterra Academy (October 2023 - December 2023)"):
        st.markdown("""
        - Mentored aspiring data engineers on foundational and advanced topics, including Python, Kafka, Airflow, Git, and Scrum Agile methodologies.
        - Provided guidance through hands-on projects, enabling mentees to acquire practical skills essential for data engineering roles.
        - **Tech Stack**: Apache Kafka, Apache Airflow, Git, Docker
        """)

    with st.expander("Data Engineer - Koltiva (August 2022 - August 2023)"):
        st.markdown("""
        - Built and maintained a robust cloud-based data infrastructure using AWS services such as S3 and RDS, resulting in improved scalability and cost-effectiveness.
        - Automated data processing and analysis workflows using Python and Apache Airflow, reducing manual effort and increasing effciency by 50%.
        - Initiate and implemented version control for data pipelines and scripts using Git, enabling easier collaboration and faster problem resolution.
        - Building real time data processing using AWS MSK to stream data from multiple topics.
        - Improved data access and analysis by integrating AWS services such as Redshift and S3 into the data pipeline, enabling faster querying and analysis of large datasets.
        - Collaborated with Business Intelligence, Data Analyst, DevOps Engineer, and business stakeholders to design and implement data solutions that met their specific requirements and needs.
        - **Tech Stack**: Amazon Web Service (AWS), Amazon MSK, Amazon RDS, Amazon Lambda, Amazon S3, ElasticSearch, Amazon EC2, Apache Airflow, Flask.
        """)

    with st.expander("Data Engineer - Insignia (September 2021 - August 2022)"):
        st.markdown("""
        - Successfully created TextThink, "Word Text Analysis" to fltering, analyzing, and counting particular words based on datasets (.csv, .xlsx, .tsv, etc).
        - Designed, developed, and maintenance Data Warehouse.
        - Conductied data orchestration using Apache Airflow.
        - Handling ETL jobs using Airflow and Apache Nifi.
        - Developed, monitoring, and reporting dashboard using Metabase and Tableau.
        - Maintaining and managing company's data infrastructure.
        - **Tech Stack**: Google Cloud Platform (GCP), BigQuery, Apache Airflow, Apache Nifi, Metabase, Tableau.
        """)
    
    with st.expander("Business Intelligence Developer - Freelance (January 2022 - August 2023)"):
        st.markdown("""
        - Handling Data Visualization.
        - Given consultation for which kind of database should client use.
        - Handled clients from worldwide.
        - Determined the data visualization.
        - Tech Stack: Metabase, Tableau, Google Data Studio.
        """)

    with st.expander("Data Analyst - PT. Visidata Anugerah Mitra (December 2020 - August 2021)"): 
        st.markdown("""
        - Successfully to serve data insights to our clients from across industries, including banking, FMCG, e-commerce, etc.
        - Gather insights start from ingestion data, transforming, until analytics.
        - Coordinated with team and supervisor during project.
        - Tech Stack: Alteryx, Tableau, Python.
        """)

    with st.expander("Data Scientist Intern - PT. Ilios Studio Teknologi (Tuupai) - October 2019 - December 2020"):
        st.markdown("""
        - Learning about data flow in Data Analytics field.
        - Understanding company's data to get insights such as retention rate, customer acquisition, etc.
        """)
    
    with st.expander("Laboratory Assistant - Informatics UII Laboratory (October 2018 - October 2019)"):
        st.markdown("""
        - My responsibility is to support our lecturer in curricular activities in laboratory. I also leading the students to more understanding about the curriculum.
        """)

    st.markdown("### Education & Certifications")
    st.write("- **Bachelor Degree of Computer Science** - Universitas Islam Indonesia (September 2016 - July 2020)")
    st.write("- **Machine Learning by Standford University** (2020)")

    with st.expander("Curriculum Vitae"):
        st.markdown("""
        - In case you need my CV, kindly download from: [Curriculum Vitae](https://drive.google.com/file/d/1eQEtlWzLuRZCZeux3HJbLaekhC48c3CU/view?usp=sharing)
        """)

    st.markdown("### Publications")
    st.write("""##### Penalty Strategy in The Fitness Function of Grey Wolf Optimizer for Minimum Spanning Tree Problem""")
    st.write("""Co-Author - IOP Publisher - 2021 - [Link](https://iopscience.iop.org/article/10.1088/1757-899X/1077/1/012071)""")

    st.write("""##### Penyilangan N-Titik Acak dalam Algoritme Genetika untuk Permasalahan Pohon Rentang Minimum""")
    st.write("""Author - Automata - 2020 - [Link](https://journal.uii.ac.id/AUTOMATA/article/view/15524)""")

    st.write("""##### Rancang Purwarupa Aplikasi UniBook Menggunakan Metode Pendekatan Design Thinking""")
    st.write("""Co-Author - Seminar Nasional Aplikasi Teknologi Informasi (SNATi) - 2017 - [Link](https://www.researchgate.net/publication/336711851_Rancang_Purwarupa_Aplikasi_UniBook_Menggunakan_Metode_Pendekatan_Design_Thinking)""")


# Panggil fungsi untuk merender halaman
render_about()