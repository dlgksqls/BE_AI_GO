import pandas as pd
from places.models import Place, Tag

# Read csv file.
df = pd.read_csv(r"C:\Users\user\Desktop\BE_AI_GO\api\config\202309.csv", encoding='cp949')

hardness = df["hardness"]
latitude = df["latitude"]

# Connect to (create) database.
for index, row in df.iterrows():
    tag, created = Tag.objects.get_or_create(name = row['tag'])
    place = Place.objects.create(
        name=row['name'],
        image=row['image'],
        classification=row['classification'],
        street_name_address=row['street_name_address'],
        hardness=row['hardness'],
        latitude=row['latitude'],
        info=row['info'],
        like=row['like'],
        tag=tag
    )
    place.save()