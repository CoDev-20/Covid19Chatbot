<?php
/***** Website's Settings and Information Retrieval Codes *****/
$revCompanyTitle = $revCompanyMission = $revCompanyVision = $revCompanyAboutUs = $revCompanyEmail = "";
$sql = "SELECT * FROM tbl_company_info WHERE id = '1'";
$query = mysqli_query($db, $sql);
while ($fetched = mysqli_fetch_array($query))
{
  $revCompanyTitle = $fetched['companytitle'];	
  $revCompanyMission = $fetched['companymission'];
  $revCompanyVision = $fetched['companyvision'];
  $revCompanyAboutUs = $fetched['companyaboutus'];
  $revCompanyEmail = $fetched['companyemail'];
}

$revFirstName = $revLastName = $revEmail = $revAddress = "";
$curUser = "";
if (isset($_SESSION['activeUser']))
{
	$curUser = $_SESSION['activeUser'];
}
$sql = "SELECT * FROM tbl_accounts WHERE username = '$curUser'";
$query = mysqli_query($db, $sql);
while ($acc = mysqli_fetch_array($query))
{
	$revFirstName = $acc['firstname'];
	$revLastName = $acc['lastname'];
	$revEmail = $acc['email'];
	$revAddress = $acc['address'];
}

$revHomeMessage = "";
$sql = "SELECT * FROM tbl_website_settings WHERE id = '1'";
$query = mysqli_query($db, $sql);
while ($fetched = mysqli_fetch_array($query))
{
  $revHomeMessage = $fetched['homemessage'];
}


/***** End of Website's Settings and Information Retrieval Codes *****/
?>
