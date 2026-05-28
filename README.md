# Python Telepresence Cluster (Kubernetes + Docker)

Ce projet permet de développer une application Python localement tout en l'exécutant dans un cluster Kubernetes grâce à Telepresence.

---

## 🚀 Prérequis

Avant de commencer, assure-toi d’avoir installé :

- Docker
- Kubernetes (kubectl configuré)
- Telepresence
- Python 3.8+
- Un cluster Kubernetes fonctionnel

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/NizmoDev/python-telepresence.git
```
```bash
cd python-telepresence
```

---

### 2. Vérifier le cluster Kubernetes

```bash
kubectl get svc
```

---

## 🔌 Connexion au cluster avec Telepresence

### 1. Se connecter au cluster

```bash
telepresence connect
```

---

### 2. Intercepter le service Python

```bash
telepresence intercept python-app --port 8080:8080
```

Cela redirige le trafic du service Kubernetes vers ton application locale.

---

## 🐍 Lancer l’application en local

```bash
python app.py
```

---

## 🌐 Accès à l’application

Accès via Kubernetes (Nginx / cluster)

http://10.244.0.9/

Accès via service intercepté

http://python-app:8080/

---

## 🔍 Vérifier les intercepts

```bash
telepresence list
```

---

## 🧠 Résumé du fonctionnement

- Kubernetes héberge le service python-app
- Telepresence intercepte le trafic
- Ton code Python tourne en local
- Le cluster redirige les requêtes vers ta machine

---

## 🛑 Arrêter l’interception

```bash
telepresence quit
```

---

## 📌 Notes

- Vérifie que le port 8080 est libre
- Le service python-app doit exister dans Kubernetes

---

## 🧪 Commandes utiles

```bash
kubectl get pods
```
```bash
kubectl get svc
```
```bash
telepresence status
```
```bash
telepresence list
```

---

## 📚 Tech stack

Python
Kubernetes
Docker
Telepresence
Nginx
