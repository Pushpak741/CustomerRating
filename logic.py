
import psycopg2
import pandas as pd

'''conn = psycopg2.connect(database="",
                        user='', password='', 
                        host='localhost'
)'''

df=pd.read_csv('C:\\Users\\pushp\\Desktop\\csv\\customer_account_info.CSV')
l=list(df.head())
print(l)
#conn.autocommit = True
#cursor = conn.cursor()



#rating_l=[],risk type=[]
#def rating(rating_l):

    

#conn.commit()
#conn.close()