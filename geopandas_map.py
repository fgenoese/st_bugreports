import streamlit as st
import altair as alt
import geopandas as gpd

regions = alt.topo_feature("https://raw.githubusercontent.com/deldersveld/topojson/master/countries/italy/italy-regions.json", 'ITA_adm1')

map = alt.Chart(regions).mark_geoshape(
    stroke='white',
    strokeWidth=2
).encode(
    color=alt.value('#eee'),
)
st.altair_chart(map, use_container_width=False)

regions_local = gpd.read_file("italy-regions.json")
map2 = alt.Chart(regions_local).mark_geoshape(
    stroke='white',
    strokeWidth=2
).encode(
    color=alt.value('#eee'),
)
st.altair_chart(map2, use_container_width=False)
