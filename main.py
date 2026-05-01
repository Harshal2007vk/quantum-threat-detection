from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import random
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataInput(BaseModel):
    value: float = Field(..., ge=0, le=1)

def quantum_analysis(value):
    qc = QuantumCircuit(1)
    if value > 0.5:
        qc.x(0)
    qc.h(0)
    state = Statevector.from_instruction(qc)
    prob_0 = abs(state.data[0])**2
    prob_1 = abs(state.data[1])**2
    results = random.choices(["0", "1"], weights=[prob_0, prob_1], k=100)
    return {
        "0": results.count("0"),
        "1": results.count("1")
    }

def detect_threat(input_value):
    quantum_result = quantum_analysis(input_value)
    count_0 = quantum_result.get('0', 0)
    count_1 = quantum_result.get('1', 0)
    total = count_0 + count_1
    if total == 0:
        return {"threat": False, "confidence": 0, "details": quantum_result}
    if count_1 > count_0:
        return {"threat": True, "confidence": count_1 / total, "details": quantum_result}
    else:
        return {"threat": False, "confidence": count_0 / total, "details": quantum_result}

@app.post("/detect")
async def detect(data: DataInput):
    return detect_threat(data.value)

@app.get("/")
async def serve_ui():
    file_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(file_path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))