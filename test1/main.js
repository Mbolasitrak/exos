
function update_buttons() {
	$.getJSON("buttons.json",function(data) {
		$.each(data,function(key,vtab) {
			// console.log(vtab);
			$("#"+key).text(vtab.content+" ("+vtab.clicks+")");
		});
	});
}

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function init() {

// HERE, WE UPDATE THE CONTENT OF THE 2 BUTTONS
update_buttons();

// SOME JQUERY CODE FOR THE BUTTONS HERE...

// URL FOR BUTTON1 : /bouton1
// BUTTON1 WHEN CLICKED WILL BECOME : Voici le Bouton 1 (1)
// BUTTON1 WHEN CLICKED AGAIN WILL BECOME : Voici le Bouton 1 (2)
// AND SO ON... ie: BUTTON1 WHEN CLICKED number of clicks TIMES WILL BECOME : Voici le Bouton 1 (number of clicks)

	$("#bouton1").click(function () {
		httpGet('/bouton1')
		update_buttons()
	})

// URL FOR BUTTON2 : /bouton2
// BUTTON2 WHEN CLICKED WILL BECOME : Et ceci est le Bouton 2 (1)
// BUTTON2 WHEN CLICKED AGAIN WILL BECOME : Et ceci est le Bouton 2 (2)
// AND SO ON... ie: BUTTON2 WHEN CLICKED number of clicks TIMES WILL BECOME : Et ceci est le Bouton 2 (number of clicks)
	$("#bouton2").click(function () {
		httpGet('/bouton2')
		update_buttons()
	})


}

