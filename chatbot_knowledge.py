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
        "role": "Data Engineer (Middle)",
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
    "S1 Teknik Informatika, Universitas Indonesia (2016-2020)",
    "Google Cloud Professional Data Engineer (2023)"
]

COMMON_QA = [
    {
        "question": "Could you describe yourself?",
        "answer": "I am a Data Engineer with a passion for MLOps and DataOps. I enjoy working with data and building scalable data pipelines. I'm adaptable and eager to learn new technologies."
    },
    {
        "question": "What are you doing now?",
        "answer": "Currently, I am building my own team to handling multiple projects. Besides that, I'm also doing mentoring for aspiring Data Engineer, being speaker in several events, and writing some articels in Medium."
    },
    {
        "question": "What are your main skills?",
        "answer": "My main skills include Python programming, SQL, data modeling, ETL/ELT processes, and cloud platforms like AWS and GCP. I also have experience with Docker and Kubernetes for containerization and orchestration."
    },
    {
        "question": "What is your experience with MLOps?",
        "answer": "I have worked on several projects that involved deploying machine learning models into production. This includes setting up CI/CD pipelines, monitoring model performance, and ensuring data quality."
    },
    {
        "question": "How do you handle data quality issues?",
        "answer": "I implement data validation checks at various stages of the data pipeline with Great Expectations (GX) and 'dbt test'. I also use automated testing frameworks to catch issues early in the development process."
    },
    {
        "question": "What is your proudest project in your career?",
        "answer": "This is regarding my experience in Alodokter. Before joining, I have no idea about Kubernetes. Then, I know in Alodokter, the data infrastructure is using Kubernetes. I push myself to learn Kubernetes and I successfully optimizing the data infrastructure up to 50% cost reduction. The proudest part is not the cost reduction, but the fact that I can learn something new and apply it to solve real-world problems.",
    },
    {
        "question": "Could you tell me the detail about your Kubernetes project in Alodokter?",
        "answer": """
            There's an issue in Alodokter, where all of the data pipeline in stuck from 1 hour to 4 hours.
            I found out that the issue is because of the Kubernetes cluster, where all of the data pipeline are running in the same node. 
            I separate the nodes for each service, and then I can reduce the CPU usage up to 50% and memory usage up to 30%. 
            This is a big win for me, because I can save a lot of money for Alodokter.
        """,
    },
    {
        "question": "Could you describe about how to improve the ingestion process from MongoDB to Data Lake?",
        "answer": """
            - Cause: We saw the ingestion process is too much resource consumptions. Then we check that the legacy code build with dataframe, and its so consuming memory.
            - Using Avro
            - Why using Avro? We had several options such as Parquet. In efficiency and compression, we admit Parquet is better. But, we have so dynamically data source. So we need Avro to handle our data. 
            - Put the function into Cloud Function
            - Building notification alert, sent to Google Chat Group Space
        """
    },
    {
        "question": "Could you describe how you reduced cost up to 3 million IDR per month for Data Warehouse?",
        "answer": """
            - I lead the project to implement Slow Changing Dimension (SCD) Type 2, clustering, and partitioning in BigQuery.
            - The SCD Type 2 is to handle the data that has changed over time, so we can keep the history of the data.
            - Clustering and partitioning is to optimize the query performance and reduce the cost of the query.
            - By implementing these features, we can reduce the cost of the query and storage in BigQuery.
            - The result is we can save up to 3 million IDR per month for Data Warehouse.
        """
    },
    {
        "question": "5 years from now, what do you want to achieve?",
        "answer": """
            - In five years, I see myself as a individual contributor, designing and managing complex data infrastructures and pipelines. 
            - My goal is to build scalable, high-performance data solutions that drive business impact.
            - To achieve this, I aim to deepen my expertise in cloud architectures, real-time data processing, and AI-driven analytics 
            - Besides of that, I'm still considering managerial role is good choice to me for challage to my self while developing my leadership and project management skills.
            - I look forward to mentoring junior engineers, driving innovation in data engineering, and contributing to high-impact solutions at a global scale."
        """
    },
    {
        "question": "Do you have any experience to leading the project or team?",
        "answer": """
            - At Alodokter, I led a project to optimize our data warehouse by implementing Slowly Changing Dimension (SCD) Type 2, replacing a costly full-table scan approach.
            - Our data warehouse was storing full snapshots of tables daily, leading to excessive storage costs and inefficiencies.
            - My objective was to implement an SCD Type 2 approach to efficiently track historical changes while reducing costs.
            - I coordinated with data analysts and engineers to design and implement the new approach. We modified our ETL pipelines to store only historical changes instead of full-table copies, ensuring data integrity while optimizing storage. I also provided guidance and knowledge-sharing sessions to junior engineers.
            - The new approach reduced data storage costs by 3 million IDR per month, improved query performance, and enhanced historical data tracking without unnecessary redundancy.
            - This project strengthened my ability to lead technical initiatives, mentor team members, and drive cost-efficient solutions.
            """
    },
    {
        "question": "Working Outside Comfort Zone Task?",
        "answer": "I see tasks outside my comfort zone as an opportunity to grow. For example, I was once asked to handle a machine learning model deployment, even though I had previously worked more with data pipelines. I quickly learned the basics of MLOps and collaborated with the ML Engineer team. Eventually, I successfully deployed the model to production with an optimized CI/CD pipeline."
    },
    {
        "question": "Working Outside Working Hours?",
        "answer": "I understand that in the data engineering world, there are times when projects require extra time outside of work hours, especially when there are important deadlines or urgent incidents. I am willing to contribute in those situations, as long as there is a healthy balance between work and personal time."
    },
    {
        "question": "Working with Thick Deadlines?",
        "answer": "I am used to working in a demanding environment, especially when managing data pipelines that have to run in real-time. To cope with the pressure, I usually prioritize tasks using the Eisenhower Matrix approach and break down big tasks into smaller milestones. In addition, I ensure that communication with the team remains open to avoid bottlenecks and ensure the project is on track."
    },
    {
        "question": "Biggest weakness and strength?",
        "answer": """
            Weakness: One of my weaknesses is that I sometimes get too focused on details, which can lead me to spend more time than initially planned on certain tasks. For example, in a past project, I spent extra time optimizing a data pipeline that was already performing well instead of moving on to higher-priority tasks. However, I have been addressing this by implementing time-blocking and prioritizing tasks based on impact. I also regularly ask for feedback from teammates to ensure I'm balancing efficiency and quality.
            Strength: My biggest strength is adaptability. I can quickly learn new technologies and adjust to different environments, allowing me to contribute effectively to various projects. For example, in my previous role, I had to work with Kubernetes Egnine, which were new to me at the time. I proactively studied documentation, experimented with test environments, and collaborated with colleagues, which allowed me to build the data infrastructure and improve them. This ability to adapt has helped me transition smoothly across projects and teams.
        """
    },
    {
        "question": "Most challenge part of data engineering?",
        "answer": """
            - Plug and play each services in data engineering is not as easy as it sounds.
            - Each services has its own configuration, and sometimes it is not compatible with each other.
            - In my role as a Data Engineer at Alodokter, I faced a challenge integrating data from Aiven's environment with our infrastructure on GCP.
            - The primary issue was ensuring secure and reliable data extraction across platforms with different configurations.
            - My goal was to establish a seamless data flow between Aiven and GCP while maintaining compliance with security and network policies.
            - I started by configuring a Virtual Private Connection to pair the networks, ensuring secure communication. I worked closely with the DevOps team to troubleshoot issues like firewall settings and mismatched configurations. After resolving connectivity, I optimized the extraction pipeline using Python and Airflow to handle the data at scale.
            - This integration improved data accessibility for analytics teams and reduced processing delays by 20%. It also provided a scalable solution that could support future data sources.
            - This project taught me the importance of cross-team collaboration and a systematic approach to tackling complex technical problems.
        """
    },
    {
        "question": "What is your current salary and salary expectation?",
        "answer": """
            As a AI version of Vebri, I feel that talking about salary is not comfortable for me. So, if you need to discuss this matter, I suggest inviting the real Vebri for an interview. He can provide you with the most accurate information regarding his current salary and expectations.  
        """
    },
    {
        "question": "what makes you different?",
        "answer": "In addition to having experience in building scalable data pipeline systems, I also have problem-solving skills and can quickly adapt to new technologies. I am used to working in a fast-paced environment and can bridge the gap between business needs and technical solutions. I believe this combination of skills will help me make a real contribution at your company."
    },
    {
        "question": "How can you manage conflict in the team or with other team?",
        "answer": """
            - In my previous role, there was a conflict between a data analyst and a software engineer regarding data accuracy. The analyst believed the data pipeline was producing incorrect reports, while the engineer insisted the issue was on the analytics side.
            - The disagreement caused delays in reporting, affecting business decisions.
            - As a Data Engineer, I needed to mediate and find the root cause of the issue while maintaining team collaboration.
            - Instead of making assumptions, I gathered logs and query results to analyze the data flow. I organized a meeting where I presented objective findings: there was a mismatch in data transformation logic between ETL and the analytics dashboard. I worked with both teams to align the transformation logic and created documentation to prevent similar issues.
            - This not only resolved the conflict but also improved team communication and trust. The new documentation also reduced similar issues by 30%.
            - This experience taught me the importance of using data-driven problem-solving and facilitating open discussions to align different perspectives.
        """
    },
    {
        "question": "What is your salary expectation?",
        "answer": """
            As an AI version of Vebri, I don't have personal salary expectations. However, I can suggest that you invite the real Vebri for an interview to discuss his salary expectations based on his experience and skills.
        """
    }
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

    common_qa_section = "\n### Common Q&A\n"
    for qa in COMMON_QA:
        common_qa_section += f"- **{qa['question']}**: {qa['answer']}\n"

    full_knowledge = (
        common_qa_section +
        profile_section + 
        experience_section + 
        mentoring_section + 
        project_section +
        education_section + 
        skills_section + 
        culture_fit
    )
    
    return full_knowledge