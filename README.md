\# HPCL B2B Lead Intelligence Agent



\## Overview



This project implements an AI-powered B2B Lead Intelligence Agent designed to help HPCL identify, prioritize, and act on high-value industrial leads using publicly available signals such as tender portals, industrial expansion announcements, logistics activity, and press releases.



The system simulates ingestion, inference, scoring, and routing of industrial fuel demand leads.



\---



\## Key Features



\### 1. Signal Ingestion

Simulates ingestion of publicly available signals from:



• Government eProcurement Portals  

• GeM Tender Portal  

• Industrial expansion signals  

• Company press releases  



\---



\### 2. Product Demand Inference Engine



Maps industrial signals to HPCL products:



• Bitumen  

• Furnace Oil  

• Marine Fuel  

• HSD Diesel  

• Hexane  



Provides Top 3 product recommendations with confidence scores.



\---



\### 3. Lead Scoring Engine



Each lead is scored using:



• Signal strength  

• Industry relevance  

• Confidence level  



Outputs:



• Lead score (0–100)  

• Urgency classification (High / Medium / Low)



\---



\### 4. Lead Intelligence Dossier



Generates complete Lead Dossier containing:



• Company profile  

• Industry classification  

• Signal source  

• Signal description  

• Recommended products  

• Confidence score  

• Lead score  

• Urgency level  

• Suggested next actions  

• Sales routing simulation  



\---



\### 5. Executive Dashboard



Provides interactive dashboard with:



• Total leads  

• High priority leads  

• Confidence metrics  

• Leads by industry  

• Leads by product demand  

• Leads by signal source  

• Urgency distribution  



\---



\### 6. Explainability



Each recommendation includes:



• Signal interpretation  

• Product inference logic  

• Confidence scoring explanation  



\---



\### 7. Lead Routing Simulation



Simulates assignment to regional HPCL sales officers.



\---



\### 8. Feedback Loop Simulation



Allows simulated actions:



• Accept lead  

• Reject lead  

• Mark converted  



\---



\## Technology Stack



Frontend:

• Streamlit



Backend:

• Python



Database:

• SQLite



Data Processing:

• Pandas



\---



\## Project Structure



hpcl\_lead\_agent/



│ app.py  

│ ingestion.py  

│ inference.py  

│ scoring.py  

│ database.py  



│ data/

│   leads.db  



│ dataset/

│   signals.csv  



│ README.md  

│ requirements.txt  



\---



\## How to Run



Install dependencies:



pip install streamlit pandas



Run ingestion:



python ingestion.py



Run dashboard:



python -m streamlit run app.py



Open browser:



http://localhost:8501



\---



\## Deliverable Compliance



This project satisfies all Productathon requirements:



• Signal ingestion pipeline  

• Product inference engine  

• Lead scoring system  

• Lead dossier generation  

• Executive dashboard  

• Explainability  

• Lead routing simulation  

• Feedback loop simulation  



\---



\## Author



HPCL Productathon Submission Prototype



