import subprocess

def get_default_profile_uuid():
    # Lire l'UUID du profil par défaut
    result = subprocess.run(['dconf', 'read', '/org/gnome/Ptyxis/default-profile-uuid'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        return result.stdout.decode('utf-8').strip().strip("'")
    else:
        print("Erreur lors de la récupération de l'UUID du profil par défaut.")
        return None

def set_opacity(profile_uuid, opacity):
    # Modifier l'opacité du profil
    opacity_value = f"{opacity:.2f}"
    result = subprocess.run(['dconf', 'write', f'/org/gnome/Ptyxis/Profiles/{profile_uuid}/opacity', opacity_value], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Opacité du profil {profile_uuid} mise à jour à {opacity_value}")
    else:
        print("Erreur lors de la mise à jour de l'opacité.")

def main():
    profile_uuid = get_default_profile_uuid()
    if profile_uuid:
        set_opacity(profile_uuid, 0.85)

if __name__ == "__main__":
    main()
