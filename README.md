=================================================
*												*
*				PROJET PYTHON					*
*		LECTEUR DE FLUX DE SYNDICATION			*
*												*					
=================================================



La page index.html est notre page d'accueil.
Cette page permet de :
- S'inscrire
- Se connecter

La page dashboard.html est la page personnelle d'un utilisateur. 
Sur cette page, il peut :
- Ajouter un flux
- Regarder un flux
- Supprimer un flux
- Se déconnecter

Notre base de donnée SQLITE est nommé "database"
Elle est composé de 2 tables : User(login, password) et Flux(user, lien)

Documentation utilisé : 
https://pythonhosted.org/feedparser/							-- liste des attributs/options des feeds et entries
https://p2m3ng.com/35/z6vf1-parcourir-un-flux-rss-en-python		-- tuto flux RSS
https://flask-wtf.readthedocs.io/en/stable/quickstart.html