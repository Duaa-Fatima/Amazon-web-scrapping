create database Amazonn;
use amazonn;
create table categories
(
id int auto_increment primary key,
category_name varchar(255) unique
);
create table products
(
product_id int auto_increment primary key,
URL text,
title text,
asin text,
ratings decimal(3, 2),
category_id int,
sub_category text,
brand_name text,
price decimal(10,2),
product_description text,
foreign key (category_id) references categories(id)
);

create table reviews
(
id int auto_increment primary key,
product_id int,
review text,
foreign key (product_id) references products(product_id)
);

select* from reviews;
select* from  products;
select* from categories;



