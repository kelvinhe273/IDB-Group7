function count_exchanges(str){
	/* PLACE HOLDER VALUES UNTIL WE FIGURE OUT THIS SHIT DB	*/

	var id = "ex " + str;
	var ref = ["TOR", "LSE", "ASE", "NMS", "MEX", "FRA", "TAI", "BER", "MUN", "HKG", "PAR"];
	
	if(str.includes(",")){
		var tmp = str.split(",");
		for(i = 0; i < tmp.length; i++){
			tmp[i] = ref.indexOf(trim(tmp[i])) + 1;
		}

		var orig = document.getElementById(id);
		document.getElementById(id).innerHTML = str.split(",")[0];
		document.getElementById(id).href = "/stockmarkets/" + tmp[0];

		for(i = 1; i < tmp.length; i++){
			var div = document.createElement('a');
			div.id = "ex " + trim(str.split(",")[i]);
			div.className = 'exchange';
			div.textContent = ", " + trim(str.split(",")[i]);
			div.href = "/stockmarkets/" + tmp[i];
			orig.appendChild(div);
		}
	}
	else{
		console.log("singular --> " + str);
		document.getElementById(id).innerHTML = str;
		var num = ref.indexOf(trim(str)) + 1;
		document.getElementById(id).href = "/stockmarkets/" + num;
	}
	return true;
}

function count_exchanges_helper(){
	_print();
	//convert nodelist to array
	for (var exchanges = [], i = document.getElementsByClassName('exchange').length - 1; i > -1; --i){
		exchanges[i] = document.getElementsByClassName('exchange')[i];
	}

	var repeated = [];
	for(i = 0; i < exchanges.length; i++){

		if (repeated.indexOf(exchanges[i].textContent) == -1){
			//console.log("NOT REPEATED " + exchanges[i].textContent)
			count_exchanges(trim(exchanges[i].textContent));
			repeated.push(exchanges[i].textContent);
		}
		else{
			//console.log("NOT REPEATED " + exchanges[i].textContent)
		}
	}	
}

function _print(){
	console.log("count_exchanges.js :))");
}

function trim(s){ 
 return ( s || '' ).replace( /^\s+|\s+$/g, '' ); 
}