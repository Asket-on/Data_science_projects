# Построение модели определения стоимости автомобиля

### Описание проекта

Сервис по продаже автомобилей с пробегом разрабатывает приложение для привлечения новых клиентов. В нём можно быстро узнать рыночную стоимость своего автомобиля. В нашем распоряжении исторические данные: технические характеристики, комплектации и цены автомобилей. Нам нужно построить модель для определения стоимости.


### Выводы:

Были рассмотрены и проанализированы модели Linear Regression, RandomForestRegressor, LGBM и CatBoost.

Наилучший результат точности предсказания показала модель LGBM с оптимизатором Optuna: RMSE=1765, гиперпараметры: {'learning_rate': 0.2, 'n_estimators': 900, 'colsample_bytree': 0.9, 'min_child_samples': 16}, но и самую низкую скорость предсказания.

### Инструменты:

Python, Scikit-learn, LightGBM, Catboost, Pandas, NumPy, Matplotlib, Seaborn.