<?php include('../php/conn.php'); ?>

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

<?php include('../php/retrieve.php'); ?>

<?php
if (isset($_POST['btnLogin']))
{
	$logUser = mysqli_real_escape_string($db, $_POST['txtUser']);
	$logPass = mysqli_real_escape_string($db, $_POST['txtPass']);

	$_SESSION['logSesUser'] = $logUser;
	if (empty($logUser))
	{
		$_SESSION['userErr'] = "Enter your username account.";
	}
	if (empty($logPass))
	{
		$_SESSION['passErr'] = "Enter your password account.";
	}

	if (!(empty($logUser)) &&
		!(empty($logPass)))
	{
		$sql = "SELECT * FROM tbl_accounts WHERE username = '$logUser'";
		$result = mysqli_query($db, $sql);
		if (mysqli_num_rows($result) > 0)
		{	
			while ($acc = mysqli_fetch_array($result))
			{
				$logUser = $acc['username'];
				$logFullName = $acc['firstname']." ".$acc['lastname'];
				$logSecPass = $acc['password'];
				$logUserType = $acc['usertype'];
			}
			if (password_verify($logPass, $logSecPass))
			{
				$_SESSION['activeUser'] = $logUser;
				$_SESSION['activeUserType'] = $logUserType;
				$_SESSION['activeFullName'] = $logFullName;
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
			else
			{
				$_SESSION['passErr'] = "Your password doesn't match with username.";
			}
		}
		else
		{
			$_SESSION['userErr'] = "Account username is not registered.";
		}
	}
	header("Location: login.php");
	exit;
}
?>

<!DOCTYPE html>
<html>
<head>
	<title><?php echo $revCompanyTitle; ?> | Login</title>
	<meta charset="utf-8">
	<meta meta="viewport" content="width=device-width">
	<link rel="stylesheet" type="text/css" href="../css/css-main.css" />
</head>
<body>
<div class="wrapper">
	<?php include('../divs/header.php'); ?>
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
	<div class="login-container">
		<div class="login-box">
			<label><h1>Login</h1></label>
			<form method="post" action="login.php" autocomplete="off">
				<input type="text" name="txtUser" placeholder="Username" value="<?php if (isset($_SESSION['logSesUser'])) { if ($_SESSION['logSesUser'] != '') { echo $_SESSION['logSesUser']; } } ?>" /><br/>
				<?php if (isset($_SESSION['userErr'])) { if ($_SESSION['userErr'] != '') { echo "<div class='error-holder'><label>".$_SESSION['userErr']."</label></div>"; } } ?>
				<input type="password" name="txtPass" placeholder="Password" /><br/>
				<?php if (isset($_SESSION['passErr'])) { if ($_SESSION['passErr'] != '') { echo "<div class='error-holder'><label>".$_SESSION['passErr']."</label></div>"; } } ?>
				<div class="login-button-holder">
					<input type="submit" name="btnLogin" value="LOGIN" />
				</div>
				<div class="anchor-holder">
					Don't have account? <a href="signup.php" style="color: #5DADE2;">Sign Up</a>
				</div>
			</form>
		</div>
	</div>
</div>
</body>
</html>

<?php
$_SESSION['logSesUser'] = "";
$_SESSION['userErr'] = "";
$_SESSION['passErr'] = "";
?>