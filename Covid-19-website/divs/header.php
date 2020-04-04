<div class="header-container">
	<div class="header-content">
		<div class="companytitle">
			<h2><a href='/website/index.php'><?php echo $revCompanyTitle; ?></a></h2>
		</div>
		<?php
		if (isset($_SESSION['activeUserType']))
		{
			if ($_SESSION['activeUserType'] == "customer")
			{
				echo "<div class='logout-holder'>
								<form method='post' action='home.php'>
									<input type='submit' name='btn' class='button-submit-logout' value='Logout'>
								</form>
							</div>
							<div class='navi'>
								<ul>
									<li><a href='home.php'>Home</a></li>
									<li><a href='/website/pages/aboutus.php'>About Us</a></li>
									<li><a href=''>FAQs</a></li>
									<li><a href='/website/pages/cart.php'>Cart</a></li>
									<li><a href='/website/pages/account.php'>Account</a></li>
								</ul>
							</div>";
			}
			else if ($_SESSION['activeUserType'] == "admin")
			{
				echo "<div class='logout-holder'>
								<form method='post' action='admin.php'>
									<input type='submit' name='btn' class='button-submit-logout' value='Logout'>
								</form>
							</div>
							<div class='admin-title-holder'>
								<h2>Administrator Mode</h2>
							</div>";
			}
		}
		else
		{
			echo "<div class='navi'>
					<ol>
						<li><a href='/website/pages/login.php'>Login</a></li>
					</ol>
					<ul>
						<li><a href='/website/index.php'>Home</a></li>
						<li><a href='/website/pages/aboutus.php'>About Us</a></li>
						<li><a href=''>FAQs</a></li>
					</ul>
				</div>";
		}

		?>
	</div>
</div>
