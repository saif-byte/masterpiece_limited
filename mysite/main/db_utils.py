from django.db import connection
def hired_trigger():
    cursor = connection.cursor()

    sql = '''
    CREATE OR REPLACE TRIGGER hired_trigger
        BEFORE INSERT ON main_hiredpainting
        FOR EACH ROW
        BEGIN 

    '''

def all_painting_view():
    cursor = connection.cursor()

    cursor.execute('''CREATE OR REPLACE VIEW allpaintings AS SELECT * FROM main_painting ;''')

    


def trigger_on_hiredpainting():
    cursor = connection.cursor()
    
    cursor.execute('''CREATE OR REPLACE TRIGGER hired_trigger AFTER INSERT ON main_hiredpainting
    FOR EACH ROW    
BEGIN
   -- update the painting table   
   UPDATE main_painting 
   SET mth_to_rtn = 6 
   WHERE id  = :NEW.painting_id_id;

   UPDATE main_painting 
   SET hired = 1 
   WHERE id  = :NEW.painting_id_id;

END;
''')    


def make_is_hired_func():
    cursor = connection.cursor()

    cursor.execute('''CREATE OR REPLACE FUNCTION is_hired( in_id IN main_painting.id%type )
  RETURN NUMBER
  IS
  bol_hired main_painting.hired%type ; 
    BEGIN
  SELECT hired 
    INTO bol_hired
    from main_painting where id = in_id;
    
    RETURN bol_hired;
    END;
''')

def rtn_pnt():
    cursor = connection.cursor()

    cursor.execute('''
    CREATE OR REPLACE PROCEDURE rtn_pnt( in_cid IN main_hiredpainting.customer_id_id%type,in_pid IN main_hiredpainting.painting_id_id%type  )
  IS
    BEGIN
  UPDATE main_hiredpainting
  SET RETURNED = 1
  WHERE customer_id_id = in_cid and painting_id_id = in_pid;
    END;

    ''')

def cal_rent():
    cursor = connection.cursor()

    cursor.execute('''
    
CREATE OR REPLACE FUNCTION cal_rent( in_cid IN main_customer.id%type ,in_pid IN main_painting.id%type  )
  RETURN NUMBER
  IS
  calrent main_painting.rent%type ; 
  orgrent main_painting.rent%type ;
  cat main_customer.category%type;
  
    BEGIN
  select rent into orgrent from main_painting where id = in_pid;
  select category into cat from main_customer where id = in_cid;
  if cat = 'B' then calrent := orgrent;
  elsif cat = 'S' then calrent := orgrent*0.95;
  elsif cat = 'G' then calrent := orgrent*0.9;
  else calrent :=orgrent*0.85;
  end if;
RETURN calrent;
    
    END;
    
    ''')


def after_rtn_trigger():
    cursor = connection.cursor()

    cursor.execute('''
CREATE OR REPLACE TRIGGER after_rtn_trig AFTER UPDATE OF returned ON main_hiredpainting
    FOR EACH ROW    
    when (new.returned = 1)
BEGIN
   -- update the painting table   
   UPDATE main_painting 
   SET hired = 0 
   WHERE id  = :NEW.painting_id_id;

END;
    ''')

def get_disc():
  cursor = connection.cursor()
  cursor.execute('''
CREATE OR REPLACE FUNCTION get_disc( in_cid IN main_customer.id%type  )
  RETURN NUMBER
  IS
  disc NUMBER;
  cat main_customer.CATEGORY%type;
    BEGIN
  select category into cat from main_Customer where id = in_cid;
  if cat = 'B' then disc := 0;
  elsif cat = 'S' then disc := 5;
  elsif cat = 'G' then disc := 10;
  else cat :=15;
  end if;
RETURN disc;
    
    END;
  ''')