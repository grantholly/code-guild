#Query execution order#

1. FROM - this selects the table(s) needed to satify the query

	- this is where your JOIN clause goes
		- your JOIN clause is executed iteratively on each
		record in the from clause to test the ON clause
		- where the ON clause is true, that record is included
		in the JOIN for further processing

2. WHERE - this is where we filter out records if the WHERE clause
	   is false.

	 - this is also called a search argument or predicate

3. GROUP BY - once we have filtered out records in our tables,
	      we can create aggregates on repeating values in a
	      column.  

	    - An example would be to group records about
	      people into groups by eye color.  We go from having
	      many detail records to having aggregate records that
	      represent groups.

4. HAVING - Now that our detail records have been rolled up into groups,
	    we can iteratively apply another filter, predicate,
            or search argument to rule out groups where the HAVING clause
	    is false.

5. SELECT - Finally, we are actually going to run the first thing we read.
	    For the surviving records, we SELECT the columns, or attributes
	    that we want to know about.

6. ORDER BY - Lastly, we sort the results by a column value.  ASC is the default
	      which is low to high, a - z, old to new, but we can do the
	      opposite with DESC.	    

#Key knowledge#

PK = primary key
	- make every record on the table unique

FK = foreign key
	- make every key value dependant on a parent key value
	- not necessarily a primary key on the parent table
	- establishes referential integrity

#normalization#

Each table is a domain representing an entity.
Normalization is the business of splitting up an entity
into smaller tables so that no column, or attribute,
is repeated in any table.  Highly normalized databases
have lots of little (few columns) tables of very specific
data like Customer_contact, Customer_detail, Customer_settings,
etc.

Each table is a locking domain meaning that an entire record is locked
across a table during write operations.  By having smaller tables, we
don't have to lock everything about a Cutomer during an update to a
subset of the Customer attributes.  This makes normalized databases
write optimized.
