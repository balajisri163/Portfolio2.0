from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings


def home(request):
    context = {
        'name': 'Balaji Ramachandran',
        'title': 'IoT Solutions Engineer',
        'location': 'Dubai, UAE',
        'email': 'balajisri163@gmail.com',
        'phone': '+971 562669545',
        'formal_photo': 'Formal Pic.jpg',
        'summary': (
            "A Research Engineer with nearly 4 years at DEWA's R&D Centre and 8+ years of total "
            "experience in IoT, Edge AI, and Software Engineering. Published 10 peer-reviewed "
            "papers across IEEE and ASME international conferences — including a Best Paper Award "
            "at EECCIS 2024 — with 4 papers in progress. Led the end-to-end R&D and development "
            "of the OmniHub IoT Terminal, recognised with the Nujoom Award 2024 and Engineering "
            "Product of the Year, alongside 15+ IoT use cases spanning energy, smart "
            "infrastructure, and sustainability."
        ),
        'about_highlights': [
            'Research Engineer at DEWA R&D Centre with 8+ years total experience.',
            '10 peer-reviewed IEEE / ASME publications, with 4 more in progress.',
            'Led the OmniHub IoT Terminal — Engineering Product of the Year 2026.',
            'Mentored 10+ engineers and represented DEWA at international events.',
            'UAE Golden Visa holder, currently transitioning to Senior Researcher.',
        ],
        'skills': {
            'Programming': ['Python', 'Java', 'PHP', '.NET', 'C++'],
            'Web & Mobile': ['HTML5', 'CSS', 'JavaScript', 'Android'],
            'Data Analysis': ['Pandas', 'NumPy', 'OpenCV', 'Scikit-learn', 'Matplotlib', 'Seaborn', 'Streamlit', 'Plotly', 'D3.js'],
            'Frameworks & Libraries': ['Flask', 'FastAPI', 'TensorFlow', 'Keras', 'PyTorch', 'TFLite', 'Selenium', 'Postman'],
            'Hardware Platforms': ['Raspberry Pi', 'Arduino', 'IIOT Gateways', 'Linux', 'Jetson Nano'],
            'Cloud & DevOps': ['AWS', 'Azure', 'GCP', 'Docker', 'Kubernetes', 'GitHub', 'Grafana', 'Jenkins'],
            'Machine Learning': ['AI Frameworks', 'Edge-based AI', "LLM's & Chatbots (OpenAI)"],
            'IIoT & Edge Systems': ['ThingsBoard', 'Azure IoT', 'Cumulocity', 'MQTT/Modbus', 'Edge Gateways', 'Secure Device-Cloud'],
            'R&D': ['Research Methodology', 'Technical Writing', 'Prototype Development & Testing'],
            'Vertical Expertise': ['Energy & Utilities', 'Industrial IoT', 'Smart Infrastructure', 'Telecom', 'Government', 'Fintech'],
        },
        'education': [
            {
                'degree': 'Master of Science: Engineering Management',
                'school': 'Middlesex University',
                'location': 'United Arab Emirates',
                'period': 'Sep 2018 - Dec 2019',
                'result': 'First Class with Distinction',
            },
            {
                'degree': 'B.E: Electrical and Electronics Engineering',
                'school': 'Anna University',
                'location': 'India',
                'period': 'Aug 2012 - Apr 2016',
                'result': 'First Class with Distinction',
            },
        ],
        'experience': [
            {
                'role': 'Research Engineer',
                'company': 'Dubai Electricity and Water Authority (DEWA)',
                'location': 'Dubai, UAE',
                'period': 'Jul 2022 - Present',
                'points': [
                    'Conducted applied R&D across 15+ edge AI and IoT use cases for the utility sector — feasibility studies, prototype development, field validation, and production deployment.',
                    "Led the full R&D lifecycle of the OmniHub IoT Terminal, from concept and research through to a production-deployed, award-winning multi-protocol device.",
                    'Published 10 peer-reviewed papers in IEEE and ASME international conferences on edge AI, IoT architectures, satellite communication, power quality, and energy forecasting.',
                    'Established IIoT standards, cybersecurity controls, and data integration frameworks ensuring secure, scalable, industry-compliant deployments.',
                    'Served as technical research lead bridging business stakeholders, OEM vendors, and engineering teams — translating KPIs into research proposals and vendor evaluation frameworks.',
                    'Mentored 10+ engineers and interns in IoT and edge AI research methodologies, and represented DEWA at international events.',
                    "3 internal invention disclosures submitted, contributing to the organisation's IP pipeline.",
                ],
            },
            {
                'role': 'Software Developer',
                'company': 'Future Trend LLC',
                'location': 'Dubai, UAE',
                'period': 'Jan 2019 - Dec 2021',
                'points': [
                    'Executed Employee Attendance projects deployed and used by multiple government ministries of UAE.',
                    'Worked as a Scrum Master to deliver Enterprise Projects as part of an Agile Team.',
                    'Developed Backend applications integrating SDKs of modern facial recognition and biometric devices.',
                    'Provided Technical Leadership to the development team.',
                ],
            },
            {
                'role': 'Senior System Engineer',
                'company': 'Infosys Limited',
                'location': 'Trivandrum, India',
                'period': 'Jun 2016 - Aug 2018',
                'points': [
                    'Implemented development, validation, and support activities for automation and web development tools.',
                    'Designed, developed, and deployed backend services with high availability and scalability.',
                    'Developed web applications handling high volumes of data and backend services.',
                    'Applied test-driven and behavior-driven development across the Software Testing Lifecycle.',
                    'Emphasized cloud deployment and DevOps practices for efficient and reliable software delivery.',
                ],
            },
        ],
        'projects': [
            {
                'name': 'Satellite Image based Survey through AI',
                'desc': 'AI-driven satellite image analysis pipeline classifying construction activity across Dubai, with parcel-level GIS integration and end-to-end model deployment framework.',
                'tags': ['AI', 'GIS', 'Satellite'],
            },
            {
                'name': 'SDI Water Quality Monitoring Station',
                'desc': 'Integrated dashboard for three sensing stations (SCAN, Algae Online, Coliminder) using OmniHub IoT Terminal with LoRa and LTE connectivity.',
                'tags': ['IoT', 'LoRa', 'LTE'],
            },
            {
                'name': 'EFI Fault Monitoring',
                'desc': '5 field-ready prototypes for real-time Earth Fault Indicator monitoring in substations using OmniHub IoT Terminal, currently under field evaluation.',
                'tags': ['IoT', 'Substations', 'Edge'],
            },
            {
                'name': 'DEWA Borewell Monitoring System',
                'desc': 'Customised water-level sensor for deployment across 400 borewells in Dubai, eliminating manual inspection entirely.',
                'tags': ['IoT', 'Water', 'Sensors'],
            },
            {
                'name': 'Low-Power IoT Water Metering Terminal',
                'desc': 'End-to-end M-Bus water meter reading solution transmitting data via NB-IoT, enabling real-time monitoring.',
                'tags': ['NB-IoT', 'M-Bus', 'Metering'],
            },
            {
                'name': 'Smart IoT Device with Mobile App',
                'desc': 'Field-crew smart device integrating thermal cameras, Bluetooth measurement tools, and AI anomaly detection — reducing substation condition monitoring from 30 to 15 minutes.',
                'tags': ['AI', 'Mobile', 'Thermal'],
            },
            {
                'name': 'Smart Crew Dispatch',
                'desc': 'Centralized simulation dashboard for near real-time field crew status and job tracking, with automated notifications and email alerts to improve dispatch efficiency.',
                'tags': ['Dashboard', 'Real-time', 'Operations'],
            },
            {
                'name': 'OmniHub Certification & Commercialisation',
                'desc': 'Led end-to-end CE certification with the vendor, ensuring international compliance, and driving commercial market entry in partnership with Infrax.',
                'tags': ['CE', 'Product', 'Commercialisation'],
            },
            {
                'name': 'SGS Power Harmonic Filter Monitoring',
                'desc': 'IoT-based dashboard for continuous monitoring of harmonic filters and power quality parameters in substations, with periodic LTE data transmission and automated alerts.',
                'tags': ['Power Quality', 'LTE', 'Dashboard'],
            },
            {
                'name': 'Energy Disaggregation',
                'desc': 'Custom edge device with AI algorithms for high-frequency appliance energy disaggregation at 80% accuracy, deployed in 15 homes with web and mobile applications.',
                'tags': ['Edge AI', 'Energy', 'Mobile'],
            },
            {
                'name': 'Load Forecasting Dashboard',
                'desc': 'Python-based web dashboard integrating AI models to forecast feeder loads using 5 years of historical data from 20 substations, with interactive ML metrics and mapping.',
                'tags': ['AI', 'Forecasting', 'Python'],
            },
            {
                'name': 'Decision Support System',
                'desc': 'Software architecture for load forecasting and energy KPI analysis using 10,000 customer meter records, enabling region, community and building level comparisons.',
                'tags': ['Analytics', 'Big Data', 'AI'],
            },
            {
                'name': 'Green Hydrogen Monitoring',
                'desc': "Remote dashboard for battery systems at MENA's first Green Hydrogen plant — Tesla lithium-ion (1.21 MW) and NaS (1.2 MW) state of charge.",
                'tags': ['Green Energy', 'Battery', 'Dashboard'],
            },
            {
                'name': 'Tesla Powerwall Telemetry System',
                'desc': 'Real-time telemetry system to monitor battery SoC, voltage, current, and temperature across Tesla Powerwall units.',
                'tags': ['Telemetry', 'Battery', 'IoT'],
            },
            {
                'name': 'Substation Monitoring Blueprint',
                'desc': 'Architected a scalable solution to expand real-time telemetry coverage from 15 to 1,000+ substations — covering edge telemetry, data pipeline design, and cloud observability.',
                'tags': ['Architecture', 'Scale', 'Observability'],
            },
            {
                'name': 'OmniHub IoT Terminal',
                'desc': "Led end-to-end development of DEWA's proprietary multi-protocol IoT terminal supporting LoRa Satellite, LoRaWAN, LTE CAT-M, NB-IoT, Wi-Fi, Bluetooth, RS485, and GPIO — solar-capable with custom industrial firmware.",
                'tags': ['IoT', 'Hardware', 'Multi-Protocol'],
            },
            {
                'name': '3U Nano-Satellite Integration',
                'desc': "LoRa-based IoT terminal connectivity with DEWA's first nano-satellite DEWASAT-1, demonstrating three utility use cases with ongoing scale-up.",
                'tags': ['Satellite', 'LoRa', 'IoT'],
            },
            {
                'name': 'Power Quality Monitoring',
                'desc': 'IoT-based real-time power quality analysis via LTE CAT-M, deployed in substations with automated alarm generation for abnormal events.',
                'tags': ['Power Quality', 'LTE CAT-M', 'IoT'],
            },
        ],
        'publications': [
            'Ramachandran, B. et al., "Real-Time Power Quality Monitoring in Dubai: A Comparative Study of LoRa Satellite, LoRaWAN, and LTE CAT-M Technologies," IEEE AICT 2025.',
            'Dua, G. S., Ramachandran, B. et al., "Smart Crew Dispatch System in Distribution Networks: A Digital Simulation Approach," IEEE ICITCOM 2025.',
            'Vohra, M., Ramachandran, B. et al., "Web-Controlled GPR System for Remote Data Acquisition and Surface Reflection Suppression," IEEE AICT 2025.',
            'Ramachandran, B. et al., "IoT Enabled Power Quality Monitoring in Substations through LoRa LEO Satellite Communication," IEEE EECCIS 2024. — Best Paper Award.',
            'Ramachandran, B. et al., "Enhancing Distribution Network Reliability through IoT-Driven Alarm Systems," IEEE ICSPIS 2024.',
            'Chikte, R., Ramachandran, B. et al., "Short-Term Time Series Energy Forecasting for Smart Buildings Using Machine Learning Models," ASME IMECE 2024.',
            'Ramachandran, B. et al., "Improvement of Direct Communication to Satellite Using LoRa-FHSS Compared to LoRa-CSS (DEWASAT-1)," IEEE MTTW 2023.',
            'Ramachandran, B. et al., "IoT-Based Test Facility for a Water Transmission Line with Leak Simulation," IEEE ITIKD 2023.',
            'Subramanian, V., Ramachandran, B. et al., "Hardware Doppler Shift Emulation and Compensation for LoRa LEO Satellite Communication," IEEE ITIKD 2023.',
            'Haitaamar, Z. N., Ramachandran, B. et al., "Design, Development, and Implementation of IoT-Enabled Laboratory," IEEE ITIKD 2023.',
        ],
        'awards': [
            {'title': 'Engineering Product of the Year', 'year': '2026', 'desc': 'Digital Engineering Award - OmniHub IoT Terminal'},
            {'title': 'Best Collaborator Award', 'year': '2025', 'desc': 'R&D Center - Cross-department Collaboration'},
            {'title': 'Quality Achievement Award', 'year': '2025', 'desc': 'CE Certification - IoT Terminal'},
            {'title': 'Nujoom Award', 'year': '2024', 'desc': 'Best Technical Project - OmniHub IoT Terminal'},
            {'title': 'Best Paper Award', 'year': '2024', 'desc': 'PQA Monitoring - EECCIS Conference'},
            {'title': 'Best Ideation Session Award', 'year': '2024', 'desc': 'Innovation & Invention Disclosures'},
        ],
        'gallery': [
            {'file': 'AICT Conference 2025.jfif', 'title': 'AICT Conference 2025', 'caption': 'Presenting research at IEEE AICT 2025.'},
            {'file': 'WETEX 2025.jfif', 'title': 'WETEX 2025', 'caption': 'Representing DEWA at WETEX 2025.'},
            {'file': 'GETEX 2025.jfif', 'title': 'GETEX 2025', 'caption': 'Showcasing OmniHub at GETEX 2025.'},
            {'file': 'Al Baheth Presentation.jfif', 'title': 'Al Baheth Presentation', 'caption': 'Al Baheth research presentation.'},
            {'file': 'EECCIS Conference 2024.jfif', 'title': 'EECCIS 2024', 'caption': 'Best Paper Award presentation at IEEE EECCIS 2024.'},
            {'file': 'ICSPIS 2024.jfif', 'title': 'ICSPIS 2024', 'caption': 'Paper presentation at IEEE ICSPIS 2024.'},
            {'file': 'Innovation Week 2023.jfif', 'title': 'Innovation Week 2023', 'caption': 'DEWA Innovation Week 2023.'},
            {'file': 'Engineering Product of the year Award.jfif', 'title': 'Engineering Product of the Year', 'caption': 'Receiving the Digital Engineering Award for the OmniHub IoT Terminal.'},
            {'file': 'Nujoom Award 2024.jfif', 'title': 'Nujoom Award 2024', 'caption': "DEWA's internal Best Technical Project award."},
            {'file': 'Best Paper Award 2024.png', 'title': 'Best Paper Award 2024', 'caption': 'Best Paper Award at IEEE EECCIS 2024.'},
            {'file': 'Best Colloborator Award.jpg', 'title': 'Best Collaborator Award', 'caption': 'Cross-department collaboration recognition.'},
        ],
    }
    return render(request, 'portfolio/home.html', context)


def download_resume(request):
    file_path = settings.MEDIA_ROOT / 'Balaji Ramachandran 2026.pdf'
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Balaji_Ramachandran_Resume_2026.pdf')