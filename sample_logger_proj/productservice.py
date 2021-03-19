from loggers.sample_logger_proj.app_queries import *
from loggers.sample_logger_proj.product_info import Product
from loggers.sample_logger_proj.db_util import get_connection, close_resources
import logging

logging.basicConfig(filename='productservices.log',level=logging.INFO,
                    format='%(funcName)s- %(lineno)d - %(asctime)s %(created)f -%(module)s- %(name)s - %(levelname)s - %(message)s')  #default level->warnig
# format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# def m1():
#     logging.info('this is info msg-20')
#     logging.debug('this is debug msg-10')
#     logging.warning('this is warning msg-30')
#     logging.error('this is error msg-40')
#     logging.critical('this is critical msg-50')
#
# if __name__ == '__main__':
#     m1()
#
# import sys
# sys.exit(0)

class ProductServiceImpl:

    def add_product(self,prod):
        logging.info('inside add product method')
        if type(prod) == Product:
            dbprod = self.get_product(prod.prodId)
            if dbprod:
                logging.warning('product with given id is already present')
                return 'Duplicate product..!'
            try:
                sql = INSERT_PRODUCT.format(prod.prodId,prod.prodName,prod.prodQty,prod.prodPrice,prod.prodVen)
                logging.info(sql)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                return 'product added successfully..'
            except BaseException as e:
                logging.error(e.args)
                return 'problem in Product Insert..!'
            finally:
                close_resources(conn, cursor)
        return 'Invalid product type'


    def delete_product(self,pid):
        if type(pid)==int and pid>0:
            dbprod = self.get_product(pid)
            if dbprod:
                try:
                    sql = DELETE_PRODUCT.format(pid)
                    logging.info(sql)
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.execute(sql)
                    conn.commit()
                    return 'product Deleted successfully..'
                except BaseException as e:
                    logging.error(e.args)
                    return 'problem in Product delete..!'
                finally:
                    close_resources(conn, cursor)
            else:
                return "product with given id is not exist..!"
        return 'Invalid product type'

    def get_product(self,pid):
        logging.info('inside get product')
        if type(pid) ==int and pid>0:
            try:
                sql = FETCH_PRODUCT.format(pid)
                logging.info(sql)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(sql)
                record = cursor.fetchone()
                if record:
                    return Product(pid=record[0],pnm=record[1],pqty=record[2],pven=record[3],pprc=record[4])
                # return 'NOo product with given id.'
            except BaseException as e:
                logging.error(e.args)
                # return 'problem in Product Insert..!'
            finally:
                close_resources(conn, cursor)
        # return 'Invalid product type'

    def get_all_products(self):
            try:
                sql = FETCH_ALL_PRODUCTS
                logging.info(sql)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(sql)
                records = cursor.fetchall()
                products = []
                for record in records:
                    products.append(Product(pid=record[0], pnm=record[1], pqty=record[2], pven=record[3], pprc=record[4]))
                return products
                # return 'product added successfully..'
            except BaseException as e:
                logging.error(e.args)
                # return 'problem in Product Insert..!'
            finally:
                close_resources(conn, cursor)

    def update_product(self,pid,newvalues):
        if self.get_product(pid) and type(newvalues)==Product:
            try:
                sql = UPDATE_PRODUCT.format(newvalues.prodName, newvalues.prodQty, newvalues.prodPrice, newvalues.prodVen, newvalues.prodId)
                logging.info(sql)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                return 'product Updated successfully..'
            except BaseException as e:
                logging.error(e.args)
                return 'problem in Product Updated..!'
            finally:
                close_resources(conn, cursor)
        return 'Invalid product type or no product with the given id exist..!'

    def create_product_table(self):
        try:
            sql = CREATE_TABLE
            logging.info(sql)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            return "Product Created Successfully..!"
        except BaseException as e:
            logging.error(e.args)
            return "Problem in Product create...!"
        finally:
            close_resources(conn, cursor)