/* Part 2 */
console.log('PART 2')

for (let i = 0; i < 20; i++) {
    console.log(i+1)
}

/* Part 3 */
console.log('PART 3')

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for (let i = 0; i < numbers.length; i++) {
    const e = numbers[i];
    let s = "";

    if (e % 3 === 0){
        s += "eple";
    }
    if (e % 5 === 0){
        s += "kake";
    }
    if (s === "") {
        s = e;
    }

    console.log(s);
}

/* Part 4 */
const title = document.getElementById("title");
title.innerHTML = "Hello, JavaScript"

/* Part 5 */
const magic = document.getElementById("magic"); 

function changeDisplay() {
    magic.style.display = "none";
}

function changeVisibility() {
    magic.style.visibility = "hidden";
    magic.style.display = "block";
}

function reset() {
    magic.style.display = "block";
    magic.style.visibility = "visible";
}

/* Part 6 */
const tech = document.getElementById("tech");

const technologies = [
    'HTML5',
    'CSS3',
    'JavaScript',
    'Python',
    'Java',
    'AJAX',
    'JSON',
    'React',
    'Angular',
    'Bootstrap',
    'Node.js'
];

for (let i = 0; i < technologies.length; i++){
    tech.innerHTML += `<li>${technologies[i]}</li>`;
}