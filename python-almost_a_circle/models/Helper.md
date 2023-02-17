## Bienvenue à la ressource pour la tâche 18, Dictionary to Instance

Update the class  `Base`  by adding the class method  `def create(cls, **dictionary):`  that returns an instance with all attributes already set:

-   `**dictionary`  can be thought of as a double pointer to a dictionary
-   To use the  `update`  method to assign all attributes, you must create a “dummy” instance before:
    -   Create a  `Rectangle`  or  `Square`  instance with “dummy” mandatory attributes (width, height, size, etc.)
    -   Call  `update`  instance method to this “dummy” instance to apply your real values
-   You must use the method  `def update(self, *args, **kwargs)`
-   `**dictionary`  must be used as  `**kwargs`  of the method  `update`
-   You are not allowed to use  `eval`

### Décortiquer 
On va commencer par lire ligne par ligne avec des exemples
On va devoir ajouter la fonction ``def create(cls, **dictionary):`` qui retourne une *instance* avec les attributs du dict.
On à déjà vu comment créer des instances d'une classe 
```
>>> r1 = Rectangle(1, 1)
>>> r2 = Rectangle(1, 2, 3)
```
Lorsqu'on à une instance on peut accéder au méthode (fonction) de la classe en question, Rectangle -> area() ou display(), Square -> to_dictionary(), Base -> from_json_string()
```
>>> r1.area()
1
>>> r2.display()
#
#
```
On appellera update sur notre instance
```
>>> print(r1.id)
1
>>> r1.update(90)
>>> print(r1.id)
90
```
mais ``**dictionary must be used as **kwargs of the method update``
```
>>> dict = {"id":90}
>>> r1.update(**dict)
>>> print(r1.id)
90
```
### Coller les morceaux
Donc on créer la fonction
```
>>> def create(cls, **dictionary):
	.. #si on cherche à savoir ce qu'est cls
	.. print(cls)

<class '__main__.Rectangle'>
```
Python nous dis que cls est Rectangle dans notre cas ça revient au même de faire
```
>>> Rectangle(1, 1)
>>> cls(1, 1)
```
on fait notre instance puis on l'update
```
>>> instance.update(dict)
```
Sacre bleu ! Ca ne marche pas !?
```
#output
({'x': 1, 'y': 0, 'width': 3, 'height': 5, 'id': 1}) 0/0 - 1/1
```
On a un dict() donc on met les ** pour préciser a python que l'argument est un [kwargs](https://book.pythontips.com/en/latest/args_and_kwargs.html#usage-of-kwargs)
```
>>> instance.update(**dict)
```
Il manquera plus que de **return** l'instance et *paf*
``[Rectangle] (1) 1/0 - 3/5``
##### J'espère que vous aurez compris (je ne vous donne pas le code complet évidement

