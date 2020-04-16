<div class="wrapper">	

<?php include 'divs/header.php'; ?>

<div class="main-content-container">
	<div class="main-intro">
		<div class="left-box">
			<div class="intro-welcome-first-header">
				<h1>
					Welcome to R.O.O.T.
				</h1>
			</div>
			<div class="intro-welcome-first-msg">
				<p>Hi! I'am CoDev-20 chat bot. I will help you guide through fight against covid-19. With the impending threat of the virus, humans must be cautious at all times. I, CoDev-20 chat bot will help you what things to remember that will help us eradicated covid-19.
</p>
			</div>
			<div class="intro-welcome-second-header">
				<h2>
					Get started by signing up if you don't have an account yet!
				</h2>
			</div>
			<div class="intro-welcome-second-msg">
				<p>
					By signing up to us, you agree to our terms and conditions. See our terms and conditions <a href="">here</a>.
				</p>
			</div>
		</div>
		<div class="right-box">
			<div class="login-box">
			<form method="post" action="index.php" autocomplete="off" name="login-form">
				<div class="login-header">
					<h1><label>Login</label></h1>
				</div>
				<div class="error-container">
					<div class="error-des" id="error_notice_login"></div>
				</div>
				<div class="login-input-holder">
					<input type="text" name="txtUsername" class="text-input-widen" placeholder="Username"><br>
					<input type="password" name="txtPassword" class="text-input-widen" placeholder="Password">
					<br>
					<input type="submit" name="btn" class="button-submit" value="LOGIN">
				</div>
			</form>
			</div>
			<div class="signup-box">
			<form method="post" action="index.php" autocomplete="off" name="signup-form">
				<div class="signup-header">
					<h1><label>Sign Up</label></h1>
				</div>
				<div class="error-container">
					<div class="error-des" id="error_notice_signup"></div>
				</div>
				<div class="signup-input-holder">
					<input type="text" name="txtRegisFname" class="text-input-widen" placeholder="First Name"><span class="error-des" id="firstname_error"></span><br>
					<input type="text" name="txtRegisLname" class="text-input-widen"
						placeholder="Last Name"><span class="error-des" id="lastname_error"></span><br>
					<input type="text" name="txtRegisUsername" class="text-input-widen" placeholder="Username"><span class="error-des" id="username_error"></span><br>
					<input type="password" name="txtRegisPassword" class="text-input-widen"
						placeholder="Password"><span class="error-des" id="password_error"></span><br>
						<input type="password" name="txtRegisConfPassword" class="text-input-widen" placeholder="Confirm Password"><span class="error-des" id="confpassword_error"></span>
					<input type="submit" name="btn" class="button-submit" value="SIGN UP">
				</div>
			</form>
			</div>
		</div>
	</div>
</div>

<script type="text/javascript" src="../BusinessWebsite/js/validation.js"></script>

<?php include 'divs/footer.php'; ?>

</div>
