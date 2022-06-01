const occupants_details = document.querySelector(".occupants_details");
const add_occupant = document.querySelector(".occupant");
const add_more_occupants = document.querySelector(".add_more_occupants");
const proceed_dependants = document.querySelector(".proceed_dependants");
const section_1 = document.querySelector(".Section_1");
const section_2 = document.querySelector(".section_2");
const section_3 = document.querySelector(".Section_3");
const section_4 = document.querySelector(".Section_4");
const section_5 = document.querySelector(".section_5");
const proceed_employment = document.querySelector(".proceed_employment");
const proceed_credit = document.querySelector(".proceed_credit");
const proceed_submit = document.querySelector(".proceed_submit");
first_page = document.querySelectorAll(".first_page");
const goToFirstPage = document.querySelector(".go_back_page1");
const goToSecondPage = document.querySelector(".go_back_page2");
const go_back_page3 = document.querySelector(".go_back_page3");
const go_back_page4 = document.querySelector(".go_back_page4");

function checkForm(e) {
  let valid = true;

  for (input of first_page) {
    if (input.value.trim() == "") {
      valid = false;

      break;
    }
  }
  return valid;
}

const html = `
 <div class="row row-space counter occupants_details" >
    <div class="col-2">
      <div class="input-group">
        <label class="label">Name</label>
        <input class="input--style-4" type="text" name="first_name" />
      </div>
    </div>
    <div class="col-2">
      <div class="input-group">
        <label class="label">Relationship</label>
        <input class="input--style-4" type="text" name="last_name" />
</div>

     `;

add_occupant.addEventListener("click", function (e) {
  occupants_details.style.display = "";
  add_more_occupants.style.display = "";
  add_occupant.style.display = "none";
  // occupants.textContent = `Occupant ${number}`;
  add_more_occupants.style.display = "";
});

add_more_occupants.addEventListener("click", function (e) {
  //     console.log("hi");
  const all_occupants = document.querySelectorAll(".counter");

  if (all_occupants.length >= 5) {
    alert("Maximum number of Occupants Reached");
    return;
  }
  //     console.log(all_occupants.length + 1);
  occupants_details.insertAdjacentHTML("afterend", html);
});

proceed_dependants.addEventListener("click", function (e) {
  if (checkForm(this)) {
    section_1.style.display = "none";
    section_2.style.display = "block";
  } else {
    alert("Fill all fields");
  }
  // section_1.style.display = "none";
  // section_2.style.display = "block";
});

proceed_employment.addEventListener("click", (e) => {
  section_2.style.display = "none";
  section_3.style.display = "block";
});

proceed_credit.addEventListener("click", (e) => {
  section_3.style.display = "none";
  section_4.style.display = "block";
});

proceed_submit.addEventListener("click", (e) => {
  section_4.style.display = "none";
  section_5.style.display = "block";
});

goToFirstPage.addEventListener("click", function (e) {
  e.preventDefault();
  section_2.style.display = "none";
  section_1.style.display = "block";
});
goToSecondPage.addEventListener("click", function (e) {
  e.preventDefault();

  section_2.style.display = "block";
  section_1.style.display = "none";
  section_3.style.display = "none";
});
go_back_page3.addEventListener("click", function (e) {
  e.preventDefault();
  section_4.style.display = "none";
  section_1.style.display = "none";
  section_3.style.display = "block";
  section_2.style.display = "none";
});
go_back_page4.addEventListener("click", function (e) {
  e.preventDefault();
  section_4.style.display = "block";
  section_1.style.display = "none";
  section_3.style.display = "none";
  section_2.style.display = "none";
});
