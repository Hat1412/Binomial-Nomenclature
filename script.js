import file from "./nomenclature.json" assert { type: "json" };
var cn = document.getElementById("cn");
var bn = document.getElementById("bn");

for (let x in file) {
  var a = document.createElement("option");
  a.value = x;
  a.innerHTML = x;
  cn.appendChild(a);

  var b = document.createElement("option");
  b.value = file[x];
  b.innerHTML = file[x];

  bn.appendChild(b);
}

function chk() {
  bn.value = file[cn.value];
}

function anti_chk() {
  for (const [key, value] of Object.entries(file)) {
    if (value === bn.value) {
      cn.value = key;
    }
  }
}

cn.addEventListener("click", chk);
bn.addEventListener("click", anti_chk);
