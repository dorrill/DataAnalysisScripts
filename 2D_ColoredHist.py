#Seaborn applies color palettes to the underlying matplotlib options, but doesn't always use it for plotting. 
#when using histplot for a 2D scatter plot, I was always stuck with the rocket color palette, which is a boring blue. One can fix this with the cmap option.
#This script imports some data, loads it into a dataframe, and plots it with a nice color scheme
#Note the comment out color palette setting does not work by itself

import pandas as pd
url = 'data/ames-housing-dataset.zip'
housing = pd.read_csv(url, engine='pyarrow', dtype_backend='pyarrow')
import seaborn as sns
#sns.color_palette("viridis", as_cmap=True)
colors = ['#747FE3', '#8EE35D', '#E37346']
sns.histplot(
    housing, x="1st Flr SF", y="SalePrice",
    bins=30, discrete=(False, False), log_scale=(False, False),cbar=True,
    hue_norm=True, cmap="viridis"
)
