<?php
defined('BASEPATH') OR exit('No direct script access allowed');
?>
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">


  <!-- Bootstrap core CSS -->
  <?php echo link_tag('Assets/vendor/bootstrap/css/bootstrap.min.css'); ?>

  <!-- Custom fonts for this template -->
  <link href="https://fonts.googleapis.com/css?family=Saira+Extra+Condensed:500,700" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Muli:400,400i,800,800i" rel="stylesheet">
  <?php echo link_tag('Assets/vendor/fontawesome-free/css/all.min.css'); ?>
  <?php echo link_tag('Assets/css/tictactoe.css'); ?>
<!--  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet"> -->

  <!-- Custom styles for this template -->
  <?php echo link_tag('Assets/css/resume.min.css'); ?>
<!--  <link href="css/resume.min.css" rel="stylesheet"> -->

</head>

<body id="page-top">
    
    <hr class="m-0">

    <section class="resume-section p-3 p-lg-5 d-flex justify-content-center" id="funproject">
      <div class="w-100">

        <div class="resume-item d-flex flex-column flex-md-row justify-content-between mb-5">
          <div class="resume-content">
            <h3 class="mb-0">Let's teach this bot to play tic tac toe</h3>
            <div class="subheading mb-3">This bot will keep improving it's skill by playing with you.</div>
            <p>reference:</p>
			<p>https://flakari.github.io/tic-tac-toe/ (tic tac toe board)</p>
			 <!-- game board -->
			<div id="score">
				<table class="table">
					<thead>
						<tr>
							<th>You</th>
							<th>Bot</th>
						</tr>
					</thead>
					<tr>
						<td id="your_score">0</th>
						<td id="bot_score">0</th>
					</tr>
				</table>
			</div>			 
			<div id="penampung">
				<div id="game-board">
					<div class="game-space top left" id="1" onclick="execute(1)"></div>
					<div class="game-space top" id="2" onclick="execute(2)"></div>
					<div class="game-space top right" id="3" onclick="execute(3)"></div>
					<div class="game-space left" id="4" onclick="execute(4)"></div>
					<div class="game-space" id="5" onclick="execute(5)"></div>
					<div class="game-space right" id="6" onclick="execute(6)"></div>
					<div class="game-space bottom left" id="7" onclick="execute(7)"></div>
					<div class="game-space bottom" id="8" onclick="execute(8)"></div>
					<div class="game-space bottom right" id="9" onclick="execute(9)"></div>
				</div>
          <!-- end of game board -->
				<br><div id="kondisi"><h2>On Game</h2></div>
				<button type="button" onclick="reset_move()" class="btn btn-primary btn-lg btn-block">Restart</button>
          </div>
        </div>

    </section>

  <!-- Bootstrap core JavaScript -->
  
  <script src='<?php echo base_url(); ?>Assets/vendor/jquery/jquery.min.js'></script>
  <script src='<?php echo base_url(); ?>Assets/vendor/bootstrap/js/bootstrap.bundle.min.js'></script>

  <!-- Plugin JavaScript -->
  <script src='<?php echo base_url(); ?>Assets/vendor/jquery-easing/jquery.easing.min.js'></script>

  <!-- Custom scripts for this template -->
  <script src='<?php echo base_url(); ?>Assets/js/resume.min.js'></script>
  <script src='<?php echo base_url(); ?>Assets/js/tictactoe.min.js'></script>

</body>

</html>
