## Ajouter une notification par mail

* Reprendre le DAG de l'exercice précédent
* Nous voulons ensuite ajouter une notification par email lorsque notre DAG a terminé (quelque soit le résultat).
* Pour cela :
* * : Configurer votre environnement composer pour pouvoir envoyer des emails : https://cloud.google.com/composer/docs/configure-email?hl=fr
  * Ajouter une tache d'envoi d'email avec l'opérateur Emailoperator (vous avez un exemple dans lien ci dessus)
* Charger votre DAG et exécuter le pour voir le résultat


## Utiliser les templates

* Lors de l'envoi du mail nous voulons ajouter certains paramètres dans le corps du mail
* * Récupérer dans les templates disponibles https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html les paramètres suivants :
  * Id du DAG run
  * Nom du dag
  * Instance de la tâche
  * Afficher ces paramètres dans le corps du mail envoyé
* Charger votre DAG et exécuter le pour voir le résultat
