import pandas as pd

scrapped_data = pd.DataFrame(columns=['Code', 'Website', 'Address', 'Phone', 'City', 'State', 'Zip', 'Country', 'Director1', 'Director2', 'Director3', 'Director4', 'Director5', 'Director6', 'Director7', 'Director8', 'Director9', 'Director10', 'Director11', 'Director12', 'Director13', 'Director14', 'Director15', 'Director16', 'Director17', 'Director18', 'Director19', 'Director20',])

scrapped_data.to_csv("scrapped_data.csv")