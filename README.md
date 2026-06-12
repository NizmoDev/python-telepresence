# 🚀 Python Telepresence Cluster
### Develop Locally, Run Through Kubernetes

This project demonstrates how to develop a **Python application locally** while receiving traffic from a **Kubernetes Service** using **Telepresence**.

With Telepresence, you can test and debug your application on your machine without rebuilding Docker images or redeploying to Kubernetes every time.

---

## 🛠️ Tech Stack

- 🐍 Python 3.8+
- ☸️ Kubernetes
- 📦 Docker
- 🔌 Telepresence
- 🌐 Nginx

---

## 📋 Prerequisites

Before getting started, make sure you have installed:

- ✅ Docker
- ✅ Kubernetes Cluster
- ✅ kubectl configured
- ✅ Telepresence
- ✅ Python 3.8 or later

Verify your cluster connection:

```bash
kubectl get nodes
```

---

## 📥 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/NizmoDev/Telepresence.git
cd Telepresence
```

### 2️⃣ Verify Kubernetes Services

Make sure your cluster is running correctly:

```bash
kubectl get svc
```

Expected output should include the `python-app` service.

---

## 🔗 Connect to Kubernetes with Telepresence

### 1️⃣ Connect Telepresence to the Cluster

```bash
telepresence connect
```

Check the connection status:

```bash
telepresence status
```

---

### 2️⃣ Intercept the Python Service

```bash
telepresence intercept python-app --port 8080:8080
```

🎯 What this does:

- Redirects Kubernetes traffic from `python-app`
- Forwards requests to your local machine
- Allows local development while staying connected to the cluster

---

## ▶️ Run the Application Locally

Start your Python application:

```bash
python app.py
```

Your application is now serving requests coming from Kubernetes.

---

## 🌍 Access the Application

### Through Kubernetes

```text
http://10.244.0.9/
```

### Through the Intercepted Service

```text
http://python-app:8080/
```

---

## 🔍 Monitor Active Intercepts

Display all active intercepts:

```bash
telepresence list
```

Example output:

```text
python-app: intercepted
```

---

## ⚙️ How It Works

```text
┌───────────────────┐
│ Kubernetes Client │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│  python-app SVC   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│   Telepresence    │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Local Python App  │
│     app.py        │
└───────────────────┘
```

### 🔄 Request Flow

1. A request reaches the Kubernetes Service.
2. Telepresence intercepts the traffic.
3. The request is forwarded to your local machine.
4. Your local Python application processes the request.
5. The response is sent back through Kubernetes.

---

## 🧪 Useful Commands

### Kubernetes

```bash
kubectl get pods
kubectl get svc
kubectl get deployments
```

### Telepresence

```bash
telepresence connect
telepresence status
telepresence list
telepresence quit
```

---

## 🛑 Stop the Intercept

Disconnect Telepresence and remove all active intercepts:

```bash
telepresence quit
```

---

## ⚠️ Notes

- Ensure port **8080** is available on your machine.
- The Kubernetes Service **python-app** must already exist.
- Telepresence must be connected before creating an intercept.
- Verify that your cluster is reachable from your local environment.

---

## 🎯 Benefits of Telepresence

✨ Develop locally with your favorite IDE

✨ No need to rebuild Docker images

✨ Faster debugging cycles

✨ Access real Kubernetes dependencies

✨ Test changes instantly

---

## 📚 Useful Resources

- Telepresence Documentation: https://www.telepresence.io/docs/
- Kubernetes Documentation: https://kubernetes.io/docs/
- Python Documentation: https://docs.python.org/

---

## 👨‍💻 Author

Developed by **NizmoDev** 🚀

If you find this project useful, don't forget to ⭐ the repository.
