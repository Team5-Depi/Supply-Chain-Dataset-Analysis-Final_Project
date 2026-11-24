"""Days_For_Shipping_Real (Regression)"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DataCoSupplyChain_Cleaned.csv", encoding="latin-1")
data = df.drop(columns=["Days for shipping (real)"])
y_dfs = df["Days for shipping (real)"]

"""dropping columns"""

ids = ["Category Id", "Customer Id", "Department Id", "Order Id", "Order Item Id", "Product Card Id"]
too_many_values = ["Customer City", "Order City", "Order State", "Order Country", "Product Name"]
leakage = ['Delivery Status', 'Late_delivery_risk', 'shipping date (DateOrders)', 'Order Status', 'Order Item Profit Ratio', 'Order Item Total']
data = data.drop(columns=ids + too_many_values + leakage, errors="ignore")

"""feature engineering"""

data["order date (DateOrders)"] = pd.to_datetime(data["order date (DateOrders)"])
data["order_year"] = data["order date (DateOrders)"].dt.year
data["order_month"] = data["order date (DateOrders)"].dt.month
data["order_weekday"] = data["order date (DateOrders)"].dt.dayofweek
data = data.drop(columns=["order date (DateOrders)"])

"""split data"""

from sklearn.model_selection import train_test_split

X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    data, y_dfs, test_size=0.2, random_state=42
)

num_cols = X_train_raw.select_dtypes(include="number").columns
cat_cols = X_train_raw.select_dtypes(exclude="number").columns

"""preprocessing"""

from sklearn.preprocessing import StandardScaler, OneHotEncoder

scaler = StandardScaler()
X_train_num = pd.DataFrame(scaler.fit_transform(X_train_raw[num_cols]), columns=num_cols, index=X_train_raw.index)
X_test_num = pd.DataFrame(scaler.transform(X_test_raw[num_cols]), columns=num_cols, index=X_test_raw.index)

encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
X_train_cat = pd.DataFrame(encoder.fit_transform(X_train_raw[cat_cols]), columns=encoder.get_feature_names_out(), index=X_train_raw.index)
X_test_cat = pd.DataFrame(encoder.transform(X_test_raw[cat_cols]), columns=encoder.get_feature_names_out(), index=X_test_raw.index)

X_train_full = pd.concat([X_train_num, X_train_cat], axis=1)
X_test_full = pd.concat([X_test_num, X_test_cat], axis=1)

"""feature selection"""

from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import LinearRegression

selector = SequentialFeatureSelector(LinearRegression(), n_features_to_select=10, direction="forward", cv=3)
selector.fit(X_train_full, y_train)
selected_cols = list(X_train_full.columns[selector.get_support()])
print(selected_cols)

X_train = X_train_full[selected_cols]
X_test = X_test_full[selected_cols]

"""model 1: linear regression"""

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

"""prediction"""

dfs_results = {}
dfs_predictions = pd.DataFrame({"Order Item Id": df.loc[y_test.index, "Order Item Id"], "Actual": y_test})
y_pred = model_lr.predict(X_test)
dfs_predictions["Linear Regression"] = y_pred

"""evaluation"""

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

dfs_results["Linear Regression"] = {
    "R2": r2_score(y_test, y_pred),
    "MSE": mean_squared_error(y_test, y_pred),
    "MAE": mean_absolute_error(y_test, y_pred),
}
print(dfs_results["Linear Regression"])

plt.scatter(y_test, y_pred, alpha=0.3)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted - Linear Regression")
plt.show()

"""model 2: decision tree before tuning"""

from sklearn.tree import DecisionTreeRegressor, plot_tree

model_dt_base = DecisionTreeRegressor(random_state=42)
model_dt_base.fit(X_train, y_train)

"""prediction"""

y_pred = model_dt_base.predict(X_test)
dfs_predictions["Decision Tree (Base)"] = y_pred

"""evaluation"""

dfs_results["Decision Tree (Base)"] = {
    "R2": r2_score(y_test, y_pred),
    "MSE": mean_squared_error(y_test, y_pred),
    "MAE": mean_absolute_error(y_test, y_pred),
}
print(dfs_results["Decision Tree (Base)"])

plt.scatter(y_test, y_pred, alpha=0.3)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted - Decision Tree (Base)")
plt.show()

plt.figure(figsize=(18, 8))
plot_tree(model_dt_base, feature_names=X_train.columns, filled=True, max_depth=3)
plt.title("Decision Tree (Base)")
plt.show()

"""feature importance (base)"""

importance_base = pd.Series(model_dt_base.feature_importances_, index=X_train.columns).sort_values()
importance_base.plot(kind="barh")
plt.title("Feature Importance - Decision Tree (Base)")
plt.show()

"""model 2: decision tree after tuning"""

from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(
    DecisionTreeRegressor(random_state=42),
    {"max_depth": [5, 10, 15, 20], "min_samples_leaf": [1, 10, 50]},
    cv=3, scoring="r2",
)
grid.fit(X_train, y_train)
print(grid.best_params_)
best_model = grid.best_estimator_

"""prediction"""

y_pred = best_model.predict(X_test)
dfs_predictions["Decision Tree (Tuned)"] = y_pred

"""evaluation"""

dfs_results["Decision Tree (Tuned)"] = {
    "R2": r2_score(y_test, y_pred),
    "MSE": mean_squared_error(y_test, y_pred),
    "MAE": mean_absolute_error(y_test, y_pred),
}
print(dfs_results["Decision Tree (Tuned)"])

plt.scatter(y_test, y_pred, alpha=0.3)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted - Decision Tree (Tuned)")
plt.show()

plt.figure(figsize=(18, 8))
plot_tree(best_model, feature_names=X_train.columns, filled=True, max_depth=3)
plt.title("Decision Tree (Tuned)")
plt.show()

"""feature importance"""

dfs_importance = pd.DataFrame({
    "Base": model_dt_base.feature_importances_,
    "Tuned": best_model.feature_importances_,
}, index=X_train.columns).sort_values("Tuned")
print(dfs_importance.round(3))

dfs_importance.plot(kind="barh")
plt.title("Feature Importance (Base vs Tuned)")
plt.show()

"""comparison"""

dfs_comparison = pd.DataFrame(dfs_results).T.round(3)
print(dfs_comparison)

dfs_comparison["R2"].plot(kind="bar", rot=0)
plt.title("R2 Comparison - Days for shipping (real)")
plt.show()

"""save the data"""

dfs_predictions.to_csv("dfs_predictions.csv", index=False, encoding="utf-8-sig")
dfs_comparison.to_csv("dfs_comparison.csv", index_label="Model", encoding="utf-8-sig")
dfs_importance.to_csv("dfs_importance.csv", index_label="Feature", encoding="utf-8-sig")
