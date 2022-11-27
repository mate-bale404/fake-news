if ($(window).width() < 400) {
  $("input[type='text']").attr("placeholder", "Input URL");
  $("input[type='text']").css("font-size", "15px");
} else {
  $("input[type='text']").attr("placeholder", "Input The News URL...");
}
