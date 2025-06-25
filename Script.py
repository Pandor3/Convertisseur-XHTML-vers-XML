import os
import shutil

# Initialisation du script
converted_count = 0
skipped_count = 0
errors = []

# Définition des chemins
base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(base_dir, "Fichiers à convertir")
output_dir = os.path.join(base_dir, "Fichiers convertis")

# Création du dossier d'entrée si il n'existe pas
os.makedirs(input_dir, exist_ok=True)

# Création du dossier de sortie si il n'existe pas
os.makedirs(output_dir, exist_ok=True)

print("\n[Début de la conversion des fichiers .xhtml vers .xml]\n")

# Traitement des fichiers
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".xhtml"):
        try:
            source_path = os.path.join(input_dir, filename)
            new_filename = os.path.splitext(filename)[0] + ".xml"
            target_path = os.path.join(output_dir, new_filename)

            shutil.copyfile(source_path, target_path)
            print(f"Converti : {filename} -> {new_filename}")
            converted_count += 1
        
        except Exception as e:
            print(f"Erreur lors de la conversion de {filename} : {e}")
            errors.append((filename, str(e)))
    
    else:
        skipped_count += 1

# Résumé des opérations
print("\n[Résumé de la conversion]")

if not os.listdir(input_dir):
    print("Le dossier 'Fichiers à convertir' a été créé mais il est vide.")
    print("Ajoutez des fichiers .xhtml dans le dossier 'Fichiers à convertir' puis relancez le script.")

if converted_count > 0:
    print(f"{converted_count} fichiers(s) converti(s) avec succès.")
else:
    print("Aucun fichier converti.")

if skipped_count > 0:
    print(f"{skipped_count} fichier(s) ignoré(s) (pas au format .xhtml).")

if errors:
    print(f"{len(errors)} erreur(s) rencontrée(s) :")
    for name, err in errors:
        print(f" - {name} : {err}")
else:
    print("Aucune erreur rencontrée.")

print("\n[Fin du script, vous pouvez fermer l'application et regarder dans le dossier 'Fichiers convertis']\n")