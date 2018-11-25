import "isomorphic-fetch";
var result;
fetch("http://localhost:5000/uploader",
	{method: 'POST',file: "file"})
.then(function(response){
	return response.json();
})
.then(function(myJson){
	result=JSON.stringify(myJson);
});