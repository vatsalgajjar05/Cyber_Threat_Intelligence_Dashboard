<<<<<<< HEAD
**# \*\*🛡️ Cyber Threat Intelligence Dashboard\*\***



**\*\*(Developed during Elevate Labs Internship)\*\***



**---**



**## 📌 Overview**



**The \*\*Cyber Threat Intelligence (CTI) Dashboard\*\* is a web-based security analytics platform developed as part of an internship at \*\*Elevate Labs\*\*.**

**The application aggregates real-time threat intelligence from open security APIs and presents it through an interactive dashboard.**



**It enables security analysts to \*\*analyze Indicators of Compromise (IOCs)\*\* such as IP addresses, assess threat severity, visualize trends, and monitor global threat activity in an intuitive manner.**



**---**



**## 🎯 Objective**



**The primary objective of this project is to demonstrate how real-time cyber threat intelligence can be collected, analyzed, stored, and visualized using open-source technologies.**



**The dashboard helps in:**



**\* Identifying malicious IPs**

**\* Understanding threat trends**

**\* Supporting faster and informed security decisions**



**---**



**## ✨ Key Features**



**\* 🔍 \*\*IP Threat Lookup\*\* using VirusTotal \& AbuseIPDB**

**\* 🚨 \*\*Threat Severity Classification\*\* (High / Medium / Low)**

**\* 📊 \*\*Threat Activity Trends Visualization\*\***

**\* 🌍 \*\*Global Threat Heatmap\*\* using IP geolocation**

**\* 🗂️ \*\*IOC Management\*\* (store, view, tag, delete)**

**\* 🏷️ \*\*Tagging System\*\* for better threat categorization**

**\* 📤 \*\*Export IOC Data\*\* (CSV \& JSON)**

**\* 🧑‍💻 \*\*Admin Panel\*\* for IOC management**

**\* 🌙 \*\*Dark-themed modern UI\*\***



**---**



**## 🛠️ Tools \& Technologies Used**



**### Backend**



**\* \*\*Python\*\***

**\* \*\*Flask\*\* (Web Framework)**

**\* \*\*SQLite\*\* (IOC \& Event Storage)**



**### Threat Intelligence APIs**



**\* \*\*VirusTotal API\*\* (Free Tier)**

**\* \*\*AbuseIPDB API\*\***



**### Frontend**



**\* \*\*HTML5\*\***

**\* \*\*CSS3\*\***

**\* \*\*JavaScript\*\***



**### Visualization**



**\* \*\*Chart.js\*\* (Threat trends)**

**\* \*\*Leaflet.js\*\* (Global threat heatmap)**



**---**



**## 📂 Project Structure**



**```**

**Cyber-Threat-Intelligence-Dashboard/**

**│**

**├── admin\_panel/**

**│   ├── app.py**

**│   ├── auth.py**

**│   ├── config.py**

**│   └── templates/**

**│**

**├── cti\_tool/**

**│   ├── app.py**

**│   ├── config.py**

**│   ├── services/**

**│   │   ├── virustotal.py**

**│   │   └── abuseipdb.py**

**│   ├── static/**

**│   └── templates/**

**│**

**├── database/**

**│   └── cti.db**

**│**

**├── requirements.txt**

**├── README.md**
  
**└── LICENSE**

**```**



**---**



**## ⚙️ Installation \& Setup**



**### 1️⃣ Clone the Repository**



**```bash**

**git clone https://github.com/your-username/cyber-threat-intelligence-dashboard.git**

**cd cyber-threat-intelligence-dashboard**

**```**



**### 2️⃣ Create Virtual Environment (Optional but Recommended)**



**```bash**

**python -m venv venv**

**source venv/bin/activate   # Linux/Mac**

**venv\\Scripts\\activate      # Windows**

**```**



**### 3️⃣ Install Dependencies**



**```bash**

**pip install -r requirements.txt**

**```**



**### 4️⃣ Configure API Keys**



**Add your API keys in `.env` or `config.py`:**



**```env**

**VIRUSTOTAL\_API\_KEY=your\_key\_here**

**ABUSEIPDB\_API\_KEY=your\_key\_here**

**```**



**### 5️⃣ Run the CTI Dashboard**



**```bash**

**python cti\_tool/app.py**

**```**



**### 6️⃣ (Optional) Run Admin Panel**



**```bash**

**python admin\_panel/app.py**

**```**



**---**



**## 🚀 How It Works**



**1. User submits an IP address for analysis.**

**2. Backend queries \*\*VirusTotal\*\* and \*\*AbuseIPDB\*\* APIs.**

**3. Threat scores are calculated and classified.**

**4. IOC data is stored in SQLite database.**

**5. Dashboard displays:**



   **\* Threat counts**

   **\* Activity trends**

   **\* Global heatmap**

**6. Admin panel allows managing and cleaning IOC data.**



**---**



**## 📊 Visualizations Included**



**\* 📈 \*\*Threat Activity Over Time (Line Chart)\*\***

**\* 🌍 \*\*Global Threat Heatmap\*\***

**\* 📋 \*\*Recent IOC Table with Severity Badges\*\***



**---**



**## 🔐 Security \& Limitations**



**\* Uses \*\*free-tier APIs\*\*, hence subject to rate limits**

**\* No advanced authentication (can be added in future)**

**\* Designed for \*\*educational \& internship purposes\*\***



**---**



**## 🏫 Internship Acknowledgment**



**This project was developed during an internship at \*\*Elevate Labs\*\*, focusing on:**



**\* Cyber Threat Intelligence**

**\* API Integration**

**\* Security Analytics**

**\* Dashboard Development**










=======
**# \*\*🛡️ Cyber Threat Intelligence Dashboard\*\***



**\*\*(Developed during Elevate Labs Internship)\*\***



**---**



**## 📌 Overview**



**The \*\*Cyber Threat Intelligence (CTI) Dashboard\*\* is a web-based security analytics platform developed as part of an internship at \*\*Elevate Labs\*\*.**

**The application aggregates real-time threat intelligence from open security APIs and presents it through an interactive dashboard.**



**It enables security analysts to \*\*analyze Indicators of Compromise (IOCs)\*\* such as IP addresses, assess threat severity, visualize trends, and monitor global threat activity in an intuitive manner.**



**---**



**## 🎯 Objective**



**The primary objective of this project is to demonstrate how real-time cyber threat intelligence can be collected, analyzed, stored, and visualized using open-source technologies.**



**The dashboard helps in:**



**\* Identifying malicious IPs**

**\* Understanding threat trends**

**\* Supporting faster and informed security decisions**



**---**



**## ✨ Key Features**



**\* 🔍 \*\*IP Threat Lookup\*\* using VirusTotal \& AbuseIPDB**

**\* 🚨 \*\*Threat Severity Classification\*\* (High / Medium / Low)**

**\* 📊 \*\*Threat Activity Trends Visualization\*\***

**\* 🌍 \*\*Global Threat Heatmap\*\* using IP geolocation**

**\* 🗂️ \*\*IOC Management\*\* (store, view, tag, delete)**

**\* 🏷️ \*\*Tagging System\*\* for better threat categorization**

**\* 📤 \*\*Export IOC Data\*\* (CSV \& JSON)**

**\* 🧑‍💻 \*\*Admin Panel\*\* for IOC management**

**\* 🌙 \*\*Dark-themed modern UI\*\***



**---**



**## 🛠️ Tools \& Technologies Used**



**### Backend**



**\* \*\*Python\*\***

**\* \*\*Flask\*\* (Web Framework)**

**\* \*\*SQLite\*\* (IOC \& Event Storage)**



**### Threat Intelligence APIs**



**\* \*\*VirusTotal API\*\* (Free Tier)**

**\* \*\*AbuseIPDB API\*\***



**### Frontend**



**\* \*\*HTML5\*\***

**\* \*\*CSS3\*\***

**\* \*\*JavaScript\*\***



**### Visualization**



**\* \*\*Chart.js\*\* (Threat trends)**

**\* \*\*Leaflet.js\*\* (Global threat heatmap)**



**---**



**## 📂 Project Structure**



**```**

**Cyber-Threat-Intelligence-Dashboard/**

**│**

**├── admin\_panel/**

**│   ├── app.py**

**│   ├── auth.py**

**│   ├── config.py**

**│   └── templates/**

**│**

**├── cti\_tool/**

**│   ├── app.py**

**│   ├── config.py**

**│   ├── services/**

**│   │   ├── virustotal.py**

**│   │   └── abuseipdb.py**

**│   ├── static/**

**│   └── templates/**

**│**

**├── database/**

**│   └── cti.db**

**│**

**├── requirements.txt**

**├── README.md**
  
**└── LICENSE**

**```**



**---**



**## ⚙️ Installation \& Setup**



**### 1️⃣ Clone the Repository**



**```bash**

**git clone https://github.com/your-username/cyber-threat-intelligence-dashboard.git**

**cd cyber-threat-intelligence-dashboard**

**```**



**### 2️⃣ Create Virtual Environment (Optional but Recommended)**



**```bash**

**python -m venv venv**

**source venv/bin/activate   # Linux/Mac**

**venv\\Scripts\\activate      # Windows**

**```**



**### 3️⃣ Install Dependencies**



**```bash**

**pip install -r requirements.txt**

**```**



**### 4️⃣ Configure API Keys**



**Add your API keys in `.env` or `config.py`:**



**```env**

**VIRUSTOTAL\_API\_KEY=your\_key\_here**

**ABUSEIPDB\_API\_KEY=your\_key\_here**

**```**



**### 5️⃣ Run the CTI Dashboard**



**```bash**

**python cti\_tool/app.py**

**```**



**### 6️⃣ (Optional) Run Admin Panel**



**```bash**

**python admin\_panel/app.py**

**```**



**---**



**## 🚀 How It Works**



**1. User submits an IP address for analysis.**

**2. Backend queries \*\*VirusTotal\*\* and \*\*AbuseIPDB\*\* APIs.**

**3. Threat scores are calculated and classified.**

**4. IOC data is stored in SQLite database.**

**5. Dashboard displays:**



   **\* Threat counts**

   **\* Activity trends**

   **\* Global heatmap**

**6. Admin panel allows managing and cleaning IOC data.**



**---**



**## 📊 Visualizations Included**



**\* 📈 \*\*Threat Activity Over Time (Line Chart)\*\***

**\* 🌍 \*\*Global Threat Heatmap\*\***

**\* 📋 \*\*Recent IOC Table with Severity Badges\*\***



**---**



**## 🔐 Security \& Limitations**



**\* Uses \*\*free-tier APIs\*\*, hence subject to rate limits**

**\* No advanced authentication (can be added in future)**

**\* Designed for \*\*educational \& internship purposes\*\***



**---**



**## 🏫 Internship Acknowledgment**



**This project was developed during an internship at \*\*Elevate Labs\*\*, focusing on:**



**\* Cyber Threat Intelligence**

**\* API Integration**

**\* Security Analytics**

**\* Dashboard Development**










>>>>>>> 89414639f3b6b4a3bedcf416c813773cc3adb2cd
