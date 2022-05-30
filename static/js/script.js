const occupants_details = document.querySelector(".occupants_details");
const add_occupant = document.querySelector(".occupant");
const add_more_occupants = document.querySelector(".add_more_occupants");
const proceed_dependants = document.querySelector(".proceed_dependants");
const section_1 = document.querySelector(".Section_1");
const section_2 = document.querySelector(".section_2");

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

proceed_dependants.addEventListener("click", function (e) {
  e.preventDefault();
  console.log(section_2);
  section_1.style.display = "none";
});

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
