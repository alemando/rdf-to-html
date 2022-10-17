function redirect(e){
    e.preventDefault();
    var iriValue = document.getElementById("iri").value.replace(/\s+/g, '');
    var sparqlEndpointValue = document.getElementById("sparqlEndpoint").value.replace(/\s+/g, '');
    var entityValue = document.getElementById("entity").value.replace(/\s+/g, '');
    window.location.href = "?sparqlendpoint="+sparqlEndpointValue+"&iri="+iriValue+"&entity="+entityValue;
}