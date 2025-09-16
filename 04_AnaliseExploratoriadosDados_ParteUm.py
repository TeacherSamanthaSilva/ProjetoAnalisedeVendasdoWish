#Análise Exploratória dos dados - Parte umimport pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_products = pd.read_csv("summer-products-with-rating-and-performance_2020-08.csv")

[i for i in df_products.columns]

cols = ['title',
 'price',
 'retail_price',
 'currency_buyer',
 'units_sold',
 'uses_ad_boosts',
 'rating',
 'rating_count',
 'badges_count',
 'badge_product_quality',
 'badge_fast_shipping',
 'tags',
 'product_color',
 'product_variation_size_id',
 'product_variation_inventory',
 'shipping_is_express',
 'countries_shipped_to',
 'inventory_total',
 'has_urgency_banner',
 'origin_country',
 'merchant_rating_count',
 'merchant_rating',]

 #Analise da qualidade dos dados

df_products = df_products[cols]

df_products.info()

df_products.isna().sum()

df_products.loc[df_products["product_color"].isna(), "product_color"] = ""
df_products.loc[df_products["product_variation_size_id"].isna(), "product_variation_size_id"] = ""
df_products.loc[df_products["has_urgency_banner"].isna(), "has_urgency_banner"] = 0
df_products.loc[df_products["origin_country"].isna(), "origin_country"] = ""

#Analise dos dados ausentes

df_products.isna().sum()

df_products.describe()

categorical_cols = [i for i in cols if i not in df_products.describe().columns]
numerical_cols = df_products.describe().columns
categorical_cols

numerical_cols

categorical_cols

df_products["tags"]  # Esta precisará de um tratamento


for col in categorical_cols:
    if col not in ["title", "tags"]:
        f, axes = plt.subplots(1,1,figsize=(18,5))
        sns.countplot(x=col, data = df_products)
        plt.xticks(rotation=90)
        plt.suptitle(col,fontsize=20)
        plt.show()

numerical_cols

for col in numerical_cols:
    f, axes = plt.subplots(1,1,figsize=(18,4))
    sns.histplot(x=col, data=df_products)
    plt.xticks(rotation=90)
    plt.suptitle(col,fontsize=20)
    plt.show()

df_products["units_sold"].value_counts()

df_products

df_products.loc[df_products["units_sold"] < 10, "units_sold"] = 10
df_products["units_sold"].value_counts()

df_products["units_sold"].median() 