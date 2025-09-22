drop  database if exists asst;
create database asst;
use asst;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;

-- Employees Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    job_title VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO employees VALUES
(1, 'Alice', 101, 'Engineer', 70000),
(2, 'Bob', 101, 'Engineer', 80000),
(3, 'Charlie', 102, 'Analyst', 65000),
(4, 'Daisy', 103, 'Manager', 90000),
(5, 'Ethan', 102, 'Analyst', 70000);

-- Sales Table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    category_id INT,
    sales_amount DECIMAL(10, 2),
    sale_date DATE
);

INSERT INTO sales VALUES
(1, 201, 10, 1000.00, '2024-01-01'),
(2, 202, 10, 1500.00, '2024-01-03'),
(3, 203, 11, 2000.00, '2024-01-04'),
(4, 201, 10, 500.00, '2024-01-05'),
(5, 203, 11, 1000.00, '2024-01-06');

-- Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    region VARCHAR(50),
    status VARCHAR(20),
    sales_amount DECIMAL(10, 2)
);

INSERT INTO orders VALUES
(1001, 301, 201, '2024-02-01', 'North', 'Shipped', 500.00),
(1002, 302, 202, '2024-02-01', 'North', 'Pending', 600.00),
(1003, 303, 203, '2024-02-02', 'South', 'Shipped', 800.00),
(1004, 301, 202, '2024-02-03', 'North', 'Shipped', 900.00),
(1005, 304, 203, '2024-02-03', 'South', 'Cancelled', 750.00),
(1006, 302, 201, '2024-02-04', 'North', 'Pending', 300.00);

-- Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category_id INT,
    price DECIMAL(10, 2)
);

INSERT INTO products VALUES
(201, 'Widget', 10, 25.00),
(202, 'Gadget', 10, 40.00),
(203, 'Thingamajig', 11, 100.00),
(204, 'Doohickey', 12, 10.00);



/*  Q1  Top-Selling Product in Each Category
*/
select sa.category_id, sa.product_id, p.product_name, 
    sum(sa.sales_amount) as total_sales from sales sa
    join products p on sa.product_id = p.product_id
    group by sa.category_id ,sa.product_id,p.product_name
    having sum(sa.sales_amount) = (select max(subt.total_sales) from(
    select s2.product_id ,sum(s2.sales_amount) as total_sales
    from sales s2 
    where s2.category_id = sa.category_id
    group by s2.product_id) as subt
    );
/*Q2: List  Department with the Highest Average Salary
*/


select department_id, avg(salary) as avg_salary
from employees  group by department_id 
order by avg_salary desc limit 1;

/*Q3: List  Employees Who Earn More Than Department Average
*/



select e.employee_id ,e.name,e.department_id,e.salary
from employees e where e.salary > (select avg(salary) from employees
where department_id = e.department_id);

/*Q4: List  Customer with Most Orders per Region
*/

select o1.region, o1.customer_id, count(*) as order_count
from orders o1 group by o1.region, o1.customer_id
having count(*) = (select max(customer_order_count)
from (select count(*) as customer_order_count
from orders o2 where o2.region = o1.region
group by o2.customer_id) as region_customer_counts
);


/*Q5: List  Categories Where Average Price > Overall Average Price*/

select category_id,avg(price) as avg_category_price from products
group by category_id having avg(price)> (select avg(price) from products);

/*Q6: list PRODUCT NEVER ORDER */

select p.product_id, p.product_name from products p 
left  join orders o ON p.product_id = o.product_id
where o.product_id is null;