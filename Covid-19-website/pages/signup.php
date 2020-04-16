<?php include('../php/conn.php'); ?>

<?php include('../php/retrieve.php'); ?>

<?php
if (isset($_POST['btnSignUp']))
{
	$regFirstName = mysqli_real_escape_string($db, $_POST['txtFirstName']);
	$regLastName = mysqli_real_escape_string($db, $_POST['txtLastName']);
	$regUsername = mysqli_real_escape_string($db, $_POST['txtUsername']);
	$regEmail = mysqli_real_escape_string($db, $_POST['txtEmail']);
	$regPass = mysqli_real_escape_string($db, $_POST['txtPassword']);
	$regConfPass = mysqli_real_escape_string($db, $_POST['txtConfPassword']);

	$_SESSION['regSesFirstName'] = $regFirstName;
	$_SESSION['regSesLastName'] = $regLastName;
	$_SESSION['regSesUsername'] = $regUsername;
	$_SESSION['regSesEmail'] = $regEmail;
	$noErr = true;

	/***** Validations *****/
	if (!(empty($regFirstName)))
	{
		if (ctype_alpha($regFirstName))
		{

		}
		else
		{
			$_SESSION['firstNameErr'] = "First name is not valid.";
			$noErr = false;
		}
	}
	else
	{
		$_SESSION['firstNameErr'] = "Enter your First Name.";
		$noErr = false;
	}

	if (!(empty($regLastName)))
	{
		if (ctype_alpha($regLastName))
		{
			
		}
		else
		{
			$_SESSION['lastNameErr'] = "Last name is not valid.";
			$noErr = false;
		}
	}
	else
	{
		$_SESSION['lastNameErr'] = "Enter your Last Name.";
		$noErr = false;
	}
		
	if (!(empty($regUsername)))
	{
		if (!(strlen($regUsername) < 8))
		{
			if (ctype_alnum($regUsername))
			{
				$sql = "SELECT * FROM tbl_accounts WHERE username = '$regUsername'";
				$query = mysqli_query($db, $sql);
				if (mysqli_num_rows($query) == 0)
				{
					
				}
				else
				{
					$_SESSION['usernameErr'] = "Username is already taken.";
					$noErr = false;
				}
			}
			else
			{
				$_SESSION['usernameErr'] = "Numbers and letters only for username.";
				$noErr = false;
			}
		}
		else
		{
			$_SESSION['usernameErr'] = "Minimum character for username is 8 only.";
			$noErr = false;
		}
	}
	else
	{
		$_SESSION['usernameErr'] = "Enter your Username.";
		$noErr = false;
	}

	if (!(empty($regEmail)))
	{
		if (filter_var($regEmail, FILTER_VALIDATE_EMAIL))
		{
			$sql = "SELECT * FROM tbl_accounts WHERE email = '$regEmail'";
			$query = mysqli_query($db, $sql);
			if (mysqli_num_rows($query) == 0)
			{
				
			}
			else
			{
				$_SESSION['emailErr'] = "Email is already taken.";
				$noErr = false;
			}
		}
		else
		{
			$_SESSION['emailErr'] = "Email is not valid.";
			$noErr = false;
		}
	}
	else
	{
		$_SESSION['emailErr'] = "Enter your valid Email.";
		$noErr = false;
	}

	if (!(empty($regPass)))
	{
		if (!(strlen($regPass) < 8))
		{
			if (ctype_alnum($regPass))
			{
				if ($regPass == $regConfPass)
				{

				}
				else
				{
					$_SESSION['passwordErr'] = "Password doesn't match with confirmation.";
					$noErr = false;
				}
			}
			else
			{
				$_SESSION['passwordErr'] = "Numbers and letters only for password.";
				$noErr = false;
			}
		}
		else
		{
			$_SESSION['passwordErr'] = "Minimum character for password is 8 only.";
			$noErr = false;
		}
	}
	else
	{
		$_SESSION['passwordErr'] = "Enter your desired password.";
		$noErr = false;
	}

	if (!(empty($regConfPass)))
	{
		
	}
	else
	{
		$_SESSION['confPasswordErr'] = "Confirm your password.";
		$noErr = false;
	}

	if ($noErr)
	{
			$securedPass = password_hash($regPass, PASSWORD_DEFAULT);
			$sql = "INSERT INTO tbl_accounts (accid, firstname, lastname, username, password, usertype, email, address, activated, packbought) VALUES (NULL, '$regFirstName', '$regLastName', '$regUsername', '$securedPass', 'customer', '$regEmail', NULL, '0', '0')";
			$query = mysqli_query($db, $sql);
			if ($query)
			{
				$_SESSION['notice'] = "Sign Up Successfully! You may now login your account.";

				$_SESSION['regSesFirstName'] = "";
				$_SESSION['regSesLastName'] = "";
				$_SESSION['regSesUsername'] = "";
				$_SESSION['regSesEmail'] = "";

				$_SESSION['firstNameErr'] = "";
				$_SESSION['lastNameErr'] = "";
				$_SESSION['usernameErr'] = "";
				$_SESSION['emailErr'] = "";
				$_SESSION['passwordErr'] = "";
				$_SESSION['confPasswordErr'] = "";

				header("Location: signup.php");
				exit;
			}
			else
			{
				$_SESSION['error'] = "An error has occurred. Contact developer for assistant.";
				header("Location: index.php");
				exit;
			}
	}
	header("Location: signup.php");
	exit;
}
?>

<!DOCTYPE html>
<html>
<head>
	<title><?php echo $revCompanyTitle; ?> | Sign Up</title>
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
	<div class="signup-container">
		<div class="signup-box">
			<label><h1>Sign Up</h1></label>
			<form method="post" action="signup.php" autocomplete="off">
				<input type="text" name="txtFirstName" placeholder="First Name" value="<?php if (isset($_SESSION['regSesFirstName'])) { if ($_SESSION['regSesFirstName'] != '') { echo $_SESSION['regSesFirstName']; } } ?>" /><br/>
				<?php if (isset($_SESSION['firstNameErr'])) { if ($_SESSION['firstNameErr'] != '') { echo "<div class='error-holder'><label>".$_SESSION['firstNameErr']."</label></div>"; } } ?>
				<input type="text" name="txtLastName" placeholder="Last Name" value="<?php if (isset($_SESSION['regSesLastName'])) { if ($_SESSION['regSesLastName'] != '') { echo $_SESSION['regSesLastName']; } } ?>" /><br/>
				<?php if (isset($_SESSION['lastNameErr'])) { if ($_SESSION['lastNameErr'] != '') { echo "<div class='error-holder'><label>".$_SESSION['lastNameErr']."</label></div>"; } } ?>
				<input type="text" name="txtUsername" placeholder="Username" value="<?php if (isset($_SESSION['regSesUsername'])) { if ($_SESSION['regSesUsername'] != '') { echo $_SESSION['regSesUsername']; } } ?>" /><br/>
				<?php if (isset($_SESSION['usernameErr'])) { if ($_SESSION['usernameErr'] != '') { echo "<div class='error-holder'><label>".$_SESSION['usernameErr']."</label></div>"; } } ?>
				<input type="text" name="txtEmail" placeholder="Email" value="<?php if (isset($_SESSION['regSesEmail'])) { if ($_SESSION['regSesEmail'] != '') { echo $_SESSION['regSesEmail']; } } ?>" /><br/>
				<?php if (isset($_SESSION['emailErr'])) { if ($_SESSION['emailErr'] != '') { echo "<div class='error-holder'><label>".$_SESSION['emailErr']."</label></div>"; } } ?>
				<input type="password" name="txtPassword" placeholder="Password" /><br/>
				<?php if (isset($_SESSION['passwordErr'])) { if ($_SESSION['passwordErr'] != '') { echo "<div class='error-holder'><label>".$_SESSION['passwordErr']."</label></div>"; } } ?>
				<input type="password" name="txtConfPassword" placeholder="Confirm Password" /><br/>
				<?php if (isset($_SESSION['confPasswordErr'])) { if ($_SESSION['confPasswordErr'] != '') { echo "<div class='error-holder'><label>".$_SESSION['confPasswordErr']."</label></div>"; } } ?>
				<div class="signup-button-holder">
					<input type="submit" name="btnSignUp" value="SIGN UP" />
				</div>
				<div class="anchor-holder">
					Already have an account? <a href="login.php">Login</a>
				</div>
			</form>
		</div>
	</div>
</div>
</body>
</html>

<?php
$_SESSION['regSesFirstName'] = "";
$_SESSION['regSesLastName'] = "";
$_SESSION['regSesUsername'] = "";
$_SESSION['regSesEmail'] = "";

$_SESSION['firstNameErr'] = "";
$_SESSION['lastNameErr'] = "";
$_SESSION['usernameErr'] = "";
$_SESSION['emailErr'] = "";
$_SESSION['passwordErr'] = "";
$_SESSION['confPasswordErr'] = "";
?>