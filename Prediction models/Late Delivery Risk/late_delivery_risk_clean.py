"""Late_Delivery_Risk (Classification)"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DataCoSupplyChain_Cleaned.csv", encoding="latin-1")
data = df.drop(columns=["Late_delivery_risk"])
y_ldr = df["Late_delivery_risk"]

"""dropping columns"""

ids = ["Category Id", "Customer Id", "Department Id", "Order Id", "Order Item Id", "Product Card Id"]
too_many_values = ["Customer City", "Order City", "Order State", "Order Country", "Product Name"]
leakage = ["Delivery Status", "Days for shipping (real)", "shipping date (DateOrders)",
           "Order Status", "Order Item Profit Ratio", "Order Item Total"]
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
    data, y_ldr, test_size=0.2, random_state=42, stratify=y_ldr
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
from sklearn.linear_model import LogisticRegression

selector = SequentialFeatureSelector(LogisticRegression(max_iter=1000), n_features_to_select=10, direction="forward", cv=3)
selector.fit(X_train_full, y_train)
selected_cols = list(X_train_full.columns[selector.get_support()])
print(selected_cols)

X_train = X_train_full[selected_cols]
X_test = X_test_full[selected_cols]

"""model 1: logistic regression"""

model_lr = LogisticRegression(max_iter=1000)
model_lr.fit(X_train, y_train)

"""prediction"""

ldr_results = {}
ldr_predictions = pd.DataFrame({"Order Item Id": df.loc[y_test.index, "Order Item Id"], "Actual": y_test})
y_pred = model_lr.predict(X_test)
ldr_predictions["Logistic Regression"] = y_pred

"""evaluation"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, ConfusionMatrixDisplay

ldr_results["Logistic Regression"] = {
    "Accuracy": accuracy_score(y_test, y_pred),
    "Precision": precision_score(y_test, y_pred),
    "Recall": recall_score(y_test, y_pred),
    "F1": f1_score(y_test, y_pred),
}
print(classification_report(y_test, y_pred))

ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Confusion Matrix - Logistic Regression")
plt.show()

"""model 2: decision tree before tuning"""

from sklearn.tree import DecisionTreeClassifier, plot_tree

model_dt_base = DecisionTreeClassifier(random_state=42)
model_dt_base.fit(X_train, y_train)

"""prediction"""

y_pred = model_dt_base.predict(X_test)
ldr_predictions["Decision Tree (Base)"] = y_pred

"""evaluation"""

ldr_results["Decision Tree (Base)"] = {
    "Accuracy": accuracy_score(y_test, y_pred),
    "Precision": precision_score(y_test, y_pred),
    "Recall": recall_score(y_test, y_pred),
    "F1": f1_score(y_test, y_pred),
}
print(classification_report(y_test, y_pred))

ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Confusion Matrix - Decision Tree (Base)")
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
    DecisionTreeClassifier(random_state=42),
    {"max_depth": [5, 10, 15, 20], "min_samples_leaf": [1, 10, 50]},
    cv=3, scoring="f1",
)
grid.fit(X_train, y_train)
print(grid.best_params_)
best_model = grid.best_estimator_

"""prediction"""

y_pred = best_model.predict(X_test)
ldr_predictions["Decision Tree (Tuned)"] = y_pred

"""evaluation"""

ldr_results["Decision Tree (Tuned)"] = {
    "Accuracy": accuracy_score(y_test, y_pred),
    "Precision": precision_score(y_test, y_pred),
    "Recall": recall_score(y_test, y_pred),
    "F1": f1_score(y_test, y_pred),
}
print(classification_report(y_test, y_pred))

ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Confusion Matrix - Decision Tree (Tuned)")
plt.show()

plt.figure(figsize=(18, 8))
plot_tree(best_model, feature_names=X_train.columns, filled=True, max_depth=3)
plt.title("Decision Tree (Tuned)")
plt.show()

"""feature importance"""

ldr_importance = pd.DataFrame({
    "Base": model_dt_base.feature_importances_,
    "Tuned": best_model.feature_importances_,
}, index=X_train.columns).sort_values("Tuned")
print(ldr_importance.round(3))

ldr_importance.plot(kind="barh")
plt.title("Feature Importance (Base vs Tuned)")
plt.show()

"""comparison"""

ldr_comparison = pd.DataFrame(ldr_results).T.round(3)
print(ldr_comparison)

ldr_comparison.plot(kind="bar", rot=0)
plt.title("Model Comparison - Late Delivery Risk")
plt.show()

"""save the data"""

ldr_predictions.to_csv("ldr_predictions.csv", index=False, encoding="utf-8-sig")
ldr_comparison.to_csv("ldr_comparison.csv", index_label="Model", encoding="utf-8-sig")
ldr_importance.to_csv("ldr_importance.csv", index_label="Feature", encoding="utf-8-sig")
