<?php include('../php/conn.php'); ?>

<?php
if (isset($_SESSION['activeUserType']))
{
	if ($_SESSION['activeUserType'] != "customer")
	{
		header("Location: /website/index.php");
		exit;
	}
}
?>

<?php include('../php/retrieve.php'); ?>

<?php
if (isset($_POST['btn']))
{
	if ($_POST['btn'] == "Logout")
	{
		session_unset();
		session_destroy();
		header("Location: ../index.php");
		exit;
	}
}

$_SESSION['cartNameGlobal'] = "tbl_cart_".$_SESSION['activeUser'];
$cartName = $_SESSION['cartNameGlobal'];
if (isset($_POST['btnAddToCart']))
{
	$addedToCartProd = $_POST['btnAddToCart'];
	$key = false;
	$sql = "SELECT * FROM $cartName";
	$exists = mysqli_query($db, $sql);
	if (!($exists))
	{
		$sql = "CREATE TABLE $cartName (productid INT(10) NOT NULL , productname VARCHAR(50) NOT NULL , stockbought INT(10) NOT NULL , totalprice DECIMAL(10,2) NOT NULL)ENGINE = InnoDB";
		$result = mysqli_query($db, $sql);
		if (!($result))
		{
    		$_SESSION['error'] = "An error has occurred. Contact developer for assistant.";
    		header("Location: home.php");
    		$key = false;
    		exit;
		}
		else
		{
			$key = true;
		}
	}
	else
	{
		$key = true;
	}
	if ($key)
	{
		$sql = "SELECT * FROM tbl_items WHERE productid = '$addedToCartProd' ";
		$query = mysqli_query($db, $sql);
		while ($items = mysqli_fetch_array($query))
		{
			$prodName = $items['productname'];
			$prodPrice = $items['productprice'];
			$prodStock = $items['productstock'];
		}
		if ($prodStock != 0)
		{
			$countBought = 1;
			$sql = "SELECT * FROM $cartName WHERE productid = '$addedToCartProd'";
			$result = mysqli_query($db, $sql);
			/***** Insert Product If Doesn't Exist *****/
			if (mysqli_num_rows($result) == 0)
			{
				$sql = "INSERT INTO $cartName (productid, productname, stockbought, totalprice) VALUES ('$addedToCartProd', '$prodName', '$countBought', '$prodPrice')";
				$result = mysqli_query($db, $sql);
				if ($result)
				{
					$curStock = $prodStock - $countBought;
					$sql = "UPDATE tbl_items SET productstock = '$curStock' WHERE productid = '$addedToCartProd'";
					$result = mysqli_query($db, $sql);
					if ($result)
					{
						$_SESSION['notice'] = $prodName." has been added successfully! Check your cart list.";
    					header("Location: home.php");
    					exit;
					}
					else
					{
						$_SESSION['error'] = "Adding to Cart Failed: An error has occured. Contact developer for assistant.";
    					header("Location: home.php");
    					exit;
					}
				}
				else
				{
					$_SESSION['error'] = "Adding to Cart Failed: An error has occured. Contact developer for assistant.";
    				header("Location: home.php");
    				exit;
				}
			}
			/***** Update Product If It Exist *****/
			else
			{
				$newTotalPrice = $countBought * $prodPrice;
				$sql = "SELECT * FROM $cartName WHERE productid = '$addedToCartProd'";
				$query = mysqli_query($db, $sql);
				while ($existProd = mysqli_fetch_array($query))
				{
					$newStockBought = $countBought + $existProd['stockbought'];
					$newTotalPrice = $newTotalPrice + $existProd['totalprice'];
				}
				$sql = "UPDATE $cartName SET stockbought = '$newStockBought', totalprice = '$newTotalPrice' WHERE productid = '$addedToCartProd'";
				$query = mysqli_query($db, $sql);
				if ($query)
				{
					$curStock = $prodStock - $countBought;
					$sql = "UPDATE tbl_items SET productstock = '$curStock' WHERE productid = '$addedToCartProd'";
					$query = mysqli_query($db, $sql);
					if ($query)
					{
						$_SESSION['notice'] = $prodName." has been added successfully! Check your cart list.";
    					header("Location: home.php");
    					exit;
					}
					else
					{
					$_SESSION['error'] = "Adding to Cart Failed: An error has occured. Contact developer for assistant.";
    				header("Location: home.php");
    				exit;
					}
				}
				else
				{
					$_SESSION['error'] = "Adding to Cart Failed: An error has occured. Contact developer for assistant.";
    				header("Location: home.php");
    				exit;
				}
			}
		}
		else
		{
			$_SESSION['error'] = "Adding to Cart Failed: Out of Stock.";
    		header("Location: home.php");
    		exit;
		}
	}
}
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta meta="viewport" content="width=device-width">
	<link rel="stylesheet" type="text/css" href="../css/css-main.css">
	<link rel="stylesheet" type="text/css" href="../css/css-responsive.css">
	<title><?php echo $revCompanyTitle; ?> | Home</title>
</head>
<body>
<div class="wrapper">

<?php include '../divs/header.php'; ?>

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
	<div class="greetings-container">
		<div class="greetings-content">
			<div class="greetings-header">
				<h1>Welcome, <?php if(isset($_SESSION['activeUser'])) { echo $_SESSION['activeUser']; } ?> </h1>
			</div>
		</div>
	</div>
<form method="post" action="home.php" autocomplete="off">
<?php
$itemStock = 0;
$sql = "SELECT * FROM tbl_items";
$result = mysqli_query($db, $sql);
$counter = 1;
$dir = "website/img/";
while ($items = mysqli_fetch_array($result))
{
	$modulo = $counter % 2;
	if ($modulo == 1)
	{
		if ($items['productstock'] == 0)
			$itemStock = "Out of Stock";
		else
			$itemStock = $items['productstock'];
		echo "<div class='menu'>
		<div class='menu-img' style='background-image: url($items[productimg]); background-size: cover;'></div>
			<div class='menu-msg'>
				<h1>$items[productname]</h1>
				<p>$items[productdesc]</p>
				<h3>Remaining Stocks: $itemStock</h3>
				<button type='submit' name='btnAddToCart' class='menu-buynow' value='$items[productid]'>Add To Cart</button>
			</div>
		</div>";
	}
	else if ($modulo == 0)
	{
		echo "<div class='menu'>
		<div class='menu-img-reverse' style='background-image: url($items[productimg]); background-size: cover;'></div>
			<div class='menu-msg-reverse'>
				<h1>$items[productname]</h1>
				<p>$items[productdesc]</p>
				<h3>Remaining Stocks: $items[productstock]</h3>
				<button type='submit' name='btnAddToCart' class='menu-buynow' value='$items[productid]'>Add To Cart</button>
			</div>
		</div>";
	}
	$counter = $counter + 1;
}
?>
</form>
</div>
</div>
</body>
</html>