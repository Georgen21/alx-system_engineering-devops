0x14. MySQL

0. Install MySQL - mandatory
First things first, let’s get MySQL installed on both your web-01 and web-02 servers.

1. Let us in! - mandatory
In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.

2. If only you could see what I've seen with your eyes - mandatory
In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

3. Quite an experience to live in fear, isn't it? - mandatory
Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.

4. Setup a Primary-Replica infrastructure using MySQL - mandatory
Having a replica member on for your MySQL database has 2 advantages:
Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data
Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed

5. MySQL backup - mandatory
What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That’s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.
Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
Requirements:
The MySQL dump must contain all your MySQL databases
The MySQL dump must be named backup.sql
The MySQL dump file has to be compressed to a tar.gz archive
This archive must have the following name format: day-month-year.tar.gz
The user to connect to the MySQL database must be root
The Bash script accepts one argument that is the password used to connect to the MySQL database
