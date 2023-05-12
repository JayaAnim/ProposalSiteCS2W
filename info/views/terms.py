from .base import Section, BaseTemplateView

""""
This views file renders the static pages of terms of service and privacy policy
"""

# ============================== Privacy policy Page and Sections ============================== #

class Section1(Section):
    section_style = 'light'
    section_title = "Privacy Policy for CyberSkills2Work"
    section_text = "Last Updated: 5/11/2023 </br></br>CyberSkills2Work is committed to protecting the privacy and accuracy of your confidential information to the extent possible, subject to provisions of state and federal laws. Other than as required by laws that guarantee public access to certain types of information, or in response to legal documents that authorize access, personally-identifiable information is not actively shared. We do not redistribute or sell personal information collected on our web servers. This Privacy Policy provides a detailed description of personal information that we collect, record, and use. If you do not agree with the terms in this privacy notice, please discontinue use of our services immediately. This Privacy Policy applies to visitors of cyberskills2work.org. It is valid regarding information shared and/or collected while using it online. This policy does not apply to any information collected offline or via channels other than our website. By using cyberskills2work.org, you hereby consent to our Privacy Policy."

class Section2(Section):
    section_style = 'dark'
    section_title = "How We Collect and Use Your Information"
    section_text = "To improve our services and/or to provide additional information to respond to inquiries, we may require you to provide us with certain personally identifiable information, including your name, phone number, email address, and/or educational goals and interests. We will use the information that you provide for research, training programs or for administrative purposes to contact you about your interests in our CyberSkills2Work program. Additional personal information may be requested for cybersecurity career option determination or for admission consideration to participate in the CyberSkills2Work program. We also collect other types of information from our website's visitors to enhance the user experience."

class Section3(Section):
    section_style = 'light'
    section_title = "Analytical Data Collection"
    section_text = "Like most websites, cyberskills2work.org uses data files that record visitors of the site. It is a standard procedure for hosting companies and their analytics services. These data files contain information such as internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date and time stamp, referring/exit pages, requested webpages, and even number of clicks on hyperlinks. This information helps us to analyze trends, administer the site, track user's movement around the site, and gather demographic information. IP addresses and other such information are not linked to any information that is personally identifiable."

class Section4(Section):
    section_style = 'dark'
    section_title = "Cookies"
    section_text = "Cyberskills2work.org uses cookies to store information about visitors' preferences to record user-specific data on visited or accessed pages and to personalize or customize our webpage content based on your browser type or information choices."

class Section5(Section):
    section_style = 'light'
    section_title = "Service Providers"
    section_text = "We may employ third-party companies and individuals for either of the following reasons: to facilitate our service, to provide services on our behalf, to perform services, to assist us in analyzing how our service is used. These third parties may have access to your personal information to perform tasks assigned to them on our behalf. However, they are required not to disclose or use the information for any other purpose."

class Section6(Section):
    section_style = 'dark'
    section_title = "Children's Information"
    section_text = "We believe in safeguarding children online. We urge parents and guardians to monitor their children's internet use and guide their online activity. Cyberskills2work.org does not knowingly collect any personally identifiable information from children under age 13. If a parent or guardian believes that cyberskills2work.org has unknowingly obtained personally-identifiable information of a child under age 13, please contact us immediately. We will promptly remove such information from our records."

class Section7(Section):
    section_style = 'light'
    section_title = "Security"
    section_text = "CyberSkills2Work and its affiliates safeguard information collected and stored in accordance with the law. All personally-identifiable information is stored securely in an encrypted manner."

class Section8(Section):
    section_style = 'dark'
    section_title = "Links to Third-Party Sites"
    section_text = "Cyberskills2work.org provides external links to other websites. These links may route to partner sites not operated by us. Therefore, we advise you to review the privacy policies of those websites. We do not manage those third-party sites and do not assume responsibility for them."

class Section9(Section):
    section_style = 'light'
    section_title = "Privacy Policy Changes"
    section_text = "At times, we may need to update our Privacy Policy. We reserve the right to update this Privacy Policy at any time and without prior notification. Therefore, we encourage you to review this page periodically for any changes."

class Section10(Section):
    section_style = 'dark'
    section_title = "Contact Information"
    section_text = "To get more information about our Privacy Policy, please contact us at info@cyberskills2work.org."

class PrivacyPolicy(BaseTemplateView):
    template_name = 'info/terms/TermsPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sections = []
        sections.append(Section1.as_view()(self.request).rendered_content)
        sections.append(Section2.as_view()(self.request).rendered_content)
        sections.append(Section3.as_view()(self.request).rendered_content)
        sections.append(Section4.as_view()(self.request).rendered_content)
        sections.append(Section5.as_view()(self.request).rendered_content)
        sections.append(Section6.as_view()(self.request).rendered_content)
        sections.append(Section7.as_view()(self.request).rendered_content)
        sections.append(Section8.as_view()(self.request).rendered_content)
        sections.append(Section9.as_view()(self.request).rendered_content)
        sections.append(Section10.as_view()(self.request).rendered_content)
        context['sections'] = sections
        return context
    
# ============================== Terms of Service and Sections ============================== #
    
class Section11(Section):
    section_style = 'light'
    section_title = "Terms of Use"
    section_text = "Last updated 5/11/23: </br></br>Please carefully review our Terms of Use agreement regarding utilization of the National Cybersecurity Workforce Development Program (CyberSkills2Work) website, mobile application or any of its online services. Our Terms of Use outlines appropriate behaviors expected of cyberskills2work.org visitors and notifies site users of actions that our website administrator may perform to keep our website, mobile app, and online services functioning properly.</br></br>Cyberskills2work.org is designed to educate the public about CyberSkills2Work, generate interest in the program, and attract potential participants and supporters. All information published to the website is provided in good faith and true to our knowledge. However, we do not guarantee the accuracy of information provided to us by third parties or secondary sources. Therefore, we will not assume any liability for any loss or damages incurred as result of your reliance on any third-party information provided to us and published to cyberskills2work.org or the mobile app.</br></br>By visiting cyberskills2work.org or its mobile app, you agree to our Terms of Use. We advise you to read our Terms of Use agreement in its entirety. If you do not agree to it, please discontinue use of our website and services."

class Section12(Section):
    section_style = 'dark'
    section_title = "External Links"
    section_text = "Our website might contain referring links to other websites or content from third parties. These links are provided to refer users to the original sources of information for further consideration. We do not assume responsibility for third-party websites, any misinformation that they may contain, or any damages you may incur from visiting them."

class Section13(Section):
    section_style = 'light'
    section_title = "CyberSkills2Work Application"
    section_text = "Cyberskills2work.org provides an application for entry to the CyberSkills2Work program. It collects required personal identifiable information from eligible applicants who are interested in joining the program. Applicants acknowledge that any information submitted, via the application, is accurate and can be substantiated.</br></br>All information provided by program applicants is screened and reviewed by CyberSkills2Work representatives. Our applicants’ information is not used or sold for any other purposes, except for consideration of acceptance to the CyberSkills2Work program. Applicants submitting plagiarized or misrepresented information will be rejected or dropped from the program, and denied the opportunity to reapply in the future. CyberSkills2Work does not assume liability for anyone impersonating someone else, stealing another person’s identification or misrepresenting themselves in submitted program applications."

class Section14(Section):
    section_style = 'dark'
    section_title = "MyCyberSkills2Work Portal"
    section_text = "This portal is available to all registered users of the CyberSkills2Work program. It provides a method for program learners to track their training progress, search for jobs, get course information, check the status of pursued certifications and badges, and communicate with institutions administering their education. Portal registrants must provide personal identifiable information to set up an account. Such information is not provided or sold to third parties. CyberSkills2Work retains learner information, for a minimum of three years, for program assessment and reporting in compliance with the Code of Federal Regulations (CFR), Subtitle A, Part 200.</br></br>A portal user must agree and understand that you are solely responsible for the content and activity of your personal account. You must not transmit any content that is unlawful, offensive, objectionable, threatening, or intended to cause harm to others. This includes any files that may contain viruses, malware, trojan horses or any content that is designed to disrupt, damage or restrict the portal software or website functions. We may terminate or suspend your portal account immediately, without prior notice, liability or limitation, if you breach our Terms of Use."

class Section15(Section):
    section_style = 'light'
    section_title = "Advertising"
    section_text = "Cyberskills2work.org features the logos of corporations or organizations who are major contributors. We might also hyperlink to the contributors’ websites to acknowledge their donations or contributions. However, our acknowledgement in this manner does not imply that our program endorses them or their products and services."

class Section16(Section):
    section_style = 'dark'
    section_title = "Testimonials"
    section_text = "Cyberskills2work.org features testimonials of user experiences. These testimonials reveal the personal experiences and opinions of CyberSkills2Work participants, members of its coalition of institutions and National Employers Network, and supporters. Testimonials featured on the website are submitted in various ways, including email. They are reviewed and edited for spelling or grammatical errors before they are published online. Full user statements may be condensed for brevity but appear verbatim. Published testimonials are a true representation of our users’ experiences. However, we advise site visitors not to assume that all who use our services or participate in the program will have the same results. Program outcomes may vary per person. CyberSkills2Work reserves the right to use the submitted testimonials and images of persons giving statements. They may not be reused or downloaded for any other purpose."

class Section17(Section):
    section_style = 'light'
    section_title = "Copyright Infringement"
    section_text = "The CyberSkills2Work brand and logo are used exclusively for promotion of the program by its administrators and coalition of institutions. All other use is prohibited. We reserve the right to take legal action on persons who unlawfully download or copy the CyberSkills2Work logo or attempt to represent our brand for unlawful or any other activity."

class Section18(Section):
    section_style = 'dark'
    section_title = "Age Restrictions"
    section_text = "Our CyberSkills2Work services and website are intended for people 18 years old or older. We are not required to verify user age. Therefore, when you utilize CyberSkills2Work services, you represent that you are age 18 or older. We do not accept responsibility for minors who visit cyberskills2work.org and attempt to utilize our services. Review our Privacy Policy for more information."

class Section19(Section):
    section_style = 'light'
    section_title = "Interruption of Service"
    section_text = "Our website administrator may occasionally need to temporarily shut down the website for maintenance caused by server issues. This may interrupt users’ ability to access our website or services. At such times, we will notify users of an anticipated interruption of services on the website or mobile app. Notifications regarding website maintenance or a disruption of service may appear on the cyberskills2work.org homepage."

class Section20(Section):
    section_style = 'dark'
    section_title = "Terms of Use Changes"
    section_text = "CyberSkills2Work reserves the right and sole discretion to modify our Terms of Use at any time. Any revisions will be indicated on this page, which includes a modification date. It is the responsibility of cyberskills2work.org users to routinely check our Terms of Use page for any changes."

class Section21(Section):
    section_style = 'light'
    section_title = "Contact Us"
    section_text = "If you have questions regarding our Terms of Use, please contact us at info@cyberskills2work.org."

class TOS(BaseTemplateView):
    template_name = 'info/terms/TermsPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sections = []
        sections.append(Section11.as_view()(self.request).rendered_content)
        sections.append(Section12.as_view()(self.request).rendered_content)
        sections.append(Section13.as_view()(self.request).rendered_content)
        sections.append(Section14.as_view()(self.request).rendered_content)
        sections.append(Section15.as_view()(self.request).rendered_content)
        sections.append(Section16.as_view()(self.request).rendered_content)
        sections.append(Section17.as_view()(self.request).rendered_content)
        sections.append(Section18.as_view()(self.request).rendered_content)
        sections.append(Section19.as_view()(self.request).rendered_content)
        sections.append(Section20.as_view()(self.request).rendered_content)
        sections.append(Section21.as_view()(self.request).rendered_content)
        context['sections'] = sections
        return context