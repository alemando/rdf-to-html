function redirect(e){
    e.preventDefault();
    var iriValue = document.getElementById("iri").value.replace(/\s+/g, '');
    var sparqlEndpointValue = document.getElementById("sparqlEndpoint").value.replace(/\s+/g, '');
    var entityValue = document.getElementById("entity").value.replace(/\s+/g, '');
    url = "?sparqlendpoint="+encodeURIComponent(sparqlEndpointValue)+"&iri="+encodeURIComponent(iriValue)+"&entity="+entityValue;
    window.location.href = url;
}