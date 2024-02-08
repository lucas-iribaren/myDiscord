from files.class_py.database import Database

class Page_Connexion(Database):
    def __init__(self):
        Database.__init__(self, "localhost", "root", "1478", "mydiscord")
    
    def verify_account_exist(self, pseudo_entry, password_entry):
        # Vérifier si les entrées ne sont pas vides
        if pseudo_entry and password_entry:
            # Récupérer les informations de l'utilisateur à partir de la base de données
            user_data = self.fetch_one("SELECT pseudo, password FROM user WHERE pseudo = ?;", (pseudo_entry,))
            if user_data:
                # Si l'utilisateur est trouvé dans la base de données, vérifier le mot de passe
                if user_data[1] == password_entry:
                    return True  # Si le mot de passe correspond, retourner True
        return False  # Si aucune correspondance n'est trouvée, retourner False

            
    
            
    
            
            
            
    