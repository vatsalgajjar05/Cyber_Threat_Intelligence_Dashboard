# 🛡️ **Cyber Threat Intelligence Dashboard**
### *(Developed during Elevate Labs Internship)*

---

## 📌 **Overview**

The **Cyber Threat Intelligence (CTI) Dashboard** is a web-based security analytics platform developed as part of an internship at **Elevate Labs**.

This application aggregates real-time threat intelligence from open-source security APIs and presents it through an interactive and visually rich dashboard.

It enables security analysts to **analyze Indicators of Compromise (IOCs)** such as IP addresses, assess threat severity, visualize trends, and monitor global cyber threat activity in an intuitive manner.

---

## 🎯 **Project Objective**

The primary objective of this project is to demonstrate how **real-time cyber threat intelligence** can be:

- Collected  
- Analyzed  
- Stored  
- Visualized  

using open-source technologies.

### The dashboard helps in:
- 🔍 Identifying malicious IP addresses  
- 📊 Understanding threat trends over time  
- ⚡ Supporting faster and informed security decisions  

---

## ✨ **Key Features**

- 🔍 **IP Threat Lookup** using VirusTotal & AbuseIPDB  
- 🚨 **Threat Severity Classification** *(High / Medium / Low)*  
- 📊 **Threat Activity Trends Visualization**  
- 🌍 **Global Threat Heatmap** using IP geolocation  
- 🗂️ **IOC Management** *(store, view, tag, delete)*  
- 🏷️ **Tagging System** for better threat categorization  
- 📤 **Export IOC Data** *(CSV & JSON)*  
- 🧑‍💻 **Admin Panel** for IOC management  
- 🌙 **Dark-Themed Modern UI**

---

## 🛠️ **Tools & Technologies Used**

### 🔹 Backend
- **Python**
- **Flask** *(Web Framework)*
- **SQLite** *(IOC & Event Storage)*

### 🔹 Threat Intelligence APIs
- **VirusTotal API** *(Free Tier)*
- **AbuseIPDB API**

### 🔹 Frontend
- **HTML5**
- **CSS3**
- **JavaScript**

### 🔹 Data Visualization
- **Chart.js** *(Threat Trends)*
- **Leaflet.js** *(Global Threat Heatmap)*

---

## 📂 **Project Structure**

Cyber-Threat-Intelligence-Dashboard/
│
├── admin_panel/
│ ├── app.py
│ ├── auth.py
│ ├── config.py
│ └── templates/
│
├── cti_tool/
│ ├── app.py
│ ├── config.py
│ ├── services/
│ │ ├── virustotal.py
│ │ └── abuseipdb.py
│ ├── static/
│ └── templates/
│
├── database/
│ └── cti.db
│
├── assets/
├── requirements.txt
├── README.md
└── LICENSE


---

## ⚙️ **Installation & Setup**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Cyber_Threat_Intelligence_Dashboard.git
cd Cyber_Threat_Intelligence_Dashboard

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure API Keys

Add your API keys in .env file or config.py:

VIRUSTOTAL_API_KEY=your_key_here
ABUSEIPDB_API_KEY=your_key_here

5️⃣ Run the CTI Dashboard
python cti_tool/app.py

6️⃣ (Optional) Run Admin Panel
python admin_panel/app.py

🚀 How the System Works

User submits an IP address for analysis

Backend queries VirusTotal and AbuseIPDB APIs

Threat scores are calculated using a CTI heuristic

IOC data is stored in SQLite database

Dashboard displays:

Threat counts

Activity trends

Global threat heatmap

Admin panel allows managing, editing, and deleting IOCs

📊 Visualizations Included

📈 Threat Activity Over Time (Line Chart)

🌍 Global Threat Heatmap

📋 Recent IOC Table with Severity Badges

🔐 Security & Limitations

Uses free-tier APIs, hence subject to rate limits

No advanced authentication (can be enhanced)

Designed for educational & internship purposes

🏫 Internship Acknowledgment

This project was developed during an internship at Elevate Labs, focusing on:

Cyber Threat Intelligence

API Integration

Security Analytics

Dashboard Development

