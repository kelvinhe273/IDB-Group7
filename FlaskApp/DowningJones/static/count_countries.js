function count_countries(str){
	/* PLACE HOLDER VALUES UNTIL WE FIGURE OUT THIS SHIT DB	*/
	var id = "cr " + str;
	var ref = ["Canada", "Great Britain", "Greece", "United States", "Mexico", "Germany", "Taiwan", "Germany", "Germany", "Hong Kong", "France"];
	
	if(str.includes(",")){
		var tmp = str.split(",");
		for(i = 0; i < tmp.length; i++){

			tmp[i] = ref.indexOf(trim(tmp[i])) + 1;
		}
		var orig = document.getElementById(id);
		document.getElementById(id).innerHTML = str.split(",")[0];
		document.getElementById(id).href = "/locations/" + tmp[0];

		for(i = 1; i < tmp.length; i++){
			var div = document.createElement('a');
			div.id = "cr " + str.split(",")[i];
			div.className = 'country';
			div.textContent = ", " + str.split(",")[i];
			div.href = "/locations/" + tmp[i];
			orig.appendChild(div);
		}

	}
	else{
		document.getElementById(id).innerHTML = str;
		var num = ref.indexOf(str) + 1;
		document.getElementById(id).href = "/locations/" + num;
	}
	return true;
}

function count_countries_helper(){
	
	//convert nodelist to array
	_print2();
	for (var countries = [], i = document.getElementsByClassName('country').length - 1; i > -1; --i){
		countries[i] = document.getElementsByClassName('country')[i];
	}

	var repeated = [];
	for(i = 0; i < countries.length; i++){

		if (repeated.indexOf(countries[i].textContent) == -1){
			//console.log("NOT REPEATED " + countries[i].textContent)
			count_countries(trim(countries[i].textContent));
			repeated.push(countries[i].textContent);
		}
		else{
			//console.log("NOT REPEATED " + countries[i].textContent)
		}
	}	
}

function _print2(){
	console.log("count_countries.js :))");
}

function trim(s){ 
 return ( s || '' ).replace( /^\s+|\s+$/g, '' ); 
}