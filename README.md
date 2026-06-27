# 💎 Diamond Price Predictor

> A machine learning web application that predicts diamond prices using a Random Forest model trained on the Kaggle Diamonds dataset (53,940 samples).

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---


---

## 🚀 Features

- Predicts diamond price based on **9 key features** (the 4Cs + physical dimensions)
- Trained on **53,940 diamonds** from the Kaggle Diamonds dataset
- REST API built with **FastAPI**
- Clean, responsive UI with animated price reveal
- Label encoding + standard scaling pipeline

---

## 🧠 Model

| Property | Detail |
|---|---|
| Algorithm | Random Forest Regressor |
| Dataset | [Kaggle Diamonds](https://www.kaggle.com/datasets/shivam2503/diamonds) |
| Training samples | 53,940 |
| Features | carat, cut, color, clarity, depth, table, x, y, z |
| Target | price (USD) |
| Preprocessing | LabelEncoder (cut, color, clarity) + StandardScaler |

---

## 📁 Project Structure

```
diamond-price-predictor/
├── app.py                      # FastAPI application
├── Diamond-Model-Complete.pkl  # Trained model + encoders + scaler
├── notebooks/
│   └── diamond_model.ipynb     # EDA & model training notebook
├── templates/
│   └── index.html              # Frontend UI
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/diamond-price-predictor.git
cd diamond-price-predictor

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn app:app --reload
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🔌 API Usage

**Endpoint:** `PATCH /predict`

```bash
curl -X PATCH http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "carat": 0.5,
    "cut": "Ideal",
    "color": "G",
    "clarity": "VS1",
    "depth": 61.5,
    "table": 55.0,
    "x": 5.09,
    "y": 5.11,
    "z": 3.13
  }'
```

**Response:**
```json
{
  "prediction_price": 1842.57
}
```

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, scikit-learn, pandas, pickle
- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Model:** Random Forest Regressor

---

## 📊 Dataset

The [Diamonds dataset](https://www.kaggle.com/datasets/shivam2503/diamonds) from Kaggle contains prices and attributes of ~54,000 diamonds.

| Feature | Description |
|---|---|
| carat | Weight of the diamond |
| cut | Quality of the cut (Fair → Ideal) |
| color | Diamond color (D=best → J=worst) |
| clarity | Clarity grade (IF=best → I1=worst) |
| depth | Total depth percentage |
| table | Width of top facet vs widest point |
| x, y, z | Physical dimensions in mm |

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ using FastAPI & scikit-learn</p>
