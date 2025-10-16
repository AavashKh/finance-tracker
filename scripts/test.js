console.log("JS file loaded!");

function button() {
    const input = document.querySelector("#stock-name");
    const greeting = document.querySelector("#greeting");

    input.addEventListener("keydown", function(event) {
        if (event.key == 'Enter') {
            greeting.textContent = 'You searched for ${input.value}';
        }
    });
}

button();