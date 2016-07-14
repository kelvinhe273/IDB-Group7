function count_countries(str){
	/* PLACE HOLDER VALUES UNTIL WE FIGURE OUT THIS SHIT DB	*/
	var id = "results " + str;
	var ref = ["Canada", "Great Britain", "Greece", "United States", "Mexico", "Germany", "Taiwan", "Germany", "Germany", "Hong Kong", "France"];
	
	if(str.includes(",")){
		var tmp = str.split(",");
		for(i = 0; i < tmp.length; i++)
			tmp[i] = ref.indexOf(tmp[i]) + 1;

		//console.log("if: " + tmp);

		//console.log("link: " + "/locations/" + tmp[0]);
		//console.log("id: " + "/locations/" + id);
		document.getElementById(id).href = "/locations/" + tmp[0];
	}
	else{
		//console.log("else: " + str);
		str = ref.indexOf(str) + 1;
		//console.log("link: " + "/locations/" + str);
		//console.log("id: " + id);
		document.getElementById(id).href = "/locations/" + str;
	}
	return true;
}

function count_countries_helper(){
	console.log("GJGJGJG");
	countries = document.getElementsByClassName("country");
	var repeated = [];

	for(i = 0; i< countries.length; i++){
		console.log(i + ": " + trim(countries.item(i).textContent) + " " + countries.length);

		//countries.item(i).innerHTML = trim(countries.item(i).textContent);

		if (repeated.indexOf(countries.item(i).textContent) == -1){
			console.log(countries.item(i).textContent + " NOT REPEATED")
			count_countries(trim(countries.item(i).textContent));
			repeated.push(countries.item(i).textContent);
		}
		else{
			console.log(countries.item(i).textContent + " REPEATED")
		}
	}
	
}

function _print(){
	console.log("called print");
}

function trim(s){ 
 return ( s || '' ).replace( /^\s+|\s+$/g, '' ); 
}