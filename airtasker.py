import yfinance as yf
import pandas as pd


x = pd.read_excel("asx_by_market_cap.xlsx")

names = x['CODE']

scrapped_data = pd.read_csv("scrapped_data.csv", index_col=0)
not_found = pd.read_csv("notfound.csv", index_col=0)


for name in names:
    name = str(name)

    company = yf.Ticker(name+".AX")
    info = company.info

    if len(info) == 1:
        not_found = pd.concat([not_found, pd.DataFrame([{"Code": name}])], ignore_index=True)
        not_found.to_csv("notfound.csv")
        
    else:
        row_data = {}
        try:
            directors = info['companyOfficers']
            for i, director in enumerate(directors, start=1):
                row_data[f"Director{i}"] = director["name"]
            
        except:
            all_directors = None
            
        try:
            website = info['website']
            
        except:
            website = None
            
        try:
            address = info["address1"] + "; " + info["address2"]
            
        except:
            try:
                address = info["address1"]
            except:
                address = None
            
        try:
            phone = info["phone"]
            
        except:
            phone = None
        try:
            city = info["city"]
            
        except:
            city = None
        try:
            state = info["state"]
            
        except:
            state = None
        try:
            zip = info["zip"]
            
        except:
            zip = None
        try:
            country = info["country"]
            
        except:
            country = None
            
        
        
        row_data["Code"] = name
        row_data["Website"] = website
        row_data["Address"] = address
        row_data["Phone"] = phone
        row_data["City"] = city
        row_data["State"] = state
        row_data["Zip"] = zip
        row_data["Country"] = country
        scrapped_data = pd.concat([scrapped_data, pd.DataFrame([row_data])], ignore_index=True)
        
        scrapped_data.to_csv("scrapped_data.csv")
            
        
                
        