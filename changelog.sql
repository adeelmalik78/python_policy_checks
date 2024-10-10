--liquibase formatted sql

--changeset adeel:table1 stripComments:false
-- this is a comment
create table table1 (
    id int,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    address1 varchar(50),
    address2 varchar(50),
    city varchar(30),
    CONSTRAINT "xpk_table1" PRIMARY KEY (id), 
    CONSTRAINT "xak_table1" UNIQUE (id,last_name) 
)
--rollback drop table table1

--changeset adeel:table1_index
create index xie01_table1 on table1 ( id, first_name, last_name, address1, address2, city );
--rollback drop index xie01_table1 

--changeset adeel:table2
create table table2 (
    id int,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    address1 varchar(50),
    address2 varchar(50),
    city varchar(30),
    CONSTRAINT "xpk_table2" PRIMARY KEY (id), 
    CONSTRAINT "xak_table2" UNIQUE (id,last_name)
);
CREATE TABLE my_sneaky_table (id int);
--rollback drop table table2;
--rollback drop table my_sneaky_table;

--changeset adeel:table2_index
create index xie_table2 on table2 ( id, first_name, last_name, address1, address2, city );
--rollback drop index xie_table2 

--changeset adeel:person
CREATE TABLE person (
    id int,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    CONSTRAINT "pk_person" PRIMARY KEY (id), 
    CONSTRAINT "ak_person" UNIQUE (id,last_name)
)
--rollback drop table person

--changeset adeel:person_index
create index xie03_person on person ( id, first_name, last_name );
--rollback drop index xie03_person

--changeset adeel:fk_table1
alter table table1 add constraint fk_table1 foreign key (id) references table2 (id);
--rollback alter table table1 drop constraint fk_table1;

--changeset adeel:xfk_table2
alter table table2 add constraint xfk_table2 foreign key (id) references table1 (id);
--rollback alter table table2 drop constraint xfk_table2;

--changeset adeel:employee
CREATE TABLE "employee+" (
    id int,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    CONSTRAINT "xpk_employee" PRIMARY KEY (id), 
    CONSTRAINT "xak_employee" UNIQUE (id,last_name)
)
--rollback drop table "employee+"

--changeset adeel:employee_rename
-- RENAME TABLE "employee+" TO "employee-"
ALTER TABLE "employee+" RENAME TO "employee-"
--rollback ALTER TABLE "employee-" RENAME TO "employee+"

--changeset amalik:insert_adeel
INSERT INTO person (id,first_name,last_name)
	VALUES (1,'Adeel','Ashraf');
--rollback DELETE FROM person WHERE id=1;

--changeset amalik:insert_amy
INSERT INTO person (id,first_name,last_name)
	VALUES (2,'Amy','Smith');
--rollback DELETE FROM person WHERE id=2;

--changeset amalik:insert_roderick 
-- Let's create multiple INSERTs into this changeset!S
INSERT INTO person (id,first_name,last_name) VALUES (3,'Roderick','Bowser');
INSERT INTO person (id,first_name,last_name) VALUES (4,'Don','DeArmond III');
--rollback DELETE FROM person WHERE id=3;

--changeset amalik:update_adeel
UPDATE person
	SET first_name='Ryan', last_name='Campbell'
	WHERE id=1;
--rollback UPDATE person SET first_name='Adeel', last_name='Malik' WHERE id=1;

--changeset amalik:boss_view
CREATE VIEW boss AS
    SELECT *
    FROM person
    WHERE id = '1';
--rollback DROP VIEW boss;