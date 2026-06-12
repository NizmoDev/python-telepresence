# Python Telepresence Cluster (Kubernetes + Docker)

This project shows how to develop a Python application locally while routing Kubernetes service traffic to it with Telepresence.

## Prerequisites

Before you start, make sure you have:

- Docker
- Kubernetes with `kubectl` configured
- Telepresence
- Python 3.8+
- A working Kubernetes cluster

## Installation

### 1. Clone the project

```bash
git clone https://github.com/NizmoDev/Telepresence.git
cd Telepresence
```

### 2. Check the Kubernetes cluster

```bash
kubectl get svc
```

## Connect To The Cluster With Telepresence

### 1. Connect to the cluster

```bash
telepresence connect
```

### 2. Intercept the Python service

```bash
telepresence intercept python-app --port 8080:8080
```

This redirects traffic from the Kubernetes service to your local application.

## Run The Application Locally

```bash
python app.py
```

## Access The Application

Access through Kubernetes or the cluster ingress:

```text
http://10.244.0.9/
```

Access through the intercepted service:

```text
http://python-app:8080/
```

## Check Active Intercepts

```bash
telepresence list
```

## How It Works

- Kubernetes hosts the `python-app` service.
- Telepresence intercepts the service traffic.
- Your Python code runs locally.
- The cluster redirects requests to your machine.

## Stop The Intercept

```bash
telepresence quit
```

## Notes

- Make sure port `8080` is available.
- The `python-app` service must exist in Kubernetes.

## Useful Commands

```bash
kubectl get pods
kubectl get svc
telepresence status
telepresence list
```

## Tech Stack

- Python
- Kubernetes
- Docker
- Telepresence
- Nginx
