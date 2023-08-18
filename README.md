# 🛡️ SkinGuardAPI

SkinGuardAPI is a state-of-the-art application leveraging FastAPI to facilitate skin lesion detection. Whether you're a dermatologist or an individual seeking preliminary checks on skin lesions, our platform provides you with an intuitive drag-and-drop interface, instant predictions, and insightful confidence scores, making it an essential first step in the diagnostic journey.

## 📸 Screenshot

![SkinGuardAPI Screenshot](SkinGuardPro.png)

## ✨ Features

- 🖱️ **Drag-and-Drop Interface**: Seamless image uploads have never been easier.
- 🧠 **Deep Learning Predictions**: Benefit from a sophisticated deep learning model ensuring precise results.
- 📊 **Confidence Scores**: Delve into the rationale with insightful scores indicating prediction reliability.
- 🔮 **Guidance System**: Receive informed recommendations based on the prediction's confidence score.

## 🚀 Installation & Setup

### 📋 Prerequisites

1. Docker set up on your machine.
2. Git LFS for managing those bulky model files.

### 🧭 Steps to Get Started

1. **Clone the Repository with LFS**:
    ```bash
    git lfs clone https://github.com/BlakeMoore9/SkinGuardAPI.git
    ```

2. **Build the Docker Image**:
    ```bash
    docker build -t skinguardapi .
    ```

3. **Run the Docker Container**:
    ```bash
    docker run -p 8000:8000 skinguardapi
    ```

4. **Dive Into the Web Interface**: Launch your favorite web browser and head over to [http://localhost:8000](http://localhost:8000).

📦 **Fetch the Docker Image Directly**:
```bash
docker pull ghcr.io/blakemoore9/skinguardapi/skin_lesion_api:1.0.0
```

## 📜 License

SkinGuardAPI proudly uses the MIT License. Dive deeper into the legalities by checking the [LICENSE](./LICENSE) document.
