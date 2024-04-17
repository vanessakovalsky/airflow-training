## Utiliser les paramètres

* Reprendre le DAG du premier exercice
* Nous voulons rendre la date d'anniversaire et le nom de la personne paramètrables
* * Définir au niveau du DAG les params : date et nom (tout deux obligatoire) : voir ici : https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html#dag-level-params
  * Dans les tâches qui ont besoin de ces informations utiliser les paramètres : https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html#referencing-params-in-a-task
* Charger votre DAG et exécuter le pour voir le résultat
