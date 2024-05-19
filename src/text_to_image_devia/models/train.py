import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

print("start set tracking uri")
mlflow.set_tracking_uri("http://localhost:5000") #  connects to a tracking URI.
print("end set tracking uri")

mlflow.set_experiment("diabetes")

mlflow.autolog()
db = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
# MLflow triggers logging automatically upon model fitting
rf.fit(X_train, y_train)

# MLflow triggers logging automatically upon model evaluation
print(rf.score(X_test, y_test))



#print(tf.config.list_physical_devices('GPU'))
#print("Hello world ! Ca va ?")