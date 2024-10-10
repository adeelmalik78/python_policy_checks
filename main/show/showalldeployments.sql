--liquibase formatted sql

--changeset amalik:showInserts runAlways:true
select * from person;
--rollback empty
