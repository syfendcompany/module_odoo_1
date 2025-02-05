# FILE: /woodworking_workshop/__init__.py

# Ce fichier initialise le module Woodworking Workshop et importe tous les composants nécessaires.

# Import des modèles principaux
from . import models

# Import des contrôleurs (pour les fonctionnalités web ou API)
from . import controllers

# Import des vues (XML) pour l'interface utilisateur
from . import views

# Import des données de démonstration (pour les tests et la présentation)
from . import data

# Import des fichiers de sécurité (groupes, règles d'accès)
from . import security

# Import des assistants (wizards) pour les processus complexes
from . import wizard


# Import des tests unitaires (pour vérifier le bon fonctionnement du module)
from . import tests


# Documentation du module
"""
Module Odoo pour la gestion d'un atelier de menuiserie.

Ce module permet de :
- Gérer les produits personnalisables et leurs attributs.
- Supporter les assemblages complexes multi-niveaux.
- Intégrer la documentation technique (fichiers Excel et 3D).
- Assurer une cohérence totale avec les autres modules Odoo (MRP, Stock, Sale).
- Préparer les bases pour de futures intégrations (MES, automates).

Pour plus d'informations, consultez la documentation technique.
"""