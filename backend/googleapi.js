const api_key_quickemail =
	"a251a31187060827a22f4d0c9f9b10acb87d5385ad471bcfe0711e7cdeae";
const getBtn = document.getElementById("get-btn");
let input_text = document.getElementById("query");
let show = document.getElementById("show")
function getData() {
	var settings = {
        "Access-Control-Allow-Origin":"*",
        "url": "https://serpapi.com/search?engine=google_scholar&api_key=63468650a4e5a5e9bd66fd100f0e95a1deb21acd2cb05ebe8a2136dbf63301ca&q=biology",
        "timeout": 0,
        "methods": "GET",
    };
    $.ajax(settings).done(function (response) {
        let array = response.organic_results
        array.forEach(element => {
            console.log(element.link)
        });
    });
}

getBtn.addEventListener("click", getData);
