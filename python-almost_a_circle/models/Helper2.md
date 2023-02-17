### Bienvenue à la ressource pour la tâche 19, File to instances
Update the class  `Base`  by adding the class method  `def load_from_file(cls):`  that returns a list of instances:

-   The filename must be:  `<Class name>.json`  - example:  `Rectangle.json`
-   If the file doesn’t exist, return an empty list
-   Otherwise, return a list of instances - the type of these instances depends on  `cls`  (current class using this method)
-   You must use the  `from_json_string`  and  `create`  methods (implemented previously)

### Décortiquer 
On va commencer par lire ligne par ligne avec des exemples
On va devoir ajouter la **class method** ``def load_from_file(cls):`` qui retourne une * liste d'instance*.
On va devoir ouvrir le fichier nommer `<Class name>.json` normalement vous le savez mais il y a un moyen, qui sont les [variables dunder](https://www.pythonmorsels.com/dunder-variables/)

```
>>> print(cls.__name__)
Rectangle
#ou
Square
```
Cela dépend de l'instance...
Si on ne trouve pas le fichier, on retourne une liste vide
```
file = "Rectangle.json" qui contient
"[{"width":1, "height":1, "x":0, "y":0, "id":90}]"
```
lorsqu'on va l'ouvrir avec ``f.read()`` on aura une string, qu'on va passer dans la fonction from_json_string() étant donner qu'on lui envoie une string de liste de dictionnaire, elle nous retourne une liste de dict (des objs)
```
for elem_dict in {resultat de json_string}:
```
il restera plus qu'a **create** (qui retournes des instances) des instances depuis la ~~**cls**~~  **classe**

```
def create(cls, **dictionary):
	""" create a new instance """
	# code code
return new_instance
```
