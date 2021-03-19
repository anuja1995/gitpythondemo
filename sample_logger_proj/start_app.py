from loggers.sample_logger_proj.productservice import ProductServiceImpl
from loggers.sample_logger_proj.productservice import Product

# why do we need loggers.

if __name__ == '__main__':
    service = ProductServiceImpl()
    # service.create_product_table()
    prod_obj = Product(pid=101,pnm='aaa',pprc=25552.25,pqty=30,pven='Flip')
    service.add_product(prod_obj)