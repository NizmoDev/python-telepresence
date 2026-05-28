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

git clone <URL_DU_REPO>
cd python-telepresence

---

### 2. Vérifier le cluster Kubernetes

kubectl get svc

---

## 🔌 Connexion au cluster avec Telepresence

### 1. Se connecter au cluster

telepresence connect

---

### 2. Intercepter le service Python

telepresence intercept python-app --port 8080:8080

Cela redirige le trafic du service Kubernetes vers ton application locale.

---

## 🐍 Lancer l’application en local

python app.py

---

## 🌐 Accès à l’application

Accès via Kubernetes (Nginx / cluster)

http://10.244.0.9/

Accès via service intercepté

http://python-app:8080/

---

## 🔍 Vérifier les intercepts

telepresence list

---

## 🧠 Résumé du fonctionnement

- Kubernetes héberge le service python-app
- Telepresence intercepte le trafic
- Ton code Python tourne en local
- Le cluster redirige les requêtes vers ta machine

---

## 🛑 Arrêter l’interception

telepresence quit

---

## 📌 Notes

- Vérifie que le port 8080 est libre
- Le service python-app doit exister dans Kubernetes

---

## 🧪 Commandes utiles

kubectl get pods
kubectl get svc
telepresence status
telepresence list

---

## 📚 Tech stack

Python
Kubernetes
Docker
Telepresence
Nginx
