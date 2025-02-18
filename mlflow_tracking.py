import mlflow

mlflow.start_run()
mlflow.log_param("model", "RandomForest")
mlflow.log_metric("accuracy", 0.85)
mlflow.end_run()
