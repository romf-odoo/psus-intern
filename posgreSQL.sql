SELECT * FROM cd.facilities
--  print out a list of all of the facilities and their cost to members. How would you retrieve a list of only facility names and costs
SELECT name, membercost FROM cd.facilities

-- produce a list of facilities that charge a fee to members
SELECT * FROM cd.facilities WHERE membercost > 0
-- produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.
Select facid, name, membercost, monthlymaintenance FROM cd.facilities
WHERE membercost > 0 and (membercost < monthlymaintenance/50)
-- produce a list of all facilities with the word 'Tennis' in their name
SELECT * FROM cd.facilities where name LIKE '%Tennis%'
-- etrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator. 
SELECT * FROM cd.facilities WHERE facid in(1,5)
-- produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly maintenance cost is more than $100? Return the name and monthly maintenance of the facilities in question.

SELECT name, CASE WHEN (monthlymaintenance > 100) then
		'expensive'
	else
		'cheap'
	end as cost
	from cd.facilities;    

-- Produce a list of members who joined after the start of September 2012 Return the memid, surname, firstname, and joindate of the members in question. 
SELECT memid, surname, firstname, joindate FROM cd.members WHERE joindate > '2012-09-01'
-- produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.
SELECT DISTINCT surname FROM cd.members ORDER BY surname limit 10
