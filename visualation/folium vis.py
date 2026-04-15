# full_folium_example.py
# مثال كامل يوضح Map, TileLayer (بـ attr), FeatureGroup, add_child/add_to,
# MarkerCluster, HeatMap, Choropleth (مع DataFrame) و LayerControl.
# شغله بعد تثبيت folium و pandas: pip install folium pandas

import folium                                # استيراد مكتبة Folium لبناء الخرائط
from folium.plugins import MarkerCluster, HeatMap, MiniMap, Fullscreen  # بعض الإضافات (plugins)
import pandas as pd                          # pandas للتعامل مع الجداول (DataFrame)
import json                                  # لتحميل أو معالجة GeoJSON لو احتجنا

# -----------------------
# 1) إعداد خريطة أساسية + إضافات TileLayers مع Attribution
# -----------------------
m = folium.Map(
    location=[30.033333, 31.233334],   # مركز الخريطة: القاهرة (latitude, longitude)
    zoom_start=11,                     # مستوى التكبير الابتدائي
    tiles=None                         # نمرر None لأننا سنضيف TileLayers يدويًا
)

# إضافة TileLayer افتراضي (OpenStreetMap) — لا يحتاج attr مضاف لأنه معروف داخل folium
folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)

# إضافة Stamen Terrain مع Attribution صريح لمنع خطأ "Custom tiles must have an attribution."
folium.TileLayer(
    tiles='https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.',
    name='Stamen Terrain'
).add_to(m)

# إضافة Stamen Toner (مثال آخر)
folium.TileLayer(
    tiles='https://stamen-tiles.a.ssl.fastly.net/toner/{z}/{x}/{y}.png',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.',
    name='Stamen Toner'
).add_to(m)

# إضافة CartoDB Positron (نمط فاتح جيد لعرض بيانات فوقه)
folium.TileLayer('CartoDB positron', name='CartoDB Positron').add_to(m)

# -----------------------
# 2) FeatureGroups و add_child() + استخدام add_to()
# -----------------------
# مجموعة للمساجد
mosques_fg = folium.FeatureGroup(name='Mosques')

# نضيف بعض العلامات (Markers) داخل مجموعة المساجد باستخدام add_child
mosques_fg.add_child(
    folium.Marker(location=[30.0486, 31.2625], popup='Al-Azhar Mosque', icon=folium.Icon(color='green'))
)
mosques_fg.add_child(
    folium.Marker(location=[30.0460, 31.2619], popup='Amr Ibn Al-As Mosque', icon=folium.Icon(color='darkgreen'))
)

# مجموعة للحدائق
parks_fg = folium.FeatureGroup(name='Parks')
parks_fg.add_child(
    folium.Marker(location=[30.0353, 31.2199], popup='Al-Azhar Park', icon=folium.Icon(color='lightgreen'))
)
parks_fg.add_child(
    folium.Marker(location=[30.0200, 31.2120], popup='Orman Garden', icon=folium.Icon(color='green'))
)

# نضيف FeatureGroups للخريطة (parent)
m.add_child(mosques_fg)
m.add_child(parks_fg)

# -----------------------
# 3) MarkerCluster — مفيد لو عندك عدد كبير من النقاط
# -----------------------
cluster_fg = folium.FeatureGroup(name='Clustered Points')
marker_cluster = MarkerCluster(name='Marker Cluster').add_to(cluster_fg)

# مثال على نقاط متعددة (قد تكون من DataFrame في الواقع)
points = [
    [30.0444, 31.2357],
    [30.0455, 31.2350],
    [30.0430, 31.2380],
    [30.0410, 31.2300],
    [30.0500, 31.2200]
]
for i, pt in enumerate(points):
    # نستخدم add_to للراحة — نفس الفكرة كـ add_child لكن الترتيب عكسي
    folium.Marker(location=pt, popup=f'Point #{i+1}').add_to(marker_cluster)

# نضيف المجموعة العنقودية (cluster_fg) للخريطة
m.add_child(cluster_fg)

# -----------------------
# 4) HeatMap — خريطة حرارية لتمثيل الكثافة
# -----------------------
heat_fg = folium.FeatureGroup(name='HeatMap')
# HeatMap يأخذ قائمة إحداثيات مع إمكانية تمرير وزن لكل نقطة
HeatMap(points).add_to(heat_fg)
m.add_child(heat_fg)

# -----------------------
# 5) مثال بسيط على PolyLine و CircleMarker
# -----------------------
# خط يربط ثلاثة نقاط (مثال على طريق/مسار)
folium.PolyLine(locations=[[30.0486,31.2625],[30.0444,31.2357],[30.0353,31.2199]],
                tooltip='Simple path').add_to(m)

# دائرة (مساحة تقريبية) حول نقطة
folium.Circle(location=[30.0444, 31.2357], radius=800, popup='Area ~800m radius').add_to(m)

# -----------------------
# 6) Choropleth — مثال DataFrame + ملف GeoJSON
# -----------------------
# مثال DataFrame يبسط الفكرة: دول ومجموع قيمة (مثال الهجرة أو أي قيمة عددية)
df_canada = pd.DataFrame({
    'country': ['Egypt', 'Sudan', 'Libya', 'Algeria'],
    'value': [100, 40, 20, 60]
})

# خيار 1: لو عندك ملف GeoJSON (ممسوح محليًا)، افعل السطور دي (غير المسار حسب ملفك)
geojson_path = 'countries.geojson'  # غيّر المسار لو ملفك اسمه مختلف

try:
    # لو الملف موجود: ننشئ Choropleth حقيقي
    with open(geojson_path, 'r', encoding='utf-8') as f:
        countries_geo = json.load(f)

    folium.Choropleth(
        geo_data=countries_geo,
        data=df_canada,
        columns=['country', 'value'],
        key_on='feature.properties.NAME',  # غيّر حسب بنية ملف الـ GeoJSON (قد يكون 'name' أو 'ADMIN' ...)
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Example Value by Country',
        name='Choropleth'
    ).add_to(m)

except FileNotFoundError:
    # خيار 2: لو ما عندكش ملف GeoJSON، نعرض مثال GeoJSON صغير مضمّن للتوضيح (لن يغطي دول حقيقية متعددة)
    sample_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "SmallRegionA"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[31.20,30.04],[31.26,30.04],[31.26,30.00],[31.20,30.00],[31.20,30.04]]]
                }
            }
        ]
    }
    # نضيف الـ GeoJson كمكوّن تفاعلي مع popup/tooltip
    folium.GeoJson(
        sample_geojson,
        name='Sample GeoJSON',
        tooltip=folium.GeoJsonTooltip(fields=['name'], aliases=['Region:'])
    ).add_to(m)

# -----------------------
# 7) إضافات واجهة مستخدم صغيرة: MiniMap + Fullscreen ثم LayerControl
# -----------------------
MiniMap().add_to(m)               # خريطة صغيرة زاوية الشاشة
Fullscreen(position='topright').add_to(m)  # زر ملء الشاشة
folium.LayerControl(collapsed=False).add_to(m)  # أداة التحكم في الطبقات (تجعل كل FeatureGroup و TileLayer قابلة للإظهار/الإخفاء)

# -----------------------
# 8) حفظ الملف النهائي
# -----------------------
m.save('full_cairo_map_example.html')
print('✅ تم إنشاء full_cairo_map_example.html — افتحه في المتصفح لمشاهدة الخريطة التفاعلية.')
