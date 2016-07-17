
/* I THINK THERE ARE PLACE HOLDER VALUES UNTIL I FIGURE OUT HOW TO DYNAMICALLY ASSIGN THEM	*/
var refc = ["Canada", "Great Britain", "Greece", "United States", "Mexico", "Germany", "Taiwan", "Germany", "Germany", "Hong Kong", "France"];
var refe = ["TOR", "LSE", "ASE", "NMS", "MEX", "FRA", "TAI", "BER", "MUN", "HKG", "PAR"];

function count(str, classn, k, href, id){
	
	var id = id + str;

	//console.log(classn[0] + (classn[0] == "c"))
	
	if(classn[0] == "c")
		var ref = refc
	else
		var ref = refe
	
	if(str.includes(",")){
		var tmp = str.split(",");
		for(i = 0; i < tmp.length; i++){

			tmp[i] = ref.indexOf(trim(tmp[i])) + 1;
		}
		var orig = document.getElementById(id);
		document.getElementById(id).innerHTML = trim(str.split(",")[0]);
		document.getElementById(id).href = href + tmp[0];

		for(i = 1; i < tmp.length; i++){
			var div = document.createElement('a');
			div.id = "cr " + str.split(",")[i];
			div.className = classn + k;
			div.textContent = trim(", " + trim(str.split(",")[i]));
			div.href = href + tmp[i];
			orig.appendChild(div);
		}

	}
	else{
		document.getElementById(id).innerHTML = str;
		var num = ref.indexOf(str) + 1;
		document.getElementById(id).href = href + num;
	}
	return true;
}

function count_helper(classn, k, href, id){
	
	//convert nodelist to array
	for (var countries = [], i = document.getElementsByClassName(classn + k).length - 1; i > -1; --i){
		countries[i] = document.getElementsByClassName(classn + k)[i];
	}

	var repeated = [];
	for(i = 0; i < countries.length; i++){

		if (repeated.indexOf(countries[i].textContent) == -1){
			//console.log("NOT REPEATED " + countries[i].textContent)
			count(trim(countries[i].textContent), classn, k, href, id);
			repeated.push(countries[i].textContent);
		}
		else{
			//console.log("NOT REPEATED " + countries[i].textContent)
		}
	}	
}

function trim(s){ 
 return ( s || '' ).replace( /^\s+|\s+$/g, '' ); 
}