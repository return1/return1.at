if(typeof console === "undefined") {
    console = { log: function() { }, info: function(){} };
} 
	
$(document).ready(function() { 

    //directly insert a external js on the page
    //var turkish = '<script src="http://advert.istanbul.net/advertpro/servlet/view/dynamic/javascript/zone?zid=445&pid=0&custom1=1&custom2=M&custom3=200"></script>';
    //$('#test1').writeCapture().html(turkish, function() {
    //	console.info("loaded turkish ads, we could apply some styling here..");
    //});

    //load content via ajax which contains document.write()
    $.get('chain/chain.html', function(data) {
	$('#test2').writeCapture().html(data, function() {
	    //console.info("loaded doubleclick ads, we could apply some styling here..");
	});
    });

});
