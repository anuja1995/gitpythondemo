import logging
from loggers.sample_logger_proj.db_util import get_connection,close_resources


'''
CREATE TABLE APP_LOG(
    log_id int,
    level_name varchar(30),
    message varchar(250),
    line_no int,
    created_at varchar(30),
    func_name varchar(30),
    primary key(log_id)
);

INSERT INTO APP_LOG VALUES(101,'INFO','this is info msg',33,'2021-03-17 23:10:12,929','m1');
INSERT INTO APP_LOG VALUES({},'{}','{}',{},'{}','{}');

'''

def myapp_gen():
    cnt = 100
    while True:
        cnt = cnt +1
        yield cnt
gen = myapp_gen()

class MyDBHandler(logging.Handler):

    def emit(self, record):    # handlers internally calls to emit method--> so we have to write our logic into emit method(override emit method)
        levelname = record.levelname
        message = record.message
        lineno = record.lineno
        create_tm = record.created
        func_name = record.funcName
        # asctime = record.asctime
        # name = record.name
        try:
            sql = "insert into app_log values({},'{}','{}',{},'{}','{}')".\
                format(next(gen),levelname,message,lineno,str(create_tm),func_name)
            print(sql)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except BaseException as e:
            logging.error(e.args)
            return 'problem in log Insert into database..!'
        finally:
            close_resources(conn, cursor)