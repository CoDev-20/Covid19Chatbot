<?php include('php/conn.php'); ?>

<?php
if (isset($_SESSION['activeUserType']))
{
	if ($_SESSION['activeUserType'] == "customer")
	{
		header("Location: /website/pages/home.php");
		exit;
	}
	else if ($_SESSION['activeUserType'] == "admin")
	{
		header("Location: /website/pages/admin.php");
		exit;
	}
}
?>

<?php include('php/retrieve.php'); ?>

<!DOCTYPE html>
<html>
<head>
	<title><?php echo $revCompanyTitle; ?> | Home</title>
	<meta charset="utf-8">
	<meta meta="viewport" content="width=device-width">
	<link rel="stylesheet" type="text/css" href="css/css-main.css" />
</head>
<body>
<div class="wrapper">
	<?php include('divs/header.php'); ?>
	<?php
	if (isset($_SESSION['notice']))
	{
  		if ($_SESSION['notice'] != "")
  		{
  			echo "<div class='notice-message'>".$_SESSION['notice']."</div>";
  		}
	}
	if (isset($_SESSION['error']))
	{
  		if ($_SESSION['error'] != "")
  		{
    		echo "<div class='notice-error'>".$_SESSION['error']."</div>";
  		}
	}
	$_SESSION['notice'] = "";
	$_SESSION['error'] = "";
	?>

	<div class="container">
		<div class="header-msg-container">
			<div class="header-msg-content">
				<div class="header-msg">
					<h1>Welcome to <?php echo $revCompanyTitle; ?></h1>
					<h3><?php echo $revHomeMessage; ?></h3>
				</div>
				<div class="sub-msg">
					<h3>Get started by signing up if you don't have an account yet! Sign up <a href="../website/pages/signup.php">here</a>. See our terms and conditions <a href="">here</a></h3>
				</div>
			</div>
		</div>
	</div>
</div>
</body>
</html>