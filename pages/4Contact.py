# pages/4_📞_Contact.py
import streamlit as st
import yagmail
from config import CONTACT_INFO

def send_email(name, email, subject, message_body):
    """Sends an email using yagmail and Streamlit secrets."""
    try:
        yag = yagmail.SMTP(
            user=st.secrets["email"]["username"],
            password=st.secrets["email"]["password"]
        )
        yag.send(
            to=st.secrets["email"]["receiver"],
            subject=f"Vebri's Landing Page: {subject} from {name}",
            contents=f"<h3>From: {name} ({email}) <{email}></h3>\n<h3>Message:</h3>\n{message_body}",
            headers={"Reply-To": email}
        )
        return True, "Email sent successfully!"
    except Exception as e:
        return False, f"Failed to send email: {e}"

def render_contact():
    st.markdown('<h2 class="section-header">Get In Touch</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📬 Contact Information")
        st.write(f"📧 **Email:** {CONTACT_INFO['email']}")
        # st.write(f"📱 **Phone:** {CONTACT_INFO['phone']}")
        st.write(f"🏢 **LinkedIn:** [{CONTACT_INFO['linkedin']}]({CONTACT_INFO['linkedin']})")
        st.write(f"🐙 **GitHub:** [{CONTACT_INFO['github']}]({CONTACT_INFO['github']})")
        st.write(f"🌐 **Medium:** [{CONTACT_INFO['medium']}]({CONTACT_INFO['medium']})")
        
        st.markdown("### 💼 Available for:")
        st.write("✅ Full-time, part-time, and freelance positions")
        st.write("✅ Consulting on data architecture & strategy")
        st.write("✅ Technical mentoring and team upskilling")
        st.write("✅ Speaking opportunities (remote or on-site)")
    
    with col2:
        st.markdown("### 📝 Send me a message")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name", key="name")
            email = st.text_input("Your Email", key="email")
            subject = st.selectbox("Subject", 
                                 ["Job Opportunity", "Consulting Inquiry", "Collaboration", "General Question"], 
                                 key="subject")
            message = st.text_area("Message", height=150, key="message")
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and email and message:
                    success, response_message = send_email(name, email, subject, message)
                    if success:
                        st.success("Thank you for your message! I'll get back to you soon.")
                        st.balloons()
                    else:
                        st.error(f"An error occurred. {response_message}")
                else:
                    st.error("Please fill in all the fields before sending.")

render_contact()