-- docker exec -it postgres /bin/bash
-- psql -U postgres-user customers

CREATE TABLE customers (CustomerID SERIAL NOT NULL PRIMARY KEY, name TEXT, age INT);
ALTER TABLE public.customers REPLICA IDENTITY FULL;

INSERT INTO customers (name, age) VALUES ( 'fred', 34);
INSERT INTO customers (name, age) VALUES ( 'sue', 25);
INSERT INTO customers (name, age) VALUES ( 'bill', 51);
INSERT INTO customers (name, age) VALUES ( 'jane', 29);

