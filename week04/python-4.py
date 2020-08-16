# -*- coding:utf-8 -*-
#from sklearn import datasets
import os
import pandas as pd
import numpy as np
    

def test():
    group = ['x', 'y', 'z']
    data = pd.DataFrame({
        "group": [group[x] for x in np.random.randint(0, len(group), 15)],
        "salary": np.random.randint(5, 50, 15),
        "age": np.random.randint(15, 50, 15),
        "id": [995 + i for i in range(15)],
        # "order_id": np.random.randint(2005, 2010, 15),
    })
    table1 = data
    table2 = None
    
    # select * from data
    print (data.values)

    # select * from data limit 10
    print (data[0:10])
    
    # select id from data
    print (data["id"])

    # select count(id) from data
    print (data["id"].count())
    
    # select * from data where id < 1000 and age > 30
    print (data[(data["id"] < 1000) & ((data["age"] > 30))])

    # =====================
    print ("\n=====================")
    table1 = pd.DataFrame({
        "id": np.random.randint(995, 1005, 15),
        "order_id": np.random.randint(2005, 2010, 15),
    })
    print (table1)
    
    # 6. select id,count(DISTINCT order_id) from table1 groupby id
    tb = table1.drop_duplicates(['order_id'])
    print (tb)
    
    grp = tb.groupby('id')
    ret = grp.aggregate({'order_id': 'count'})
    print (ret)

    print ("\n7. =====================")
    # 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
    print(pd.merge(table1, data, on="id", how="inner"))

    # 8. SELECT * FROM table1 UNION SELECT * FROM table2;
    pd.concat([table1, table2])

    # 9. DELETE FROM table1 WHERE id=10;
    res = table1[table1["id"] != 10]
    print(res)
    

    # 10. ALTER TABLE table1 DROP COLUMN column_name;
    del table1['id']
    print (table1)
    
    
    
if __name__ == "__main__":
    test()
    print ("===  end  ===")
    
