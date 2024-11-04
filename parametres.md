## Utiliser les paramètres

* Nous voulons rendre le nom du bucket et du fichier utilisé paramètrables
* * Définir au niveau du DAG les params : bucket et filename (tout deux de type string et obligatoire) : voir ici : https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html#dag-level-params
  * Dans les tâches qui ont besoin de ces informations utiliser les paramètres : https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html#referencing-params-in-a-task
* Charger votre DAG et exécuter le pour voir le résultat
