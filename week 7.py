#------ More on Databases; Queries

# CREATE TABLE purchase ( id INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY, cust_id INT(10), FOREIGN KEY purchase(cust_id) REFERENCES customer_info(id), product VARCHAR(20) NOT NULL, price FLOAT(10, 2) NOT NULL, `date` DATE NOT NULL )
# SELECT * FROM `purchase`
# INSERT INTO purchase (cust_id, product, price, `date`) VALUES (4, "iPhone 12 pro max", 1119.99, "2021-02-14")
# INSERT INTO purchase (product, price, `date`) VALUES ("Large Hydron Collider", 1200000, "2021-02-14")
# INSERT INTO purchase (cust_id, product, price, `date`) VALUES (1, "Telescope", 849.99, "2021-03-10")
# INSERT INTO purchase (cust_id, product, price, `date`) VALUES (2, "Macbook M1", 1500.99, "2021-05-17")
# INSERT INTO purchase (product, price, `date`) VALUES ("Hoverboard", 2000, "2021-06-06")
# INSERT INTO purchase (cust_id, product, price, `date`) VALUES (5, "Replica Light-Saber", 2999.99, "2021-06-06")
# SELECT * FROM purchase
# SELECT * FROM purchase
# SELECT * FROM purchase
# SELECT * FROM purchase
# SELECT * FROM purchase
# INSERT INTO purchase (cust_id, product, price, `date`) VALUES (5, "Replica Millenium Falcon", 3599.99, "2021-05-14")
# SELECT * FROM `purchase`
# INSERT INTO purchase (cust_id, product, price, `date`) VALUES (4, "Apple Air Pods", 399.99, "2021-05-14")
# SELECT * FROM `purchase`
# SELECT * FROM `purchase`
# SELECT * FROM `purchase`
# SELECT * FROM `purchase`
# SELECT * FROM `purchase`
# INSERT INTO purchase (product, price, `date`) VALUES ("Templar Artifact", 599.99, "2021-06-14")
# INSERT INTO purchase (product, price, `date`) VALUES ("Star Gazer", 1599.99, "2021-04-10")
# SELECT * FROM `purchase`
# SELECT * FROM `purchase`
# SELECT * FROM `purchase`
# SELECT * FROM `purchase`
# SELECT * FROM `purchase`
# SELECT * FROM `purchase`
# SELECT * FROM `purchase`
# SELECT * FROM `purchase` ORDER BY `purchase`.`product` ASC
# SELECT * FROM `purchase` ORDER BY `purchase`.`product` DESC
# SELECT * FROM `purchase` ORDER BY `purchase`.`id` ASC
# SELECT * FROM purchase WHERE price = (SELECT MAX(price) FROM purchase)
# SELECT name, location FROM customer_info WHERE id = (SELECT cust_id FROM purchase WHERE price = (SELECT MIN(price) FROM purchase))
# SELECT * FROM customer_info WHERE location LIKE "%America"
# SELECT location, AVG(age) AS "average age" FROM customer_info GROUP BY location
# SELECT * FROM customer_info WHERE location IN ("Italy", "United Kingdom", "United states of America", "Ontario, Canada", "Geneva, Switzerland")
# SELECT * FROM customer_info WHERE location NOT IN ("Italy", "United Kingdom", "United states of America", "Ontario, Canada", "Geneva, Switzerland")
# SELECT location, gender, COUNT(gender) AS "gender count" FROM customer_info GROUP BY location, gender
# SELECT customer_info.name, customer_info.location, purchase.product, purchase.price, customer_info.gender FROM customer_info INNER JOIN purchase ON customer_info.id = purchase.cust_id ORDER BY purchase.price DESC
# SELECT customer_info.name, customer_info.location, purchase.product, purchase.price, customer_info.gender FROM customer_info LEFT JOIN purchase ON customer_info.id = purchase.cust_id WHERE customer_info.gender = "Male"
# SELECT customer_info.name, customer_info.location, purchase.product, purchase.price, customer_info.gender FROM customer_info LEFT JOIN purchase ON customer_info.id = purchase.cust_id
# UNION
# SELECT customer_info.name, customer_info.location, purchase.product, purchase.price, customer_info.gender FROM customer_info RIGHT JOIN purchase ON customer_info.id = purchase.cust_id