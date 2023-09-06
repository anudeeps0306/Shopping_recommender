from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df['name_encoded'] = label_encoder.fit_transform(df['name'])
df['main_category_encoded'] = label_encoder.fit_transform(df['main_category'])
df['sub_category_encoded'] = label_encoder.fit_transform(df['sub_category'])
