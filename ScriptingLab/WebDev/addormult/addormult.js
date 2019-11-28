function mult() {

    var num = document.querySelector(".input").value;
    document.querySelector("h3").innerText = `${num} * 2 = ${num * 2}`;

}

function square() {

    var num = document.querySelector(".input").value;
    document.querySelector("h3").innerText = `${num} * ${num} = ${num * num}`;

}