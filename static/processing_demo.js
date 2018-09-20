const BALL_SIZE = 40;
const GRAVITY = 0.1;

var balls = [];

var running = true;
var show_background = true;

function setup() {
  createCanvas(1000, 800);
  background(100);
}


function draw() {
  if (running) {
    if (show_background) {
      background(100);
    }
    draw_balls();
  }
}

function keyPressed() {
  register_keypress();
}

function keyReleased() {
  register_keyrelease();
}

function mousePressed() {
  new_ball();
}

function stop() {
  running = !running;
}

function toggle_background() {
  show_background = !show_background;
}

function new_ball() {
  balls.push({x: mouseX, y: mouseY, vx: random(-5,5), vy: 0});
}

function draw_balls() {
  for (var i = 0; i < balls.length; i++) {
    var ball = balls[i];
    draw_ball(ball);
  }
}

function draw_ball(ball) {
  bounce(ball);
  ball.x += ball.vx;
  ball.y += ball.vy;
  ball.vy += GRAVITY;
  ellipse(ball.x, ball.y, BALL_SIZE, BALL_SIZE);
}

function bounce(ball) {
  if (ball.x + BALL_SIZE/2 > width || ball.x - BALL_SIZE/2 < 0) {
    ball.vx = -ball.vx*0.98;
  }
  if (ball.y + BALL_SIZE/2 > height) {
    ball.vy = -ball.vy*0.98;
  }
}

