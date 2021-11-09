import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

start = pd.Timestamp('20180101', tz='Europe/Rome')
end = pd.Timestamp('20200101', tz='Europe/Rome')
index = pd.date_range(start,end,freq='M')[:-1]

source = pd.DataFrame(np.cumsum(np.random.randn(len(index), 3), 0).round(2),
                    columns=['A', 'B', 'C'], index=index)
source.index.names = ['x']
source = source.reset_index().melt('x', var_name='category', value_name='y')

### line chart with facet
line = alt.Chart(source).mark_line(point=True).encode(alt.X('month(x):O', title=''), alt.Y('y:Q', title=''), color='category:N')


nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        encodings=['x'], empty='none')
selectors = alt.Chart(source).mark_point().encode(
    x='month(x):O',
    opacity=alt.value(0),
).add_selection(
    nearest
)
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)
text = line.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, 'y:Q', alt.value(' '))
)
rules = alt.Chart(source).mark_rule(color='gray').encode(
    x='month(x):O',
).transform_filter(
    nearest
)
altair_chart= alt.layer(
    line, selectors, points, rules, text
).facet(row=alt.Row('year(x):O', title=''))
st.altair_chart(altair_chart, use_container_width=True)
