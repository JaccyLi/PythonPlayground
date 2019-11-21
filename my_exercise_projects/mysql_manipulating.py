import mysql.connector


mydb1=mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "stevenux",
    database = "pytest",
)

mydb2=mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "stevenux",
    database = "hellodb",
)


cursor2 = mydb2.cursor()
#print(mydb2)


sqlFormula_create_hellodb="CREATE DATABASE IF NOT EXISTS hellodb DEFAULT CHARACTER SET utf8;"

sqlFormula_create_classes="""CREATE TABLE classes ( 
  ClassID tinyint(3) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Class varchar(100) DEFAULT NULL,
  NumOfStu smallint(5) unsigned DEFAULT NULL
  ) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;"""
sqlFormula_insert_classes="INSERT INTO classes VALUES (1,'Shaolin Pai',10),(2,'Emei Pai',7),(3,'QingCheng Pai',11),(4,'Wudang Pai',12),(5,'Riyue Shenjiao',31),(6,'Lianshan Pai',27),(7,'Ming Jiao',27),(8,'Xiaoyao Pai',15);"

sqlFormula_create_coc="""CREATE TABLE coc (
  ID int(10) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  ClassID tinyint(3) unsigned NOT NULL,
  CourseID smallint(5) unsigned DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;"""
sqlFormula_insert_coc="INSERT INTO coc VALUES (1,1,2),(2,1,5),(3,2,2),(4,2,6),(5,3,1),(6,3,7),(7,4,5),(8,4,2),(9,5,1),(10,5,9),(11,6,3),(12,6,4),(13,7,4),(14,7,3);"

sqlFormula_create_courses="""
CREATE TABLE courses (
  CourseID smallint(5) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Course varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
"""
sqlFormula_insert_courses="INSERT INTO courses VALUES (1,'Hamo Gong'),(2,'Kuihua Baodian'),(3,'Jinshe Jianfa'),(4,'Taiji Quan'),(5,'Daiyu Zanghua'),(6,'Weituo Zhang'),(7,'Dagou Bangfa');"


sqlFormula_create_scores="""CREATE TABLE scores (
  ID int(10) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  StuID int(10) unsigned NOT NULL,
  CourseID smallint(5) unsigned NOT NULL,
  Score tinyint(3) unsigned DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
"""
sqlFormula_insert_scores="INSERT INTO scores VALUES (1,1,2,77),(2,1,6,93),(3,2,2,47),(4,2,5,97),(5,3,2,88),(6,3,6,75),(7,4,5,71),(8,4,2,89),(9,5,1,39),(10,5,7,63),(11,6,1,96),(12,7,1,86),(13,7,7,83),(14,8,4,57),(15,8,3,93);"


sqlFormula_create_students="""
CREATE TABLE students (
  StuID int(10) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Name varchar(50) NOT NULL,
  Age tinyint(3) unsigned NOT NULL,
  Gender enum('F','M') NOT NULL,
  ClassID tinyint(3) unsigned DEFAULT NULL,
  TeacherID int(10) unsigned DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
"""
sqlFormula_insert_students="INSERT INTO students VALUES (1,'Shi Zhongyu',22,'M',2,3),(2,'Shi Potian',22,'M',1,7),(3,'Xie Yanke',53,'M',2,16),(4,'Ding Dian',32,'M',4,4),(5,'Yu Yutong',26,'M',3,1),(6,'Shi Qing',46,'M',5,NULL),(7,'Xi Ren',19,'F',3,NULL),(8,'Lin Daiyu',17,'F',7,NULL),(9,'Ren Yingying',20,'F',6,NULL),(10,'Yue Lingshan',19,'F',3,NULL),(11,'Yuan Chengzhi',23,'M',6,NULL),(12,'Wen Qingqing',19,'F',1,NULL),(13,'Tian Boguang',33,'M',2,NULL),(14,'Lu Wushuang',17,'F',3,NULL),(15,'Duan Yu',19,'M',4,NULL),(16,'Xu Zhu',21,'M',1,NULL),(17,'Lin Chong',25,'M',4,NULL),(18,'Hua Rong',23,'M',7,NULL),(19,'Xue Baochai',18,'F',6,NULL),(20,'Diao Chan',19,'F',7,NULL),(21,'Huang Yueying',22,'F',6,NULL),(22,'Xiao Qiao',20,'F',1,NULL),(23,'Ma Chao',23,'M',4,NULL),(24,'Xu Xian',27,'M',NULL,NULL),(25,'Sun Dasheng',100,'M',NULL,NULL);"


sqlFormula_create_teachers="""
CREATE TABLE teachers (
  TID smallint(5) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  Name varchar(100) NOT NULL,
  Age tinyint(3) unsigned NOT NULL,
  Gender enum('F','M') DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
"""
sqlFormula_insert_teachers="INSERT INTO `teachers` VALUES (1,'Song Jiang',45,'M'),(2,'Zhang Sanfeng',94,'M'),(3,'Miejue Shitai',77,'F'),(4,'Lin Chaoying',93,'F');"


sqlFormula_create_toc="""
CREATE TABLE toc (
  ID int(10) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  CourseID smallint(5) unsigned DEFAULT NULL,
  TID smallint(5) unsigned DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
sqlFormula_insert_toc=""

EXECUTE=False
INSERT=False
COMMIT=False

if EXECUTE:
    cursor2.execute(sqlFormula_create_coc)
    cursor2.execute(sqlFormula_create_courses)
    cursor2.execute(sqlFormula_create_scores)
    cursor2.execute(sqlFormula_create_students)
    cursor2.execute(sqlFormula_create_teachers)
    cursor2.execute(sqlFormula_create_toc)

if INSERT:
    cursor2.execute(sqlFormula_insert_coc)
    cursor2.execute(sqlFormula_insert_courses)
    cursor2.execute(sqlFormula_insert_scores)
    cursor2.execute(sqlFormula_insert_students)
    cursor2.execute(sqlFormula_insert_teachers)
    cursor2.execute(sqlFormula_insert_toc)

if COMMIT:
    mydb2.commit()

sqlFormula_meta_students="desc students;"
sqlFormula_query_students_1="SELECT * FROM students;"

cursor2.execute(sqlFormula_meta_students)
query_status_students=cursor2.fetchall()

cursor2.execute(sqlFormula_query_students_1)

query_result1=cursor2.fetchall()

for stat in query_status_students:
    print stat
print

for item in query_result1:
    print item



#mycursor = mydb1.cursor()
#sqlFormula_insert="INSERT INTO students (name,summary) VALUES (%s, %s)"
#sqlFormula_query1="SELECT * FROM students WHERE ID > %d;"
#sqlFormula_query2="SELECT name,count(ID) FROM students GROUP BY name;"
#students=[("mary", "Learning mysql..."),
#          ("jack", "Learning python..."),
#          ("bob", "Doing nothing..."),
#          ("jacob", "Nothing to do...")]
#max_id=mycursor.execute("SELECT MAX(ID) FROM students;")
#for i in mycursor:
#    max_left = i
#print(max_left[0])
#if max_left[0] < 200:
#    for i in range(50):
#        mycursor.executemany(sqlFormula_insert, students)
#        mydb1.commit()
#mycursor.execute(sqlFormula_query2)
#for item in mycursor:
#    print(item)
#
#mycursor.executemany(sqlFormula_query, 190)

# mycursor.execute("CREATE DATABASE PYTEST;")
#mycursor.execute("SELECT HOST,USER,authentication_string FROM MYSQL.USER;")
#mycursor.execute("INSERT INTO students (name, summary) VALUES ('matiandia','Learning nothing...');")
#mycursor.execute("SELECT * FROM students;")
#mycursor.execute("TRUNCATE students;")
#mycursor.execute("CREATE TABLE LEARN (ID int unsigned auto_increment primary key , NAME varchar(20) not null , SUMMARY varchar(255));")
#mycursor.execute("insert into learn (NAME,SUMMARY) values ('jack','Learning python...');insert into learn (NAME,SUMMARY) values ('mary','Learning mysql...');")
