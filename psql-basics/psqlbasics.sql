/* 
   Author: Jane Doe
   Purpose: Calculate annual revenue summaries
   Date: June 2026
*/

/* 
   Author: Kev
   Purpose: To demonstrate basic SQL operations such as SELECT, INSERT, and DELETE on a products table.
   Date: June 2026
*/

/* 
   The following SQL statements perform various operations on the products table, including selecting all records, inserting new records, and deleting existing records. The RETURNING clause is used in the INSERT and DELETE statements to return the affected records for verification.
*/

-- Select (get, fetch, read) all records from the products table
SELECT * FROM products;

/*
   The following INSERT statements demonstrate how to add new records to the products table. 
   The RETURNING clause is used to return the inserted records for verification.
*/

-- Insert (create) a new product into the products table
INSERT INTO products (name, price, inventory) VALUES ('Car', 7000, 10) returning *;

-- Insert multiple products into the products table
INSERT INTO products (name, price, inventory) VALUES ('Bed', 50, 10), ('Mattress', 25, 10) returning id, name, created_at;

/* 
   update (modify, change) records in the products table
   The following UPDATE statements demonstrate how to modify existing records in the products table.
   The RETURNING clause is used to return the updated records for verification.
*/

-- Update a product's name and inventory in the products table

UPDATE products SET name = 'HP Laptop', inventory = 20 WHERE id = 16 RETURNING *;

-- Updates all products to be on sale and return the updated records
UPDATE products SET is_sale = true RETURNING *;


/*
   The following DELETE statements demonstrate how to remove records from the products table.
   The RETURNING clause is used to return the deleted records for verification.
*/

-- Delete a product from the products table
DELETE FROM products WHERE id = 19;

-- Example1 Delete from the products table and return the deleted record
DELETE FROM products WHERE id = 19 RETURNING *;

-- Example2 Delete from the products table and return the deleted record
DELETE FROM products WHERE id = 18 RETURNING *;

-- Example3 Delete from the products table and return the deleted record
DELETE FROM products WHERE name = 'Smartphone' RETURNING *;

