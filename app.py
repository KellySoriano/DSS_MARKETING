import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Marketing", layout="wide")

df = pd.read_csv("marketing_campaign(1).csv", sep="\t")

# Limpiar estados civiles irrelevantes
df = df[~df["Marital_Status"].isin(["YOLO", "Absurd", "Alone"])]

st.title("📊 DSS para Segmentación de Clientes en Marketing Digital")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    fig = px.scatter(
        df,
        x="Income",
        y="NumWebPurchases",
        title="Compras Web según Ingresos"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    canales = {
        "Web": df["NumWebPurchases"].sum(),
        "Store": df["NumStorePurchases"].sum(),
        "Catalog": df["NumCatalogPurchases"].sum()
    }

    canales_df = pd.DataFrame({
        "Canal": list(canales.keys()),
        "Compras": list(canales.values())
    })

    fig2 = px.bar(
        canales_df,
        x="Canal",
        y="Compras",
        title="Preferencia de Canal de Compra",
        color="Canal"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

education = df["Education"].value_counts().reset_index()
education.columns = ["Educación", "Cantidad"]

fig3 = px.bar(
    education,
    x="Educación",
    y="Cantidad",
    title="Clientes por Nivel Educativo",
    color="Educación"
)

st.plotly_chart(fig3, use_container_width=True)

marital = df["Marital_Status"].value_counts().reset_index()
marital.columns = ["Estado Civil", "Cantidad"]

fig4 = px.pie(
    marital,
    values="Cantidad",
    names="Estado Civil",
    hole=0.5,
    title="Segmentación por Estado Civil"
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

productos = {
    "Vinos": df["MntWines"].sum(),
    "Carnes": df["MntMeatProducts"].sum(),
    "Pescados": df["MntFishProducts"].sum(),
    "Oro": df["MntGoldProds"].sum(),
    "Dulces": df["MntSweetProducts"].sum()
}

productos_df = pd.DataFrame({
    "Producto": list(productos.keys()),
    "Total": list(productos.values())
})

fig5 = px.bar(
    productos_df,
    x="Producto",
    y="Total",
    title="Análisis de Preferencia de Productos",
    color="Producto"
)

st.plotly_chart(fig5, use_container_width=True)
