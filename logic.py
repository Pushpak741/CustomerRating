
import psycopg2


con=psycopg2.connect(
    host="localhost",
    database="CustomerRating",
    user="postgres",
    password="1234"
)
cur=con.cursor()



cur.execute("COPY rating_customer_info FROM 'C:\\Users\\pushp\\Desktop\\csv\\customer_info.csv' DELIMITER ',' CSV HEADER;")

con.commit()
con.close()
#df=pd.read_csv('C:\\Users\\pushp\\Desktop\\csv\\customer_account_info.CSV')
#l=list(df.head())
#print(l)
#conn.autocommit = True
#cursor = conn.cursor()



#rating_l=[],risk type=[]
#def rating(rating_l):

    

#conn.commit()
#conn.close()