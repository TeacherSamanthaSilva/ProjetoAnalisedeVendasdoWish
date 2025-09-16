from sklearn.model_selection import train_test_split

model_cols = ['price', 'retail_price', 
       'uses_ad_boosts', 'rating', 'badges_count',
       'badge_product_quality', 'badge_fast_shipping', 'product_variation_inventory',
       'shipping_is_express', 'countries_shipped_to', 'inventory_total',
       'has_urgency_banner', 
       'merchant_rating', 'discount', 'tags_count']

x = df_products[model_cols]
y = df_products["success"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

from sklearn.metrics import classification_report, confusion_matrix

y_pred = rf_model.predict(x_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

feature_importances = pd.DataFrame(rf_model.feature_importances_,
                                   index = x.columns,
                                    columns=['importance']).sort_values('importance', ascending=True)

fig, ax = plt.subplots(figsize=(20, 8))
feature_importances.plot(kind="barh", ax=ax)

import shap

explainer = shap.TreeExplainer(rf_model)
shap_values = explainer.shap_values(x)
shap.summary_plot(shap_values[1], x)

df_products["discount"] = df_products["retail_price"] - df_products["price"]

fig, ax = plt.subplots(figsize=(20, 6))
sns.distplot(df_products.loc[df_products["success"] == 1, "discount"], label="1")
sns.distplot(df_products.loc[df_products["success"] == 0, "discount"], label="0")
plt.legend()
