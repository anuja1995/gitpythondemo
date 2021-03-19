CREATE_TABLE = '''
        create table product_info (
            prod_id int,
            prod_name varchar(30),
            prod_qty int,
            prod_price float,
            prod_ven varchar(30),
            primary key(prod_id)
        )
'''

INSERT_PRODUCT="INSERT INTO PRODUCT_INFO VALUES({},'{}',{},{},'{}')"

DELETE_PRODUCT='DELETE FROM PRODUCT_INFO WHERE PROD_ID={}'

UPDATE_PRODUCT="UPDATE PRODUCT_INFO SET PROD_NAME='{}',PROD_QTY={},PROD_PRICE={},PROD_VEN='{}' WHERE PROD_ID={}"

FETCH_PRODUCT='SELECT * FROM PRODUCT_INFO WHERE PROD_ID ={}'

FETCH_ALL_PRODUCTS='SELECT * FROM PRODUCT_INFO'