## MySQL实验楼笔记 1

#### MySQL的基本操作

###### 数据库级别操作
  - 查看数据库：show databases;
  - 使用某一个数据库： use XXX;
  -  创建数据库： create database xxx;
  
###### 表级操作
    - 创建表： create table table\_name(name varchar(20),birth date);
    - 查看表：show tables;
    - 查看表的信息: describe table\_name;(利用该方法查看表的字段及其类型)
    - 从文本文件中加载数据：
      Unix编辑的文件: load data local infile 'path/to/file' into table table_name;
      windows编辑的文件：load data local infile 'path/to/file' into table table_name lines
      terminated by '\r\n';
    -



    这个月19-25 号。

