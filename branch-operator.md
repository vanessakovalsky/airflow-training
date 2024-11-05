## Ajouter des conditions et utiliser le BranchOperator

* Ensuite nous voulons ajouter une condition à notre DAG : Si le fichier data/demo.txt est présent dans notre bucket, alors on continue le traitement, sinon on appelle on charge le fichier dans le bucket
* Pour cela :
* * Utiliser un branch operateur qui va vérifier notre condition : https://docs.astronomer.io/learn/airflow-branch-operator 
  * Pour vérifier la présence d'un fichier sur un bucket on peut utiliser GCSObjectExistenceSensor : https://registry.astronomer.io/providers/google/versions/latest/modules/gcsobjectexistencesensor
 
* Charger votre DAG et exécuter le pour voir le résultat

