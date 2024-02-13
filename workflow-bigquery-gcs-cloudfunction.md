# Ecrire un pipeline qui va utiliser différents services GCP

Cet exercice a pour objectif :
* d'écrire un workflow qui s'executera sur cloud composer et utilisera différent service GCP (Clouf Function, BigQuery, Google Cloud Storage)

Voici à quoi va ressembler notre pipeline dans un premier temps :

![](https://gary-yiu.com/wp-content/uploads/2023/06/Untitled-2048x561.png)

## Mise en place du DAG

* Créer un fichier DAG
* Définir les 4 étapes nécessaires et leur ordonnancement

## Récupération des données avec appel à Cloud Fonction

* Nous allons déclarer notre tache d'appel à Cloud Function en utilisant l'opérateur SimpleHTTPOperator
* Nous devons commencer par déclarer la fonction dans Cloud Function qui va nous permettre de l'utiliser dans notre workflow
* Dans la console GCP créer une cloud function, qui va télécharger les données ici : https://data.police.uk/data/ et les déposer dans un bucket GCS
* En déclencheur, choisir une requête HTTP et noter le point d'entrée.
* Revenir au fichier dag, à l'aide de la documentation https://dzone.com/articles/simplehttpoperator-in-apache-airflow, déclarer la tâche qui appelle votre fonction cloud fonctions.

(si besoin un exemple pour la fonction en python : https://gist.github.com/TimEbbers/b9d3c0a63410ba3a629a62a16126f8ba)

## Charger des données depuis un bucket GCS vers BigQuery

* A l'aide de l'opérateur GCSToBigQueryOperator https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/transfer/gcs_to_bigquery.html
* Configurer votre tache avec votre bucket, votre connexion et le projet, dataset et table de sorti

## Traiter les données

* En utilisant l'opérateur BigQueryOperator https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/bigquery.html 
* Traiter les données (vérifier les duplications par exemple)

## Aggréger les données

* Avec le même opérateur BigQueryOperator, aggréger les données

## Exécuter le pipeline

* Charger votre fichier dans le bucket de votre environnement composer
* Executer le

## Pour aller plus loin

* Voir ici pour la construction d'un tableau de bord avec Data Studio : https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/bigquery.html

## Solution : 

https://github.com/GaryYiu/shared_repo/blob/main/crime_airflow_docker/dags/london_crime_data_pipeline.py
