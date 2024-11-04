## Faire passer des données d'une tâches à une autre

* Lors de l'envoi du fichier sur le bucket nous voulons récupérer l'URI du fichier et la mettre dans l'email envoyé
* Pour cela, nous allons devoir récupérer la données de la tâche de dépôt de fichier, puis la transmettre à la tâche d'envoi d'email
* Nous allons donc utiliser les Xcom pour le faire, voir un exemple ici : https://marclamberti.com/blog/airflow-xcom/
* Charger votre DAG et exécuter le pour voir le résultat

