# **lpgdlcFontDuLinux**

Membres du projet : Paul BOUQUET - Cédric DELAUNAY - Thomas LE MASSON

## **Projet de Linux embarqué : contrôle d'un serveur Caméra et d'un serveur Servomoteur depuis un client déporté**

Répertoires :

- Client : contient le client python

- Serveur_Caméra : contient le serveur Caméra et le binaire cross-compilé v4lgrab

- Serveur_Servo  : contient le serveur contrôlant le servo-moteur

# **Démarrage rapide**

- Pour le serveur caméra, les binaires sont déjà compilés. Vous pouvez donc transférer les deux
  exécutables sur la Raspberry, et lancer le serveur Caméra (par défaut, il est en écoute sur le
  port 8002). Si vous voulez recompiler le serveur caméra, il vous suffit de copier le dossier
  ServeurCamera/ dans le docker contenant le cross-compilateur, et d'utiliser le Makefile.

- Pour le serveur servo-moteur, copiez le dossier sur la Raspberry, et exécutez ... 

- Pour le client python, lancez le simplement avec en paramètres l'ip de la raspberry, le port du
  serveur caméra et le port du serveur servo-moteur. Suivez ensuite les instructions affichées dans
  votre console.


# **Client Python**

# **Serveur Python**

Ce serveur permet de faire la liaison entre le client et le servomoteur.

Le serveur n'accepte qu'**une seule connection** jusqu'à la fin de son exécution.

On peut lancer le serveur sur le port et sur la pin de la raspeberry que l'on souhaite.

Par défaut, le serveur se lance sur le **port 6667** et la **pin 11** de la raspberry. [plan
raspberry](schema_raspeberryPI3)

Les commandes reçues par le serveur sont ensuite envoyées et traitées par le servomoteur.

Les signaux **SIGINT**, **SIGSTP**, **SIGQUIT** et **SIGTERM** sont gérés et arrêtent correctement
le serveur (On arrête le servomoteur. Puis, on coupe la connection avec le client. Enfin, la socket
est fermée). scoket est fermé)

Si aucune commande n'est envoyée, le serveur s'arrête.

# **Serveur Caméra**

# **Serveur Servomoteur**

On initialise le servomoteur à la position "0". C'est-à-dire, qu'il n'y pas d'angle entre la
référence de mesure des angles et l'axe du servomoteur. [documentation
constructeur](documentation_MicroServoSG90)

Le servomoteur reçoit les commandes du serveur sous forme de chaîne de caractère.

Cette chaîne de caractère est analysée à l'aide d'un **regex** pour déterminer si la commande est
correcte ou pas.

Si la commande n'est pas correte, une erreur est levée et la commande non interprétée est affichée
dans la console. Une mauvaise commande n'arrête pas le serveur, ni le servomoteur.

Si la commande est correcte, le servomoteur l'exécute.

La seule commande dsiponible est **MOVE**, suivie d'un numéro qui peut être négatif.

**Example de commande valide :** MOVE65, MOVE-16.

Le numéro représente, en degré, l'angle que l'on va rajouter à sa position actuelle.

**Example de fonctionnement :**

| Commandes consécutives | Position |
| ---------------------- | :------: |
| ```init```             |    0     |
| MOVE15                 |    15    |
| MOVE-45                |   -30    |


# **Axes d'amélioration**

- Lancer les serveurs au démarrage de la Raspberry

- Rajouter plus de commandes : EXIT, INIT, LOOP ...

[schema_raspeberryPI3]:
https://docs.microsoft.com/en-us/windows/iot-core/media/pinmappingsrpi/rp2_pinout.png

[documentation_MicroServoSG90]:
http://www.ee.ic.ac.uk/pcheung/teaching/de1_ee/stores/sg90_datasheet.pdf

