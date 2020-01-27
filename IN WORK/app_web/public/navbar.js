menu.onclick = function myfunction() {
  let x = document.getElementById("myTopnav");

  if (x.className === "topnav") {
    x.className += " responsive";
  }else {
    x.className = "topnav";
  }
}
// let model = document.getElementsByClassName("modal");
// let btn = document.getElementsByClassName("mybtn");
// let span  = document.getElementsByClassName("close")[0];
//
// btn.onclick = function () {
//   model.style.display="block";
// };
//
// span.onclick = function () {
//   model.style.display = "none";
// };
//
// window.onclick = function (event) {
//   if (event.target == model) {
//     model.style.display="none";
//   };
// };
