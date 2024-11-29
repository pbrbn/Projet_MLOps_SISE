import joblib
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Chargement des données
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Train / Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialisation du modèle
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Charger le modèle dasn un fichier pkl
joblib.dump(model, 'model.pkl')
print("Modèle entrainé et enregistrer model.pkl")