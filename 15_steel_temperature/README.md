# Steel end temperature prediction
### Project description
In order to optimize production costs, the metallurgical plant "Tak Zakalyaem Stal" LLC decided to reduce the consumption of electricity during the steel processing stage. Our task is to build a model that will predict the final temperature of the steel after all processing stages.


### Conclusions:
Based on the conducted research for building a model to predict the final temperature of steel after all processing stages, various machine learning models such as Linear Regression, Random Forest, LGBM, and CatBoost were considered and analyzed.

The results of the research indicate that the CatBoost model showed higher prediction accuracy, with a target metric deviation of up to 9% compared to other models. In particular, the best accuracy result was achieved by the CatBoost model with the Optuna optimizer in cross-validation:

- MAE = 6.30,
    - hyperparameters: {'iterations': 322, 'learning_rate': 0.0361, 'depth': 7, 'l2_leaf_reg': 4, 'border_count': 219, 'bagging_temperature': 0.6046957628390406, 'subsample': 0.6, 'colsample_bylevel': 0.8, 'min_child_samples': 17}.
    
On the test set, MAE = 6.34.
### Tools:

Python, Pandas, LightGBM, Catboost, Optuna