Python Telepresence Cluster (Kubernetes + Docker)

DESCRIPTION
Ce projet permet de développer une application Python en local tout en l’exécutant dans un cluster Kubernetes grâce à Telepresence.

PREREQUIS

Avant de commencer, installer :
- Docker
- Kubernetes (kubectl configuré)
- Telepresence
- Python 3.8 ou plus
- Un cluster Kubernetes fonctionnel

INSTALLATION

1. Cloner le dépôt :
git clone https://github.com/NizmoDev/python-telepresence.git
cd python-telepresence

2. Vérifier l’accès au cluster Kubernetes :
kubectl get svc

CONNEXION AU CLUSTER AVEC TELEPRESENCE

1. Se connecter au cluster :
telepresence connect

2. Intercepter le service Kubernetes :
telepresence intercept python-app --port 8080:8080

Cela redirige le trafic du service Kubernetes vers ton application locale.

EXECUTION LOCALE

Lancer l’application Python :
python app.py

ACCES A L’APPLICATION

Accès via Kubernetes :
http://10.244.0.9/

Accès via service intercepté :
http://python-app:8080/

VERIFICATION

telepresence list

RESUME DU FONCTIONNEMENT

- Kubernetes héberge le service python-app
- Telepresence intercepte le trafic réseau
- Le code Python tourne en local
- Le cluster redirige les requêtes vers la machine locale

ARRET

telepresence quit

COMMANDES UTILES

kubectl get pods
kubectl get svc
telepresence status
telepresence list

STACK TECHNIQUE

- Python
- Kubernetes
- Docker
- Telepresence
- Nginx
