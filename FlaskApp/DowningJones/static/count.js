
/* I THINK THERE ARE PLACE HOLDER VALUES UNTIL I FIGURE OUT HOW TO DYNAMICALLY ASSIGN THEM	*/
//locations
var refc = ["Canada", "Great Britain", "Greece", "United States", "Mexico", "Germany", "Taiwan", "Germany", "Germany", "Hong Kong", "France"];
//currencies
var refu = ["CAD", "GBp", "EUR", "USD", "MXN", "TWD", "HKD"];
//exchanges
var refe = ["TOR", "LSE", "ASE", "NMS", "MEX", "FRA", "TAI", "BER", "MUN", "HKG", "PAR"];

/*
$('table-responsive').bootstrapTable({
    onEventName: count_helper('currency', '', '/currencies/', 'cu ', true)});

$('table-responsive').on('onSort', count_helper('currency', '', '/currencies/', 'cu ', true));
*/




function count(str, classn, k, href, id){
	
	var id = id + str;
	if(classn[0]+classn[1] == "co")
		var ref = refc;
	else if(classn[0]+classn[1] == "cu")
		var ref = refu;
	else
		var ref = refe;

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
		var orig = document.getElementById(id);
		document.getElementById(id).innerHTML = str;
		var num = ref.indexOf(str) + 1;
		document.getElementById(id).href = href + num;
	}
	return true;
}

/* for duplicate cells (same text value)	*/
function change_links(str, classn, k, href, id){
	
	for (var elems = [], i = document.getElementsByClassName(classn + k).length - 1; i > -1; --i){
		elems[i] = document.getElementsByClassName(classn + k)[i];
	}
	var tmp = new Array();
	for(var i = 0; i < elems.length; i++)
		if(trim(str) == trim(elems[i].innerHTML))
			tmp.push(elems[i])

	for (var i = 1; i<tmp.length; i++){
		//console.log(tmp[i])
		tmp[i].href = tmp[0].href;
	}
	
	return true;
}
function count_helper(classn, k, href, id, change_link){
	print();
	//converts nodelist to array
	for (var elems = [], i = document.getElementsByClassName(classn + k).length - 1; i > -1; --i){
		elems[i] = document.getElementsByClassName(classn + k)[i];
		//console.log("TMP " + elems[i].textContent)
	}

	var repeated = [];
	for(i = 0; i < elems.length; i++){

		if (repeated.indexOf(elems[i].textContent) == -1){
			console.log("NOT REPEATED " + elems[i].textContent)
			count(trim(elems[i].textContent), classn, k, href, id);
			if(change_link)
				change_links(trim(elems[i].textContent), classn, k, href, id);
			repeated.push(elems[i].textContent);
		}
		else{
			//console.log("REPEATED " + elems[i].textContent)
		}
	}	
}
function trim(s){ 
	return ( s || '' ).replace( /^\s+|\s+$/g, '' ); 
}
function print(){ 
	console.log("--------- PRINT !!! ---------");
}