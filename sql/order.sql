-- docker exec -it postgres /bin/bash
-- psql -U postgres-user customers

CREATE TABLE orders (
    OrderID SERIAL NOT NULL PRIMARY KEY,
    OrderNumber int NOT NULL,
    CustomerID int,
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
    );


ALTER TABLE public.orders REPLICA IDENTITY FULL;

INSERT INTO orders (OrderNumber, CustomerID) VALUES ( 1, 1);
INSERT INTO orders (OrderNumber, CustomerID) VALUES ( 2, 2);
INSERT INTO orders (OrderNumber, CustomerID) VALUES ( 3, 3);
INSERT INTO orders (OrderNumber, CustomerID) VALUES ( 4, 4);

DELETE FROM orders WHERE OrderID = 1;