import streamlit as st
import altair as alt
import geopandas as gpd
import json

st.header('Load from remote URL using alt.topo_feature')
code = '''
st.header('Load from remote URL using alt.topo_feature')
regions = alt.topo_feature("https://raw.githubusercontent.com/deldersveld/topojson/master/countries/italy/italy-regions.json", 'ITA_adm1')
map = alt.Chart(regions).mark_geoshape(
    stroke='white',
    strokeWidth=2
).encode(
    color=alt.value('#eee'),
)
st.altair_chart(map, use_container_width=False)
'''
st.code(code, language='python')
regions = alt.topo_feature("https://raw.githubusercontent.com/deldersveld/topojson/master/countries/italy/italy-regions.json", 'ITA_adm1')
map = alt.Chart(regions).mark_geoshape(
    stroke='white',
    strokeWidth=2
).encode(
    color=alt.value('#eee'),
)
st.altair_chart(map, use_container_width=False)

st.header('Load from local file using alt.InlineData')
with open("italy-regions.json", 'r', encoding = 'utf-8') as f:
    data = json.load(f)
regions_local = alt.InlineData(values=data, format=alt.DataFormat(feature='ITA_adm1',type='topojson')) 
map = alt.Chart(regions_local).mark_geoshape(
    stroke='white',
    strokeWidth=2
).encode(
    color=alt.value('#eee'),
)
st.altair_chart(map, use_container_width=False)

st.header('Load from local file using geopandas')
regions_local = gpd.read_file("italy-regions.json")
map = alt.Chart(regions_local).mark_geoshape(
    stroke='white',
    strokeWidth=2
).encode(
    color=alt.value('#eee'),
)
st.altair_chart(map, use_container_width=False)

st.header('Load from local file using geopandas + alt.InlineData')
regions_local = gpd.read_file("italy-regions.json")
data = alt.InlineData(values = regions_local.to_json(), format = alt.DataFormat(property='features', type='json'))
map = alt.Chart(data).mark_geoshape(
    stroke='white',
    strokeWidth=2
).encode(
    color=alt.value('#eee'),
)
st.altair_chart(map, use_container_width=False)
