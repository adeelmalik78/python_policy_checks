--liquibase formatted sql

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