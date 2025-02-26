pipeline {
    agent any  // Utilise un agent pour exécuter les étapes, ici cela peut être un agent par défaut

    environment {
        // Si tu veux ajouter des variables d'environnement ici, tu peux les définir
        // Exemple : 
        // PATH = "/usr/local/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                // Cloner le dépôt Git
                git 'https://github.com/Meeeehddiiii/password_generator/'  // Remplace par l'URL de ton dépôt
            }
        }

        stage('Set up Python') {
            steps {
                // Installer Python et les dépendances
                script {
                    sh 'python3 -m venv venv'  // Créer un environnement virtuel
                    sh '. venv/bin/activate'  // Activer l'environnement virtuel
                    sh 'pip install -r requirements.txt'  // Installer les dépendances, si tu as un fichier requirements.txt
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Exécuter les tests avec pytest ou unittest
                script {
                    // Remplacer l'appel interactif par des valeurs par défaut pour les tests
                    sh 'python3 -c "import password_generator; password_generator.generate_password(8, use_digits=True, use_specials=True)"'
                    
                    // Lance les tests unitaires (assumes tu as un fichier de tests unitaires)
                    sh 'python3 -m unittest test_password_generator.py'
                }
            }
        }
    }

    post {
        success {
            echo 'Les tests ont été réussis !'
        }
        failure {
            echo 'Les tests ont échoué.'
        }
    }
}
