```markdown
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
1. Docker set up on your machine. That's it.

### 🧭 Steps to Get Started

**Option A - Build the Docker Image Locally**:  
Navigate to the directory containing the Dockerfile and execute the following:
```
docker build -t skinguardapi .
```

Then run the Docker container:
```
docker run -p 8000:8000 skinguardapi
```

**Option B - Fetch the Docker Image Directly**:  
Instead of building the image locally, you can pull the image directly from the GitHub Container Registry:
```
docker pull ghcr.io/blakemoore9/skinguardapi/skin_lesion_api:1.0.0
```

After pulling, run the Docker container using:
```
docker run -p 8000:8000 ghcr.io/blakemoore9/skinguardapi/skin_lesion_api:1.0.0
```

**Explanation**:  
Both the commands mentioned in **Option A** and **Option B** start a new container. The `-p 8000:8000` option maps the container's port `8000` to your host machine's port `8000`, allowing you to access the application via a web browser. If you're new to Docker, understanding the `-p` option is crucial; without it, you won't be able to access the application externally.

**Dive Into the Web Interface**: Launch your favorite web browser and head over to [http://localhost:8000](http://localhost:8000).

---

This layout clearly provides two options for users: building the image themselves or pulling the pre-built image from the GitHub Container Registry.

## 📜 License

SkinGuardAPI uses the MIT License. Dive deeper into the legalities by checking the [LICENSE](./LICENSE) document.
```
