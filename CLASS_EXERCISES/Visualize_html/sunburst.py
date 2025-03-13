import pandas as pd
import plotly.express as px

file_path = "dataset-416.xlsx"
xls = pd.ExcelFile(file_path)

df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])

df_filtered = df.dropna(subset=['Tên học phần', 'Học Kỳ', 'Loại môn học'])

df_filtered = df_filtered.copy()
df_filtered['Học Kỳ'] = df_filtered['Học Kỳ'].astype(int).astype(str)

fig = px.sunburst(
    df_filtered,
    path=['Học Kỳ',pi 'Loại môn học', 'Tên học phần'],
    values=[1] * len(df_filtered),
    title="Biểu đồ Nested Pie Chart của các môn học theo kỳ",
    color='Loại môn học',
)

output_html = "sunburst_chart.html"
fig.write_html(output_html)