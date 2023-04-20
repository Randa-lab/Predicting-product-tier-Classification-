#Encoding categorical features. 
#I chose label encoding because the number of categories in make_name is quite large and categories in product tier might be ordinal

from sklearn.preprocessing import LabelEncoder

# Creating a instance of label Encoder.
label_encoder = LabelEncoder()

# Encode labels in columns 'product_tier' and 'make_name'. 
df['product_tier']= label_encoder.fit_transform(df['product_tier']) 
df['make_name']= label_encoder.fit_transform(df['make_name'])
