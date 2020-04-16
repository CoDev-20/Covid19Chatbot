<?php include('../php/conn.php'); ?>


<?php include('../php/retrieve.php'); ?>

<!DOCTYPE html>
<html>
<head>
	<title><?php echo $revCompanyTitle; ?> | Home</title>
	<meta charset="utf-8">
	<meta meta="viewport" content="width=device-width">
	<link rel="stylesheet" type="text/css" href="../css/css-main.css" />
</head>
<body>
<div class="wrapper">
	<?php include('../divs/header.php'); ?>
	<div class="whole-container">
		<div class="aboutus-content">
			<h1>About Us</h1>
			<p><?php echo $revCompanyAboutUs; ?></p>
		</div>
		<div class="missionvision-content">
			<h1>Mission</h1>
			<p><?php echo $revCompanyMission; ?></p>
			<h1>Vision</h1>
			<p><?php echo $revCompanyVision; ?></p>
		</div>
	</div>
</div>
</body>
</html>