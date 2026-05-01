# 🚀 Quantum Threat Detection System

A simple full-stack project that simulates **quantum-inspired cyber threat detection** using probabilistic behavior.

---

## 🔍 Overview

This project demonstrates how concepts from quantum computing can be applied to cybersecurity.

The system:
- Takes a numeric input (0–1)
- Applies a quantum-inspired circuit
- Simulates probabilistic outcomes
- Classifies whether the input represents a potential threat

---

## 🧠 How It Works

1. Input value is received via API
2. A quantum circuit is created using Qiskit
3. Hadamard gate creates superposition
4. Conditional X gate simulates anomaly
5. Statevector probabilities are calculated
6. Random sampling simulates quantum measurement
7. Output is classified as:
   - ✅ Safe
   - ⚠️ Threat

---

## ⚙️ Tech Stack

- **Backend:** FastAPI  
- **Quantum Simulation:** Qiskit  
- **Frontend:** HTML, CSS, JavaScript  
- **API Testing:** Swagger UI  

---

## 📁 Project Structure


quantum-threat-detection/
│
├── main.py # FastAPI backend
├── index.html # Frontend UI
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🚀 How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
2. Run backend
python -m uvicorn main:app --reload
3. Open frontend

Open index.html in your browser

4. Test API

Go to:

http://localhost:8000/docs
📊 API Endpoint
POST /detect
Request:
{
  "value": 0.7
}
Response:
{
  "threat": true,
  "confidence": 0.65,
  "details": {
    "0": 35,
    "1": 65
  }
}
💡 Use Cases
Cybersecurity anomaly detection
Fraud detection systems
Risk analysis models
Educational quantum computing demos
🌍 Future Improvements
Integrate Machine Learning models
Real-time monitoring dashboard
Cloud deployment (Render / AWS)
Advanced quantum circuits
⚠️ Disclaimer

This is a quantum-inspired simulation, not a real quantum computing system.

👨‍💻 Author

Harshal

⭐ Support

If you like this project, give it a ⭐ on GitHub!


---

