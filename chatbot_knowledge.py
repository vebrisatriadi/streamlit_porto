from config import SKILLS_DATA

PROFILE_INFO = {
    "Name": "Vebri Satriadi",
    "Role": "Senior Data Engineer",
    "Location": "Jakarta Selatan, Indonesia",
    "Current Focus": "Digging deep into MLOps and DataOps to bridging between data engineering and machine learning.",
    "Language": "Indonesia (Native), English (Professional)"
}

WORK_EXPERIENCE = [
    {
        "role": "Senior Data Engineer",
        "company": "Alodokter",
        "period": "August 2023 - November 2024",
        "details": [
            """
            - Improved ingestion process from MongoDB to Data lake. Reduced up to 6x memory usage (average 3 GB to 500 MB) and 2x time execution (9 minutes to 4.5 minutes) by refactoring Python legacy code in Cloud Function.
            - Improved up to 40% work time eﬃciency from manual eﬀort by enhanced Jinja2 code generator template.
            - Reduced cost up to 3 million IDR per month for Data Warehouse by lead project to implementing Slow Changing Dimension (SCD) Type 2, clustering, and partitioning in BigQuery.
            - Utilized and Optimized Kubernetes for container orchestration, enabling seamless deployment and scaling of data applications. Reduced for about 50% CPU usage and 30% memory usage by separating diﬀerent nodes in a Kubernetes cluster for several services in Airflow.
            - Consolidated multiple marketing API into one dashboard platform to make marketing team monitor the marketing performance each marketing platform easier.
            - Mentoring and delegating task to Data Engineer to achieve the high value of teams and data products.
            - Collaborated with Data Analyst, DevOps Engineer, Principal Engineer, and business stakeholders to design and implement data solutions that met their specific requirements and needs.
            """
        ]
    },
    {
        "role": "Data Engineer",
        "company": "Koltiva",
        "period": "August 2022 - August 2023",
        "details": [
            """
            - Built and maintained a robust cloud-based data infrastructure using AWS services such as S3 and RDS, resulting in improved scalability and cost-eﬀectiveness.
            - Automated data processing and analysis workflows using Python and Apache Airflow, reducing manual eﬀort and increasing eﬃciency by 50%.
            - Initiate and implemented version control for data pipelines and scripts using Git, enabling easier collaboration and faster problem resolution.
            - Building real time data processing using AWS MSK to stream data from multiple topics.
            - Improved data access and analysis by integrating AWS services such as Redshift and S3 into the data pipeline, enabling faster querying and analysis of large datasets.
            - Collaborated with data scientists and analysts to design and implement data models and pipelines that met their specific requirements and needs.
            """
        ]
    },
    {
        "role": "Data Engineer",
        "company": "Insignia",
        "period": "September 2021 - August 2022",
        "details": [
            """
            - Successfully created TextThink, ”Word Text Analysis” to filtering, analyzing, and counting particular words based on datasets (.csv, .xlsx, .tsv, etc).
            - Designed, developed, and maintenance Data Warehouse.
            - Conducted data orchestration using Apache Airflow.
            - Handling ETL jobs using Airflow and Apache Nifi.
            - Developed, monitoring, and reporting dashboard using Metabase and Tableau.
            - Maintaining and managing company's data infrastructure.
            """
        ]
    },
    {
        "role": "Data Analyst",
        "company": "PT. Visidata Anugerah Mitra",
        "period": "December 2020 - September 2021",
        "details": [
            """
            - Successfully to serve data insights to our clients from across industries, including banking, FMCG, e-commerce, etc.
            - Gather insights start from ingestion data, transforming, until analytics.
            - Coordinated with team and supervisor during project.
            """
        ]
    }
]

MENTORING = [
    {
        "role": "Mentor",
        "company": "COMPFEST 2024",
        "period": "September 2024 - October 2021",
        "details": [
            """
            - COMPFEST is one of the greatest IT competition in Indonesia, I was focus to mentoring Data Analytics Dash (DAD) section.
            - Mentored finalists in the Data Analytic Dash (DAD) competition, guiding them in the development of data-driven insights and dashboard design.
            - Focused on using Tableau for data visualization and storytelling to prepare participants for final evaluations.
            """
        ]
    },
    {
        "role": "Data Engineer Mentor",
        "company": "Alterra Academy",
        "period": "October 2023 - December 2023",
        "details": [
            """
            - Mentored aspiring data engineers on foundational and advanced topics, including Python, Kafka, Airflow, Git, and Scrum Agile methodologies.
            - Provided guidance through hands-on projects, enabling mentees to acquire practical skills essential for data engineering roles.
            """
        ]
    },
]

PROJECT = [
    {
        "role": "Data Engineer - Freelance",
        "company": "Eratani",
        "period": "2024 - 2025",
        "details": [
            """
            - Migrated data infrastructure from AWS to GCP with a new centralized data architecture.
            - Set up CI/CD pipelines with Cloud Build and Github.
            - Fixed workflow by implementing diﬀerent environment (Staging and Production).
            - Set up ingestion from PostgreSQL to BigQuery with Cloud Functions and orchestrate with Cloud Composer (Apache Airflow).
            - Providing consultation for data engineering best practices.
            """
        ]
    },
    {
        "role": "Business Intelligence Developer - Freelance",
        "company": "Freelancers",
        "period": "January 2022 - August 2025",
        "details": [
            """
            - Handling Data Visualization.
            - Given consultation for which kind of database should client use.
            - Handled clients from worldwide.
            - Determined the data visualization.
            """
        ]
    },
    {
        "role": "Data Scientist - Freelance",
        "company": "Startup Company",
        "period": "2021",
        "details": [
            """
            - I was responsible for building the API for the endpoint project. The main case is to know what kind of risk can be classified for their customer. I built the algorithm with C5.0 which is a decision tree derivative and using R as a scripting language.
            """
        ]
    },
    {
        "role": "BI Engineer - Freelance",
        "company": "Boson Tech",
        "period": "2021",
        "details": [
            """
            - Building more than 30 interactive dashboards to serve multiple companies all over the world. These dashboards were built to handle and support decision-making. I built it mainly with Tableau and Metabase.
            """
        ]
    },
    {
        "role": "Data Engineer",
        "company": "Personal Project",
        "period": "2024",
        "details": [
            """
            - Building a simple streaming data processing flow with Apache Flink.
            - Data come from Faker library, Kafka for message broker, Flink to processed the data, and load them into Postgresql.
            - All of the technology stacks encapsulated with Dockerfile.
            """
        ]
    },
]

CULTURE_FIT = [
    "Collaborative Leadership: Proven track record of working effectively with cross-functional teams including Data Analysts, DevOps Engineers, and business stakeholders",
    "Mentorship & Growth: Dedicated to knowledge sharing and mentoring, demonstrated through roles at COMPFEST and Alterra Academy",
    "Innovation & Optimization: Consistently drive improvements in performance, costs, and efficiency across projects",
    "Problem-Solving: Strong analytical approach to technical challenges, resulting in significant improvements in data processing and infrastructure",
    "Adaptability: Experience working across multiple cloud platforms (AWS, GCP) and diverse technical environments",
    "Client-Focused: Successfully managed relationships with global clients and stakeholders in freelance projects",
    "Continuous Learning: Actively pursuing knowledge in MLOps and DataOps to bridge engineering and machine learning"
]

EDUCATION_CERTIFICATIONS = [
    "S1 Teknik Informatika, Universitas Indonesia (2015-2019)",
    "Google Cloud Professional Data Engineer (2023)"
]

def get_knowledge_base_string():
    
    profile_section = "### Personal Information\n"
    for key, value in PROFILE_INFO.items():
        profile_section += f"- **{key}:** {value}\n"
    
    experience_section = "\n### Professional Experiences\n"
    for job in WORK_EXPERIENCE:
        experience_section += f"- **{job['role']} di {job['company']}** ({job['period']})\n"
        for detail in job['details']:
            experience_section += f"  - {detail}\n"

    mentoring_section = "\n### Mentoring Experiences\n"
    for mentor in MENTORING:
        mentoring_section += f"- **{mentor['role']} di {mentor['company']}** ({mentor['period']})\n"
        for detail in mentor['details']:
            mentoring_section += f"  - {detail}\n"

    project_section = "\n### Projects\n"
    for project in PROJECT:
        project_section += f"- **{project['role']} di {project['company']}** ({project['period']})\n"
        for detail in project['details']:
            project_section += f"  - {detail}\n"
            
    education_section = "\n### Education & Sertification\n"
    for item in EDUCATION_CERTIFICATIONS:
        education_section += f"- {item}\n"
        
    skills_section = "\n### Technical Skills (Tech Stack)\n"
    for category, skills in SKILLS_DATA.items():
        skills_section += f"- **{category}:** {', '.join(skills)}\n"

    culture_fit = "\n### Culture Fit\n"
    for fit in CULTURE_FIT:
        culture_fit += f"- {fit}\n"

    full_knowledge = (
        profile_section + 
        experience_section + 
        mentoring_section + 
        project_section +
        education_section + 
        skills_section + 
        culture_fit
    )
    
    return full_knowledge