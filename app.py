import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="DSS Marketing",
    page_icon="📊",
    layout="wide"
)

# ESTILO PERSONALIZADO
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

h1 {
    color: #1f3c88;
}

h2, h3 {
    color: #1f3c88;
}
</style>
""", unsafe_allow_html=True)

# CARGAR CSV
df = pd.read_csv("marketing_campaign(1).csv")

# LIMPIAR DATOS
df = df[~df["Marital_Status"].isin(["YOLO", "Absurd", "Alone"])]

# TÍTULO
st.markdown("""
<h1 style='text-align: center;'>
📊 DSS para Segmentación de Clientes en Marketing Digital
</h1>

<p style='text-align: center; font-size:18px;'>
Análisis interactivo de comportamiento y preferencias de clientes
</p>
""", unsafe_allow_html=True)

st.divider()

# MÉTRICAS
col1, col2, col3 = st.columns(3)

col1.metric("Clientes", len(df))
col2.metric("Ingreso promedio", f"${int(df['Income'].mean()):,}")
col3.metric("Compras Web", int(df['NumWebPurchases'].sum()))

st.divider()

# FILTRO
educacion = st.selectbox(
    "Selecciona nivel educativo",
    df["Education"].unique()
)

df_filtrado = df[df["Education"] == educacion]

# GRÁFICAS
col1, col2 = st.columns(2)

# SCATTER
with col1:
    fig1 = px.scatter(
        df_filtrado,
        x="Income",
        y="NumWebPurchases",
        title="Compras Web según Ingresos",
        template="plotly_white"
    )

    st.plotly_chart(fig1, use_container_width=True)

# BARRAS CANAL
with col2:
    canales = {
        "Web": df_filtrado["NumWebPurchases"].sum(),
        "Store": df_filtrado["NumStorePurchases"].sum(),
        "Catalog": df_filtrado["NumCatalogPurchases"].sum()
    }

    canales_df = pd.DataFrame({
        "Canal": list(canales.keys()),
        "Compras": list(canales.values())
    })

    fig2 = px.bar(
        canales_df,
        x="Canal",
        y="Compras",
        color="Canal",
        title="Preferencia de Canal de Compra",
        template="plotly_white"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# EDUCACIÓN
educacion_counts = df["Education"].value_counts().reset_index()
educacion_counts.columns = ["Educación", "Cantidad"]

fig3 = px.bar(
    educacion_counts,
    x="Educación",
    y="Cantidad",
    color="Educación",
    title="Clientes por Nivel Educativo",
    template="plotly_white"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ESTADO CIVIL
estado_counts = df["Marital_Status"].value_counts().reset_index()
estado_counts.columns = ["Estado Civil", "Cantidad"]

fig4 = px.pie(
    estado_counts,
    values="Cantidad",
    names="Estado Civil",
    hole=0.5,
    title="Segmentación por Estado Civil",
    template="plotly_white"
)

st.plotly_chart(fig4, use_container_width=True)

st.divider()

# PRODUCTOS
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
    color="Producto",
    title="Análisis de Preferencia de Productos",
    template="plotly_white"
)

st.plotly_chart(fig5, use_container_width=True)

st.divider()

# CONCLUSIONES
st.markdown("""
## Conclusiones

- Los vinos representan el producto con mayor nivel de compra dentro de los clientes analizados.

- Las carnes constituyen el segundo producto con mayor preferencia de consumo.

- Dulces y pescados presentan menores niveles de compra en comparación con los demás productos.

- Los resultados obtenidos permiten identificar patrones de consumo útiles para estrategias de segmentación y campañas de marketing personalizadas.
""")

st.divider()

# EQUIPO
st.markdown("""
### Elaborado por

- Kelly Soriano  
- Valeria Peniche  
- Dariana Echeverria
""")
