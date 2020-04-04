<?php
/***** Opening Session *****/
session_start();

/***** Connect to Database *****/
$server = "localhost";
$username = "root";
$password = "";
$database = "root_db";
$db = mysqli_connect($server, $username, $password, $database);
if (!($db))
{
	die("Can't connect to database.");
}
?>
