$("#toggle_header").click(() => {
  if ($("header").hasClass("red")) {
    $("header").removeClass("red");
    $("header").addClass("green");
  } else {
    $("header").removeClass("green");
    $("header").addClass("red");
  }
})